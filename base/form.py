from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room,User

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['name','username','email','password1','password2']
#Form for the room
class RoomForm(ModelForm):
    #Two min value we need here
    class Meta:
        model=Room
        fields='__all__'
        exclude=['host','participants']
        #this feilds could also be a list
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar','name','username', 'email','bio']