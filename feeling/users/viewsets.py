from django.contrib.auth.models import User

from rest_framework import viewsets
from . import serilizers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serilizers.UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
