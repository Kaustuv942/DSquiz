from django.contrib import admin

# Register your models here.

from .models import Movies, Myusers, Series, Books

admin.site.register(Movies)
admin.site.register(Myusers)
admin.site.register(Series)
admin.site.register(Books)
