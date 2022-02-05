from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from LibraryApp.models import Client,Book
from LibraryApp.serializers import ClientSerializer,BookSerializer

from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def Lib_Client_APi(request, index=0):
    if request.method=='GET':
        client=Client.objects.all()
        client_serializer=ClientSerializer(client,many=True)
        return JsonResponse(client_serializer.data,safe=False)
    elif request.method=='POST':        #create
        client_data=JSONParser().parse(request)
        client_serializer=ClientSerializer(data=client_data)
        if client_serializer.is_valid():
            client_serializer.save()
            return JsonResponse("Added Successfully!!",safe=False)
        return JsonResponse("Failsed to Add",safe=False)
    elif request.method=='PUT':         #update
        client_data=JSONParser().parse(request)
        client=Client.objects.get(ClientIndex=client_data['ClientIndex'])
        client_serializer=ClientSerializer(client,data=client_data)
        if client_serializer.is_valid():
            client_serializer.save()
            return JsonResponse("Updated Successfully!",safe=False)
        return JsonResponse("Failed to Update",safe=False)
    elif request.method=='DELETE':      #Delete
        client=Client.objects.get(ClientIndex=index)
        client.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def Lib_Book_APi(request, index=0):
    if request.method=='GET':
        book=Book.objects.all()
        book_serializer=BookSerializer(book,many=True)
        return JsonResponse(book_serializer.data,safe=False)
    elif request.method=='POST':        #create
        book_data=JSONParser().parse(request)
        book_serializer=BookSerializer(data=book_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse("Added Successfully!!",safe=False)
        return JsonResponse("Failsed to Add",safe=False)
    elif request.method=='PUT':         #update
        book_data=JSONParser().parse(request)
        book=Book.objects.get(BookIndex=book_data['BookIndex'])
        book_serializer=BookSerializer(book,data=book_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse("Updated Successfully!",safe=False)
        return JsonResponse("Failed to Update",safe=False)
    elif request.method=='DELETE':      #Delete
        book=Book.objects.get(BookIndex=index)
        book.delete()
        return JsonResponse("Deleted Successfully",safe=False)


@csrf_exempt
def SaveFile(request):
    file=request.FILES['uploadedFile']
    file_name=default_storage.save(file.name,file)

    return JsonResponse(file_name,safe=False)
