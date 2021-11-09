from django.contrib import admin

# Register your models here.
from .models import review,novels
admin.site.register(review)
admin.site.register(novels)
