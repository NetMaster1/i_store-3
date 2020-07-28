from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject')

# Register your models here.
admin.site.register(Review, ReviewAdmin),