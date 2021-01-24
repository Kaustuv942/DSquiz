from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from collections import Counter
import datetime
import pytz

utc=pytz.UTC



# Create your models here.


class Myusers(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50,default=None,unique=True)
    choice = models.CharField(max_length=30,null=True)
    score = models.IntegerField(default=0)   # The no. of correct answers
    rank=models.IntegerField(null=True)
    day = models.IntegerField(default=1)
    qno = models.IntegerField(default = 1)
    lastcorrectans = models.DateTimeField(auto_now=True)

    class Meta:
        ordering =['-score','lastcorrectans']

    def ranks(self):
        players=self.objects.all()
        rank=1
        active = config.current_config(config)
        for player in players:
            player.rank=rank  
            rank +=1
        return players

    # def scoreupdate(player):
    #     player.pointsfactor+=1
    #     player.save()

    def __str__(self):
        return "{}".format(self.name)


class question (models.Model):
    order = models.IntegerField(default=0)
    question = models.CharField(max_length=5000)
    islink = models.BooleanField(default=False)
    link = models.CharField(max_length=450, null=True, blank = True)
    ispic = models.BooleanField(default=False)
    image = models.URLField(max_length=1000, null=True, blank = True)
    answer = models.CharField(max_length=50)
    day=models.IntegerField(default=1)

    def __str__(self):
        return "{}".format(self.question)
    
    class Meta:
        unique_together = ('day', 'order',)
        ordering=['day','order']

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


class config(models.Model):
    current_day=models.IntegerField()
    q_no=models.IntegerField()
    quiz_active=models.BooleanField(default=True)
    quiz_start=models.DateTimeField()
    quiz_endtime=models.DateTimeField()
    points=models.IntegerField(default=10)
    class Meta:
        ordering =['-current_day','quiz_endtime']
    def __str__(self):
        active = config.current_config(config)
        s= ""
        z= ""
        if self.quiz_endtime.replace(tzinfo=utc)< datetime.datetime.now().replace(tzinfo=utc):
            z = "-expired"
        if self== active:
            s = "-ONLINE"
            if z=="-expired":
                s="-Current Config"
        return "Day-{} {}{}".format(self.current_day,s,z)

    def current_config(self):

        configs= self.objects.all()
                                                                    # arr = [[config]*(no of instances of each day)]* no of days
        arr=[]
        arr = [0 for i in range(10)]                                #initialized 10 days with 0 instances of each
        cnt = 1
        for con in configs:
            curr_day = con.current_day
            arr[curr_day] += 1  
            cnt = max(curr_day, cnt)       
        list_of_configs = []        
        new = []
        for i in range(1,cnt+1):                                    #This is like a vector of vectors with ith day config in list[i] vector. So we basically choose 1 out of each day,
            for j in configs:
                curr_day = j.current_day
                if curr_day == i:
                    new.append(j)
            list_of_configs.append(new)
            new = []                

        maxi = timezone.now().replace(tzinfo=utc)
        choice = None
        if len(configs) == 0: 
            default_choice = None
        else: 
            default_choice = configs[0]
        for i in list_of_configs:
            
            maxi = timezone.now().replace(tzinfo=utc)
            for j in i:
                default_choice = j
                quiz_endtime = j.quiz_endtime.replace(tzinfo=utc)
                
                if maxi < quiz_endtime:                             #the config with the maximum endtime is chosen incase of a clash
                    choice = j
                    
                    maxi = quiz_endtime
            if choice is not None:                                  #IMP: if there is a valid config with a lower day it would be given higher priority
                break
        if choice is None:                                          #if there are no configs, the case is handled in quiz_active () function
            choice = default_choice
        curr_config=choice                  
        
        return curr_config

    def quiz_active(self):
        curr_config = self.current_config(self)                     #current valid config is found
        if curr_config is None:
            return False     
        print(curr_config.quiz_start)                                       
        current_time=timezone.now().replace(tzinfo=utc)    #No config in the DB     
        quiz_endtime=curr_config.quiz_endtime.replace(tzinfo=utc)
        quiz_srttime=curr_config.quiz_start.replace(tzinfo=utc)
        print(quiz_endtime)
        print(quiz_srttime)
        print(current_time)  
        if current_time >= quiz_endtime or current_time <= quiz_srttime :                               #if the valid config's time endtime is yet to come, then its an active quiz. The starttime value is 
            curr_config.quiz_active=False                           #compared in the frontend. 
            print(current_time>quiz_endtime)
            return False
        return True




