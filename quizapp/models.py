from django.db import models


from django.contrib.auth.models import User

import datetime
from collections import Counter



# Create your models here.


class Myusers(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50,default=None,unique=True)
    choice = models.CharField(max_length=30,null=True)
    pointsfactor = models.IntegerField(default=0)   # The no. of correct answers
    rank=models.IntegerField(null=True)
    lastcorrectans = models.DateTimeField(auto_now=True)

    class Meta:
        ordering =['-pointsfactor','lastcorrectans']

    def ranks(self):
        players=self.objects.all()
        rank=1
        for player in players:
            player.rank=rank
            player.pointsfactor= player.pointsfactor*10
            rank +=1
        return players

    def scoreupdate(player):
        player.pointsfactor+=1
        player.save()

    def __str__(self):
        return "{}".format(self.name)

class Movies (models.Model):
    order = models.IntegerField(default=0, unique=True, primary_key=True)
    question = models.CharField(max_length=5000)
    islink = models.BooleanField(default=False)
    link = models.CharField(max_length=450, null=True)
    ispic = models.BooleanField(default=False)
    image = models.URLField(max_length=1000, null=True)
    answer = models.CharField(max_length=50)
    day=models.IntegerField(default=1)

    def __str__(self):
        return "{}".format(self.question)

    def check_ans(self,answer,question):
        string = question.answer.lower()
        answer = answer.lower()
        answers=string.split(",")
        for ans in answers:
            if answer==ans:


                return True
        return False

        # #answer checker is messed up too//fixed. gaps are not respected tho.take care
        # if(Counter(answer) == Counter(question.answer)):
        #     return True
        # else:
        #     return False

       

    def get_next_question(self,day,qno):
        question=self.objects.filter(day=day,order=qno)
        return question


    

class Series (models.Model):
    order = models.IntegerField(default=0, unique=True)
    question = models.CharField(max_length=5000)
    islink = models.BooleanField(default=False)
    link = models.CharField(max_length=450, null=True)
    ispic = models.BooleanField(default=False)
    image = models.URLField(max_length=1000, null=True)
    answer = models.CharField(max_length=50)
    day=models.IntegerField(default=1)

    def __str__(self):
        return "{}".format(self.question)

    def check_ans(self,answer,question):
        string = question.answer.lower()
        answer = answer.lower()
        answers=string.split(",")

        for ans in answers:
            if answer==ans:
                return True
        return False

    def get_next_question(self,day,qno):
        question=self.objects.filter(day=day,question_no=qno)
        return question


class Books (models.Model):
    order = models.IntegerField(default=0, unique=True)
    question = models.CharField(max_length=5000)
    islink = models.BooleanField(default=False)
    link = models.CharField(max_length=450, null=True)
    ispic = models.BooleanField(default=False)
    image = models.URLField(max_length=1000, null=True)
    answer = models.CharField(max_length=50)
    day=models.IntegerField(default=1)

    def __str__(self):
        return "{}".format(self.question)

    class Meta:
        ordering=['day','order']


    def check_ans(self,answer,question):
        string = question.answer.lower()
        answer = answer.lower()
        answers=string.split(",")
        for ans in answers:
            if answer==ans:
                return True
        return False

    def get_next_question(self,day,qno):
        question=self.objects.filter(day=day,question_no=qno)
        return question





