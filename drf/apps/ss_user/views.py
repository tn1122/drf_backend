# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import SsUser
from .serializer import SsUserSerializer

class SsuserViewSet(ModelViewSet):

    queryset = SsUser.objects.all()
    serializer_class = SsUserSerializer

