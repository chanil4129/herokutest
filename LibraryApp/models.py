from django.db import models

# Create your models here.
# DB 모델(자료형)

class Client(models.Model):
    ClientIndex=models.AutoField(primary_key=True)
    ClientId=models.CharField(max_length=100)

class Book(models.Model):
    BookIndex=models.AutoField(primary_key=True)
    BookName=models.CharField(max_length=100)
    Bookstate=models.CharField(max_length=100)  #boolean형으로 바꾸기
    LendDate=models.DateField()
    ReturnDate=models.DateField()
    PhotoFileName=models.CharField(max_length=100)