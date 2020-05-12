from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Myusers, Movies, Series, Books
from django.contrib.auth.models import User

from django.http import HttpResponse


def login(request):
    if request.user.is_authenticated:
        player = request.user
        try:
            crap = Myusers.objects.get(email=player.email)
            if crap.choice is None:
                firsttime = 1
        #        return HttpResponse("No choices filled!")
            else :
                firsttime = 0
        except Myusers.DoesNotExist:
            user = Myusers()
            user.name = player.username
            user.email = player.email
            user.save()
            firsttime = 1

        crap = Myusers.objects.get(email=player.email)

        pk = crap.pointsfactor
        pk = pk+1
        pk = str(pk)

        if firsttime == 0:
            if crap.choice == "Movies":
               # question = get_object_or_404( Movies, pk = pk)
                return questionmovies(request)
                
               # return render(request, 'questions.html',{'question':question, 'pk':pk})

            elif crap.choice == "Series":
                return questionseries(request)

            elif crap.choice == "Books":
                return questionbooks(request)


                
            else:
                return HttpResponse("You shouldn't be here. This error should have never happened. Just like you. Report the moderator immediately//kkc")


        return choose(request)
    else:
        return render(request, 'index.html')

@login_required
#This function is messed up. Needs to be fixed asap.//kkc//fixed//kkc
def choose(request):
    
    player = request.user
    name = player.username
    case = 0
    prk = 1
    try:
        

        crap = Myusers.objects.get(email=player.email)
        
        if crap.choice == "Movies":

               # question = get_object_or_404( Movies, pk = pk)
            return questionmovies(request)
               # return render(request, 'questions.html',{'question':question, 'pk':pk})

        elif crap.choice == "Series":
            return questionseries(request)

        elif crap.choice == "Books":
            return questionbooks(request)

    
                
        

        if crap.choice is None:

            case = 0
    #        return HttpResponse("correct ans!")
        else:
            return HttpResponse("You shouldn't be here. This error should have never happened. Just like you. Report the moderator immediately")



    except Myusers.DoesNotExist:
        user = Myusers()
        string = player.first_name + " " + player.last_name
        user.name = string
        user.email = player.email
        user.save()
        
        case = 0
        


    
    if case is 0:
        firsttime = 1
        return render(request, 'choose.html', {'name':name, 'firsttime':firsttime, 'pk':prk})

    firsttime = 0

 #   name = crap.choice
    

    return render(request, 'choose.html', {'name':name, 'firsttime':firsttime, 'pk':prk})


@login_required
def questionmovies(request):

    
    user = request.user
    player = Myusers.objects.get(email=user.email)
    if player.choice is None:
        player.choice = "Movies"
        player.save()
    #    return HttpResponse("lol saved as movies!")
    elif player.choice == "Movies":
        pass
    else:
        return HttpResponse("Fuck OFF. You shouldn't be here.")


    qno = player.pointsfactor
    qno = qno+1
    

    #lastobjectornot
    shit = qno -1
    questionsdec= Movies.objects.order_by('-order')
    questionno = questionsdec.first()
    if questionno.order == shit :
        return end(request)
        #return HttpResponse("More questions coming soon!")
    sc = qno
    qno = str(qno)      #converting back to string since the pk must be string
    question = get_object_or_404( Movies, order = qno)
    
    decision = 0

    if request.method == 'POST':
        
        
        answer = request.POST.get('Answer')
        
        decision = question.check_ans(answer, question)
        if (decision == 1):
            
            player.pointsfactor= player.pointsfactor+1
            player.save()
            qno = player.pointsfactor
            qno = qno+1



            #lastobjectornot
            questionsdec= Movies.objects.order_by('-order')
            questionno = questionsdec.first()
            shit = qno -1
            if questionno.order == shit :
                return end(request)
                #return HttpResponse("Confratulations. Now, wait. More questions coming your way!")

            sc = qno
            qno = str(qno)
            
        #    pk = int(pk)
        #    pk = pk+1
        #    pk = str(pk)
            questionnext = get_object_or_404( Movies, order = qno)
       #     return HttpResponse("correct ans!")
            return render(request,'questions.html',{'question':questionnext, 'pk':qno, 'score':(sc-1)*10})

        else :
            decision = -9             
            return render(request, 'questions.html',{'question':question, 'pk':qno, 'score':(sc-1)*10, 'cr':decision})
    
    else:
        return render(request, 'questions.html',{'question':question, 'pk':qno, 'score':(sc-1)*10, 'cr':decision})
     
    



    
    return render(request, 'questions.html',{'question':question, 'pk':qno, 'score':(sc-1)*10, 'cr':decision})

