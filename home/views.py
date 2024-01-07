from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Home(APIView):
    def get(self, request):
        return Response(status.HTTP_200_OK)