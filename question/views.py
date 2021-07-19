from django.shortcuts import render, get_object_or_404, redirect
from .models import *


def home(request):
    questions = Question.objects.all()
    return render(request, 'home.html', {'questions': questions})


# 새 질문 만들기
def make_question(request):
    if request.method == 'POST':
        new_question = Question()
        new_question.que = request.POST['que']
        new_question.answer1 = request.POST['answer1']
        new_question.answer2 = request.POST['answer1']
        new_question.page = request.POST['page']
        new_question.save()
        return redirect('home')
    else:
        return render(request, 'new.html')


def detail(request, id):
    question = get_object_or_404(Question, pk=id)
    return render(request, 'detail.html', {'question': question})


def edit(request, id):
    if request.method == "POST":
        edit_question = Question.objects.get(pk=id)
        edit_question.que = request.POST['que']
        edit_question.answer1 = request.POST['answer1']
        edit_question.answer2 = request.POST['answer2']
        # edit_question.page = request.POST['page']
        edit_question.save()
        return redirect('detail', edit_question.id)
    else:
        question = Question.objects.get(pk=id)
        return render(request, 'edit.html', {'question': question})


def delete(request, id):
    delete_question = Question.objects.get(pk=id)
    delete_question.delete()
    return redirect('home')