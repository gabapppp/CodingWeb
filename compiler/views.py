from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from compiler.utils.runner import run_code
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from rest_framework.permissions import AllowAny, IsAuthenticated


class CompileCodeView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        code = request.data['code']
        language = request.data['language'].strip()
        version = int(request.data['version'])
        output = run_code(code, language, version)
        result = output['result']  if 'result' in output else ''
        return Response(result, status=status.HTTP_200_OK)
        
