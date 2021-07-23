from django.http.request import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import Paginator
from django.http import HttpResponse
from result.models import Result
from account.models import User


def home(request):
    questions = Question.objects.all()
    paginator = Paginator(questions, 1)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    user_id = request.user.id
    user = User.objects.get(id=user_id)
    return render(request, 'home.html', {'questions': page})


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
    choice = Result.objects.get(pk=pk)
    selection = request.POST['btn']
    # print(f'selection: {selection}')
    choice.result += int(selection)
    choice.save()

    return redirect('home')