from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from home.serializers import SourceSerializer


# from home.models import Source
# Create your views here.

class SourceCreateView(CreateAPIView):
    serializer_class = SourceSerializer

    def post(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data)
        import subprocess
        import sys
        if serializer.is_valid():
            output = subprocess.run([sys.executable, "-c", serializer.data.get("source_code")], capture_output=True, text=True)
            if output.stderr != "":
                return Response({
                    "error": output.stderr, }
                    , status=status.HTTP_400_BAD_REQUEST)
            return Response({"output": output.stdout}, status=status.HTTP_200_OK)
