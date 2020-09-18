from django.contrib import admin
from .models import Entity, Person
from django.contrib.auth.models import User


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')  # dispays columns we need
  
class EntityAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')  # dispays columns we need
   
# Register your models here.
admin.site.register(Person, PersonAdmin),
admin.site.register(Entity, EntityAdmin),

