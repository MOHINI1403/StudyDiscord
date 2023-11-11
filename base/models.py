from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    name=models.CharField(max_length=200,null=True)
    email=models.EmailField(unique=True,null=True)
    bio=models.TextField(null=True)
    
    avatar=models.ImageField(null=True,default="avatar.svg")
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
# Create your models here.




class Topic(models.Model):
    #Q topic would have multiple rooms but a room could have multiple topics
    
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Room(models.Model):
   # host=models.CharField
    host=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    topic=models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)#null=True means that database cannot have a row with this value blank we can't keep it blank
    participants=models.ManyToManyField(User,related_name='participants',blank=True)
    updated=models.DateTimeField(auto_now=True)#every time the save method is called update the timeStamp
    created=models.DateTimeField(auto_now_add=True)
    #Auto_now takes the snapsnot everytime but autoNow_add takes the snapshot when we first save or create this instance
    class Meta:
        # no dash in front of these first it sort in asc order anfd when there is a dash it sort it in desc order
        
        ordering:['-updated','-created']
    def __str__(self):
        return self.name
    
class Message(models.Model):

    #Establishing many to one relationshsip
    user=models.ForeignKey(User,on_delete=models.CASCADE)#One user could have multiple msgs butmultiple msgs could be 
    room=models.ForeignKey(Room,on_delete=models.CASCADE)#all the messages will be deleted if the particular room is deleted
    body=models.TextField()
    updated=models.DateTimeField(auto_now=True)#every time the save method is called update the timeStamp
    created=models.DateTimeField(auto_now_add=True)
    class Meta:
        # no dash in front of these first it sort in asc order anfd when there is a dash it sort it in desc order
        
        ordering:['-updated','-created']
    def __str__(self):
        return self.body[0:50]
