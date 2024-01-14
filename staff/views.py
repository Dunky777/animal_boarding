from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        return Response({"message": "Пау пау, вы авторизованный пользователь!"})