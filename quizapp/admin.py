from django.contrib import admin


# Register your models here.

from .models import Movies, Myusers, Series, Books, config, question

admin.site.register(Movies)
admin.site.register(Myusers)
admin.site.register(Series)
admin.site.register(Books)
admin.site.register(config)
admin.site.register(question)