from django.http.request import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import Paginator
from django.http import HttpResponse
from result.models import Result
from account.models import User


def home(request):
    # User 생성
    new_user = User()
    new_user.save()
    print(new_user.id)

    return render(request, 'home.html', {'user_id': new_user.id})


# 새 질문 만들기
def question_create(request):
    if request.method == 'POST':
        new_question = Question()
        new_question.que = request.POST['que']
        new_question.answer1 = request.POST['answer1']
        new_question.answer2 = request.POST['answer2']
        new_question.page = request.POST['page']
        new_question.save()
        return redirect('home')
    else:
        return render(request, 'new.html')


def question_detail(request, id):
    question = get_object_or_404(Question, pk=id)
    return render(request, 'detail.html', {'question': question})


def question_edit(request, id):
    if request.method == "POST":
        edit_question = Question.objects.get(pk=id)
        edit_question.que = request.POST['que']
        edit_question.answer1 = request.POST['answer1']
        edit_question.answer2 = request.POST['answer2']
        # edit_question.page = request.POST['page']
        edit_question.save()
        return redirect('question_detail', edit_question.id)
    else:
        question = Question.objects.get(pk=id)
        return render(request, 'edit.html', {'question': question})


def question_delete(request, id):
    delete_question = Question.objects.get(pk=id)
    delete_question.delete()
    return redirect('home')


def choices(request, pk):
    # 객체 불러오기
    questions = Question.objects.all()
    paginator = Paginator(questions, 1)
    page_number = request.GET.get('page') or 1
    page = paginator.get_page(page_number)
    ## 점수계산
    # 유저 정보 가져오기
    user = User.objects.get(pk=pk)

    if int(page_number) <=4:
        selectionIE = request.POST['test2']
        user.result1 += int(selectionIE)
    elif int(page_number) <=7:
        selectionSN = request.POST['test2']
        user.result2 += int(selectionSN)
    elif int(page_number) <=10:
        selectionFT = request.POST['test2']
        user.result3 += int(selectionFT)
    else:
        selectionPJ = request.POST['test2']
        user.result4 += int(selectionPJ)
    user.save()
    ## 유형판단
    # 빈리스트 생성
    mbti = []
    # 유저 정보 가져오기
    user = User.objects.get(pk=pk)
    if user.result1 <=5:
        mbti.append("E")
    else :
        mbti.append("I")
    if user.result2 <=4:
        mbti.append("N")
    else :
        mbti.append("S")
    if user.result3 <=4:
        mbti.append("F")
    else :
        mbti.append("T")
    if user.result4 <=4:
        mbti.append("J")
    else :
        mbti.append("P")
    user.result = ''.join(mbti)
    user.save()
    print(user.result)
    if int(page_number) <= questions.count():
        return render(request, 'choices.html', {'questions': page, 'user_id': user.id})


def results(request, pk):
    user = User.objects.get(pk=pk)
    if user.result == 'ENFP':
        return render(request, 'result1.html', {'user': user})
    elif user.result == 'ENTP':
        return render(request, 'result2.html', {'user': user})
    elif user.result == 'ENTJ':
        return render(request, 'result3.html', {'user': user})
    elif user.result == 'ENFJ':
        return render(request, 'result4.html', {'user': user})
    elif user.result == 'ESFP':
        return render(request, 'result5.html', {'user': user})
    elif user.result == 'ESTP':
        return render(request, 'result6.html', {'user': user})
    elif user.result == 'ESTJ':
        return render(request, 'result7.html', {'user': user})
    elif user.result == 'ESFJ':
        return render(request, 'result8.html', {'user': user})
    elif user.result == 'INFP':
        return render(request, 'result9.html', {'user': user})
    elif user.result == 'INTP':
        return render(request, 'result10.html', {'user': user})
    elif user.result == 'INTJ':
        return render(request, 'result11.html', {'user': user})
    elif user.result == 'INFJ':
        return render(request, 'result12.html', {'user': user})
    elif user.result == 'ISFP':
        return render(request, 'result13.html', {'user': user})
    elif user.result == 'ISTP':
        return render(request, 'result14.html', {'user': user})
    elif user.result == 'ISTJ':
        return render(request, 'result15.html', {'user': user})
    elif user.result == 'ISFJ':
        return render(request, 'result16.html', {'user': user})