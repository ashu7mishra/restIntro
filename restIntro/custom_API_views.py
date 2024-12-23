from rest_framework import viewsets, status
from rest_framework.views import APIView
from .models import User
from .serializer import UserSerializer
from rest_framework.response import Response


class UserListCreateAPIViews(APIView):

    def get(self,request):
        users = User.objects.all()
        serialized = UserSerializer(users, many=True)
        return Response(serialized.data)

    def post(self,request):
        serialized = UserSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)