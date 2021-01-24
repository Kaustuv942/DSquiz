from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Myusers, config, question
from django.contrib.auth.models import User
from django.http import HttpResponse

def login(request):
    if request.user.is_authenticated:
        player = request.user
        try:
            player = Myusers.objects.get(email=player.email)
        except Myusers.DoesNotExist:
            user = Myusers()
            user.name = player.first_name + " " + player.last_name
            user.email = player.email
            user.save()

        player = Myusers.objects.get(email=player.email)

        return timer(request)
    else:
        return render(request, 'index.html')

@login_required
def timer(request):
    active = config.current_config(config)
    if active is None:
        return end(request)
    starttime = active.quiz_start   
    running = config.quiz_active(config)
    if running is True:
        return Question(request)
    return render(request, 'timer.html', {'starttime':starttime})

@login_required
def Question(request):
    user = request.user
    player = Myusers.objects.get(email = user.email)
    active = config.current_config(config)
    if config.quiz_active(config) is False:
        return timer(request)
    # if player.day < active.current_day:
    #     player.day = active.current_day
    #     player.qno = 1
    #     player.save()
    if player.qno > active.q_no:
        return end(request)
    try:
        Thisquestion = question.objects.get(order = player.qno, day = player.day)
    except question.DoesNotExist:
        return end(request)
    qno = player.qno
    if request.method == 'POST':
        answer = request.POST.get('Answer')
        decision = question.check_ans(question, answer, Thisquestion)
        print(decision)
        if decision == True:
            player.score +=active.points
            player.qno += 1

            player.save()
            if player.qno > active.q_no:
                return end(request)
            
            


            return Question(request)  
        else:
            return render(request, 'questions.html',{'question':Thisquestion, 'pk':qno, 'score':player.score, 'cr':-9}) 
    else:
        return render(request, 'questions.html',{'question':Thisquestion, 'pk':qno, 'score':player.score, 'cr':0})
    
def leaderboard(request):
    users = Myusers.ranks(Myusers)
    if request.user.is_authenticated:
        player = request.user
        name = player.email
        return render(request, 'leaderboard.html', {'users':users, 'nam':name})
    else:
        return render(request, 'leaderboard.html', {'users':users})

@login_required
def end(request):
    return render(request, 'end.html')
