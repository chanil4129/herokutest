from rest_framework import serializers
from LibraryApp.models import Client,Book

#Serializer

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Client
        fields=('ClientIndex',
                'ClientId')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=('BookIndex',
                'BookName',
                'Bookstate',
                'LendDate',
                'ReturnDate',
                'PhotoFileName')