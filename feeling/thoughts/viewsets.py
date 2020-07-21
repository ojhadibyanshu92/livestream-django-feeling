from rest_framework import viewsets
from . import serilizers
from . import models


class ThoughtViewSet(viewsets.ModelViewSet):
    serializer_class = serilizers.ThoughtSerializer

    def get_queryset(self):
        return self.request.user.thoughts.all()

