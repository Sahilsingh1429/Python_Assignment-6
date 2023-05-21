from rest_framework.serializers import ModelSerializer
from .models import *

class Door(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        # excludes = 'Isbn'
        # fields = ('title','author','publisher')