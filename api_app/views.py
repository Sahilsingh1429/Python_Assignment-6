from django.shortcuts import render
from rest_framework.views import *
from .serializers import *
from rest_framework.response import Response
# Create your views here.

class CreateData(APIView):
    
    def post(self,request):
        ser_obj = Door(data = request.data)
        if ser_obj.is_valid():
            ser_obj.save()
            all_books = Book.objects.all()
            ser_n_obj = Door(all_books,many = True)
            return Response(ser_n_obj.data)
        else:
            return Response(ser_obj.errors)
        
        
class GetData(APIView):
    
    def get(self,request,bid):
            b1 = Book.objects.get(id=bid)
            ser_obj = Door(b1)
       
            return Response(ser_obj.data)
        
        
class UpdateData(APIView):
    
    def put(self,request,bid):
        b1 = Book.objects.get(id=bid)
        ser_obj = Door(b1, data = request.data)
        if ser_obj.is_valid():
            ser_obj.save()
            all_books = Book.objects.all()
            ser_n_obj = Door(all_books,many = True)
            return Response(ser_n_obj.data)  
        else:
            return Response(ser_obj.errors)
        

class DeleteData(APIView):
    
    def delete(self,request,bid):
        b1 = Book.objects.get(id = bid)
        b1.delete()
        all_books = Book.objects.all()
        ser_n_obj = Door(all_books,many = True)
        return Response(ser_n_obj.data)
    
class AllData(APIView):
    
    def get(self,request):
            all_books = Book.objects.all()
            ser_n_obj = Door(all_books,many = True)
            return Response(data = ser_n_obj.data)
        
        
        
     
        
        
        
    
        