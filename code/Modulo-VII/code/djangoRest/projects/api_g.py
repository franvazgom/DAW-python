from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from projects.data import Data
import json

class DataTest(APIView):
    def get(self, request):
        data = Data()
        return Response({'resultado':data.get_test_data()}, status=status.HTTP_200_OK)