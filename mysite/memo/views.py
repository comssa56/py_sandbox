from django.db.models.query import QuerySet
import django_filters

from django.http import HttpResponse
from rest_framework import viewsets, filters

from .models import Memo
from .serializer import MemoSerializer

def index(request):
    return HttpResponse("Hello, world")



class MemoViewSet(viewsets.ModelViewSet):
    queryset = Memo.objects.all()
    serializer_class = MemoSerializer

