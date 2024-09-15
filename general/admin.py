from django.contrib import admin
from general import  models
from general.models import ContactModel,LoginModel

# Register your models here.
admin.site.register(ContactModel)
admin.site.register(LoginModel)

