from django.contrib.auth.models import AbstractUser, User
from rest_framework import generics, response, status

from ThirdModuleOrenburgBackend.serializers import RegisterSerializer


class RegisterUserApi(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        user = self.serializer_class(data=request.POST)
        if user.is_valid():
            user.save()
            user_retrieved = User.objects.get(username=user.data['username'])
            raw_user_password = user.data['password']
            user_retrieved.set_password(raw_user_password)
            user_retrieved.save()
            return response.Response(status=status.HTTP_201_CREATED)
        else:
            return super().post(request, *args, **kwargs)
