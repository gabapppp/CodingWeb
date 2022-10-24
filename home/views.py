from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from home.serializers import SourceSerializer
from .executeCode import execute_cpp_code, execute_python_code


# from home.models import Source
# Create your views here.

class SourceCreateView(CreateAPIView):
    serializer_class = SourceSerializer

    def post(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data.get("stdin"));
            if serializer.data.get("language") == "python":
                return Response(execute_python_code(serializer.data.get("source_code"), serializer.data.get("stdin")))
            if serializer.data.get("language") == "cpp":
                return Response(execute_cpp_code(serializer.data.get("source_code"), serializer.data.get("stdin")))
