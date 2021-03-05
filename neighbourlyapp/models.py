from django.db import models
import re
from datetime import date
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.


# Managers here.
class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors= {}
        if len(postData['formfname'])<2:
            errors['formfname']= 'First name is not quite long enough. Try again.'
        if len(postData['formlname'])<2:
            errors['formlname']= 'Last name is not quite long enough. Try again.'
        if not EMAIL_REGEX.match(postData['formemail']):
            errors['formemail']= 'Invalid email address'
        if User.objects.filter(email=postData['formemail']):
            errors['formemail']= 'There can only be one-- Highlander. Email is taken, try again.'
        if len(postData['formpassword'])<8: 
            errors['formpassword']= 'Your password must be more than eight(8) characters!'
        if postData['formpassword'] != postData['checkformpassword']:
            errors['checkformpassword']= 'Passwords do not match. Check yourself, before you wreck yourself.'
        return errors
    def login_validator(self, postData):
        errors= {}
        if not EMAIL_REGEX.match(postData['formemail']):
            errors['formemail']= 'Invalid email address'
        if not User.objects.filter(email=postData['formemail']):
            errors['formemail']= 'Password/Email mismatch.'
        if len(postData['formpassword'])<8: 
            errors['formpassword']= 'Your password must be more than eight(8) characters!'
        return errors
class ToolManager(models.Manager):
    def tool_validator(self, postData):
        errors= {}
        if len(postData['formitem_name'])==0:
            errors['formitem_name'] = 'Item Name is required'
        elif len(postData['formitem_name']) < 2:
            errors['formitem_name'] = 'Your Item Name should be at least 2 characters'
        # else:
        #     errors['formitem_name'] = 'Item Name is required'
        # if postData['formtitle']:
        if len(postData['formtitle'])==0:
            errors['formtitle'] = 'Your Description  should be at least 3 characters'
        elif len(postData['formtitle']) < 3:
            errors['formtitle'] = 'Description is required'
        # if postData['formlocation']:
        if len(postData['formlocation']) ==0:
            errors['formlocation'] = 'Location is required'
        elif len(postData['formlocation']) <3:
            errors['formlocation'] = 'Your Location  should be at least 3 characters'
        # if postData['formstart_date']:
        if len(postData['formstart_date'])==0:
            errors['formstart_date'] = 'Start Date is required' 
        elif len(postData['formstart_date']) < 3:
            errors['formstart_date'] = 'Your Start Date should be at least 3 characters'
            # if postData['formend_date']:
        if len(postData['formend_date'])==0:
            errors['formend_date'] = 'End Date is required' 
        elif len(postData['formend_date']) < 3:
            errors['formend_date'] = 'Your End Date should be at least 3 characters'
        return errors
#######################################################################
# Create your models here.
class User(models.Model):
    #id
    first_name= models.CharField(max_length=60)
    last_name= models.CharField(max_length=60)
    email= models.CharField(max_length=50)
    password= models.CharField(max_length=30)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects= UserManager()
###########################################################
class Tool(models.Model):
    #id
    item_name = models.CharField(max_length=60)
    description =models.CharField(max_length=250)
    location= models.CharField(max_length=60)
    start_date = models.DateTimeField(default=date.today)
    end_date = models.DateTimeField(default=date.today)
    user = models.ForeignKey(User, related_name='tools', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ToolManager()    
