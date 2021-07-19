from django.shortcuts import redirect, render, get_object_or_404
from .models import *

# Create your views here.
def detail(request, id):
    result = get_object_or_404(Result, pk = id)
    return render(request, 'detail.html', {'result':result})

def make_post(request):
    if request.method == "POST":
        new_result = Result()
        new_result.image = request.FILES['image']
        new_result.body = request.POST['body']
        new_result.save()
        return redirect('home')
    else:
        return render(request, 'new.html')

def update(request, id):
    if request.method == 'POST':
        update_result = Result.objects.get(id=id)
        update_result.image = request.FILES['image']
        update_result.body = request.POST['body']
        update_result.save()
        return redirect('detail', update_result.id)
    else:
        result = Result.objects.get(id=id)
        return render(request, 'edit.html', {'result':result})

def delete(request, id):
    delete_result = Result.objects.get(id = id)
    delete_result.delete()
    return redirect('home')