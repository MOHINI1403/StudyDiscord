from django.shortcuts import render,redirect
from django.db.models import Q

from django.http import HttpResponse
from .models import Room,Topic,Message,User
from .form import RoomForm,UserForm,MyUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required
# Create your views here.
#Functions or classes and they are going to fire actions when a person goes to a particular url

#To create a view

#rooms=[
    #{'id':1,'name':'Lets Learn Python!'},
    #{'id':2,'name':'Design with me'},
    #{'id':3,'name':'Okie that'},
#]

#Never use login as a function name 
def loginPage(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        email=request.POST.get('email').lower()
        password=request.POST.get('password')
        try:
            user=User.objects.get(email=email)
        except:
            messages.error(request,'User Does Not Exist')
        
        user=authenticate(request,email=email,password=password)#to check weather the credentials right or not
        if user is not None:
            login(request,user)#this will add the session in the database and the browser
            return redirect('home')#if the authentication 
        else:
            messages.error(request,'Username or password does not exist')
        
    context={'page':page}
    return render(request,'base/login_register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    
    form=MyUserCreationForm()
    if request.method=='POST':
        form=MyUserCreationForm(request.POST)#Getting all the details into the form variable
        if form.is_valid():
            user=form.save(commit=False)#We are saving the details and freezing the details
            user.username=user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'An error Occured during registration')
            
            
    return render(request,'base/login_register.html',{'form':form})
    
def home(request):
    #what kind of request
    q=request.GET.get('q') if request.GET.get('q')!=None else ''#In the end it will contains the vlue of the 'q' parameter in the GET request
    #rooms=Room.objects.all()#this would give all the rooms in the room folder
    rooms=Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
        #filter this value down with the query mentioned whatever value in topic name 
    topics=Topic.objects.all()[0:5] #Limiting the topics list to only 5 into the list topics
    room_count=rooms.count()
    room_messages=Message.objects.filter(Q(room__topic__name__icontains=q)).order_by('-created')
    
    
    context={'rooms':rooms,'topics':topics,'room_count':room_count,'room_messages':room_messages}
    return render(request,'base/home.html',context)#http response is returned and it returns with this value 

def room(request,pk):
    #pk=Primary Key
   
    #rooms=Room.objects.filter(topic__name=q)#filter this value down with the query mentioned 
    room=Room.objects.get(id=pk)
    Roommessages=room.message_set.all().order_by('-created')#to fetch all the messages which are related to a particular room
    #the message are sorted in descending order
    participants=room.participants.all()
    
    if request.method=='POST':
        #We have a create method and we will go ahead and create the actual messgae
        message=Message.objects.create(
            
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)#this user will be added to the many to many feild 
        return redirect('room',pk=room.id)
    context={'room':room,'Roommessages':Roommessages,'participants':participants}
    return render(request,'base/room.html',context)
#this view renders the html page which is a form to create new room

def userProfile(request,pk):
    user=User.objects.get(id=pk)#This would fetch me the user who's messgae was that 
    rooms=user.room_set.all()
    
    room_messages=user.message_set.all()
    topics=Topic.objects.all()
    context={'user':user,'rooms':rooms,'room_messages':room_messages,'topics':topics}
    return render(request,'base/profile.html',context)
@login_required(login_url='login')
def createRoom(request):
    form=RoomForm()
    topics=Topic.objects.all() #this would fetch all the topics
    
    if request.method=='POST':
        #all the data entered into the form
        topic_name=request.POST.get('topic')
        topic,created=Topic.objects.get_or_create(name=topic_name) #created will store the value weather we are creating the ne topic or not as true and false
        
        # a new Room objeect is created using this 
        
        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            
        )
        #form=RoomForm(request.POST)
        #if form.is_valid():
            
            #room=form.save(commit=False)#this would save that model into database
            #room.host=request.user #we can only create the room who is logged in
            #room.save()
            
        return redirect('home') #here 'home' is the name of the urlPattern on which we need to be redirected
        
        
    context={'form':form,'topics':topics}
    return render(request,'base/room_form.html',context)


@login_required(login_url='login')
def updateRoom(request,pk):
    room=Room.objects.get(id=pk)
    form=RoomForm(instance=room)
    topics=Topic.objects.all()
    #If the user is trying to edit someone else room details
    
    if request.user !=room.host:
        return HttpResponse('You Are Not Allowed Here')
    
    
    if request.method=='POST':
        topic_name=request.POST.get('topic')
        topic,created=Topic.objects.get_or_create(name=topic_name)
        room.name=request.POST.get('name')
        room.topic=topic
        room.description=request.POST.get('description')
        room.save()
        
        return redirect('home')
    context={'form':form,'topics':topics}
    return render(request,'base/room_form.html',context)
    
@login_required(login_url='login')
def deleteRoom(request,pk):
    room=Room.objects.get(id=pk)
    
    
    if request.method=='POST':
        room.delete()#remove that item from the database and deleting it 
        return redirect('home')#If the user deleted the room 
    return render(request,'base/delete.html',{'obj':room})#The room would be called object in the template


@login_required(login_url='login')
def deleteMessgae(request,pk):
    message=Message.objects.get(id=pk)
    if request.user != message.user:
        return HttpResponse('You are not allowed to delete')
        
    if request.method=='POST':
        message.delete()#remove that item from the database and deleting it
         
        return redirect('home')#If the user deleted the room 
    return render(request,'base/delete.html',{'obj':message})#The room would be called object in the template

@login_required(login_url='login')
def updateUser(request):
    user=request.user
    form=UserForm(instance=user)
    if request.method=='POST':
        form=UserForm(request.POST,request.FILES,instance=user) # This line creates an instance of a form class called UserForm and populates it with the data from the user object. This is typically used for pre-filling the form with the user's existing data when rendering the update page
        if form.is_valid():
            form.save()
            return redirect('user-profile',pk=user.id)
    return render(request,'base/update-user.html',{'form':form})


def topicsPage(request):
    q=request.GET.get('q') if request.GET.get('q') !=None else ''
    topics=Topic.objects.filter(name__icontains=q)
    return render(request,'base/topics.html',{'topics':topics})

def activityPage(request):
    room_messages=Message.objects.all()
    return render(request,'base/activity.html',{'room_messages':room_messages})