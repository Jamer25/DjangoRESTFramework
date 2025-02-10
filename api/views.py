from rest_framework import viewsets
from .serializer import ProgrammerSerializer
from .models import Programmer

# Create your views here.

class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset=Programmer.objects.all() ##forma de listar elementos de un modelo
    #a través del ORM (object relational mapping) para a través de clases poder manipular los elementos de una tabla
    ##queryset es la lista de elementos que estamos accediendo mediante el orm de django
    serializer_class=ProgrammerSerializer