@login_required
def questionseries(request):

    
    user = request.user
    player = Myusers.objects.get(email=user.email)

    if player.choice is None:
        player.choice = "Series"
        player.save()
    #    return HttpResponse("lol saved as movies!")
    elif player.choice == "Series":
        pass
    else:
        return HttpResponse("Fuck OFF. You shouldn't be here.")

    qno = player.pointsfactor
    qno = qno+1

    #lastobjectornot
    shit = qno -1
    questionsdec= Series.objects.order_by('-order')
    questionno = questionsdec.first()
    if questionno.order == shit :
        return end(request)
        #return HttpResponse("Confratulations. Now, wait. More questions coming your way!")

    sc = qno
    qno = str(qno)

    question = get_object_or_404( Series, order = qno)
    decision = 0


    if request.method == 'POST':
        
        
        answer = request.POST.get('Answer')
        decision = question.check_ans(answer, question)
        if (decision == 1):
            
            player.pointsfactor= player.pointsfactor+1
            player.save()
            qno = player.pointsfactor
            qno = qno+1

            #lastobjectornot
            questionsdec= Series.objects.order_by('-order')
            questionno = questionsdec.first()
            shit = qno -1
            if questionno.order == shit :
                return end(request)
                #return HttpResponse("Confratulations. Now, wait. More questions coming your way!")
            sc = qno
            qno = str(qno)
            
        #    pk = int(pk)
        #    pk = pk+1
        #    pk = str(pk)
            questionnext = get_object_or_404( Series, order = qno)
       #     return HttpResponse("correct ans!")
            return render(request,'questions.html',{'question':questionnext, 'pk':qno, 'score':(sc-1)*10})#pk important to determine the question no element in the page of question

        else :
            decision = -9              
            return render(request, 'questions.html',{'question':question, 'pk':qno, 'score':(sc-1)*10, 'cr':decision})
    
    if request.method == 'GET':
        

        
        
       
        return render(request, 'questions.html',{'question':question, 'pk':qno, 'score':(sc-1)*10, 'cr':decision})
     
    decision = 0



    
    return render(request, 'questions.html',{'question':question, 'pk':qno, 'score':(sc-1)*10, 'cr':decision})


@login_required
def questionbooks(request):

    
    user = request.user
    player = Myusers.objects.get(email=user.email)

    if player.choice is None:
        player.choice = "Books"
        player.save()
    #    return HttpResponse("lol saved as movies!")
    elif player.choice == "Books":
        pass
    else:
        return HttpResponse("Fuck OFF. You shouldn't be here.")

    qno = player.pointsfactor
    qno = qno+1
    

    #lastobjectornot
    questionsdec= Books.objects.order_by('-order')
    questionno = questionsdec.first()
    shit = qno -1
    if questionno.order == shit :
        return end(request)
        #return HttpResponse("Confratulations. Now, wait. More questions coming your way!")
    sc = qno
    qno = str(qno)      #converting back to string since the pk must be string
    question = get_object_or_404( Books, order = qno)
    

    decision = 0
    if request.method == 'POST':
        
        
        answer = request.POST.get('Answer')
        decision = question.check_ans(answer, question)
        if (decision == 1):
            
            player.pointsfactor= player.pointsfactor+1
            player.save()
            qno = player.pointsfactor
            qno = qno+1



            #lastobjectornot
            shit = qno -1
            questionsdec= Books.objects.order_by('-order')
            questionno = questionsdec.first()
            if questionno.order == shit :
                return end(request)
                #return HttpResponse("Confratulations. Now, wait. More questions coming your way!")
                

            sc = qno
            qno = str(qno)
            
        #    pk = int(pk)
        #    pk = pk+1
        #    pk = str(pk)
            questionnext = get_object_or_404( Books, order = qno)
       #     return HttpResponse("correct ans!")
            return render(request,'questions.html',{'question':questionnext, 'pk':qno, 'score':(sc-1)*10})

        else :
            decision = -9              
            return render(request, 'questions.html',{'question':question, 'pk':qno, 'score':(sc-1)*10, 'cr':decision})
    
    else:
        
        return render(request, 'questions.html',{'question':question, 'pk':qno, 'score':(sc-1)*10, 'cr':decision})
     
    



    
    return render(request, 'questions.html',{'question':question, 'pk':qno, 'score':(sc-1)*10, 'cr':decision})


def leaderboard(request):
    users = Myusers.ranks(Myusers)
    if request.user.is_authenticated:
        player = request.user
        name = player.first_name + " " + player.last_name
        return render(request, 'leaderboard.html', {'users':users, 'nam':name})
    else:
        return render(request, 'leaderboard.html', {'users':users})

        
#rajkumar
@login_required
def end(request):
    return render(request, 'end.html')
