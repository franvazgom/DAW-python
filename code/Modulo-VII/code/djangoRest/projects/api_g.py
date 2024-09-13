from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from projects.serializers import SumaSerializer, ProjectParameterSerializer
from django.core.serializers.json import DjangoJSONEncoder
from projects.data import Data
import json

class ProjectService(APIView):
    def post(self, request):
        serializer = ProjectParameterSerializer(data=request.data)
        if serializer.is_valid():
            parametros = serializer.validated_data['parametros']            
            data = Data()
            res = data.get_projects(parametros)
            res = json.dumps(list(res.values()), cls=DjangoJSONEncoder)
            return Response({'resultado':res}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DataTest(APIView):
    def get(self, request):
        data = Data()
        return Response({'resultado':data.get_test_data()}, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = SumaSerializer(data=request.data)
        if serializer.is_valid():
            n1 = serializer.validated_data['num1']
            n2 = serializer.validated_data['num2']
            data = Data()
            return Response({'resultado':data.get_suma(n1, n2)}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
