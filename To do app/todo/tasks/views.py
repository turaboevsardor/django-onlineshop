from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *

from . forms import *
def index(request):
    tasks = Task.objects.all()
    form = TaskForm

    if request.method == 'Post':
        form = TaskForm(request.Post)
        if form.is_valid():
            form.save()
        return
    context = {'tasks':tasks,'form':form}
    return render(request,'tasks/list.html', context)

def upgdateTask(request,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'Post':
        form = TaskForm(request.Post,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

def deleteTask(request,pk):
    item = Task.objects.get(id=pk)
    if request.method == 'Post':
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request,'tasks/.html')

    context = {'form':form}
    return render(request,'tasks/upgdate_task.html')
