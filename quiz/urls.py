"""quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url


from quizapp import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    
    url(r'^choosefile/', views.choose, name='choose'),
    url(r'^end/', views.end, name='end'),
    url(r'^questions/movies/$', views.questionmovies, name='questions_of_movies'),
    url(r'^questions/series/$', views.questionseries, name='questions_of_series'),
    url(r'^questions/books/$', views.questionbooks, name='questions_of_books'),
    url(r'^leaderboard/', views.leaderboard, name='leaderboard'),
    path('accounts/login/', views.login),
    path('admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
 

]
