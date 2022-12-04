from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework import permissions, status
from rest_framework.response import Response
from .serializers import SourceSerializer, ExecuteSerializer
from .models import Source
from .executeCode import execute_cpp_code, execute_python_code

# Create your views here.


class SourceCreateView(ListCreateAPIView):
    serializer_class = SourceSerializer
    queryset = Source.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Source.objects.filter(author=user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ExecuteView(CreateAPIView):
    serializer_class = ExecuteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            fileID = serializer.data.get('fileID')
            if not (Source.objects.filter(id=fileID).exists()):
                return Response("File doesn't exist!", status=status.HTTP_204_NO_CONTENT)

            source = Source.objects.get(id=fileID)

            source_serializer = SourceSerializer(source)
            filename = source_serializer.data.get('filename')
            path = 'media/user_{0}/{1}'.format(
                2, filename)

            if source_serializer.data.get("language") == "PY":
                return Response(execute_python_code(path, serializer.data.get("stdin")))
            if source_serializer.data.get("language") == "CPP":
                return Response(execute_cpp_code(path, serializer.data.get("stdin")))
        return Response(status=status.HTTP_400_BAD_REQUEST)
