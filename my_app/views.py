from django.shortcuts import render,redirect
from .forms import TaskForm
from.models import TaskModel
# Create your views here.
def task(request):
    if request.method=="POST":
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=TaskForm()
    return render (request,'task.html',{'form':form})

def home(request):
    data=TaskModel.objects.all()
    return render (request,'todo_list.html',{'data':data})

def Edit(request,id):
    data=TaskModel.objects.get(pk=id)
    if request.method=="POST":
        form=TaskForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=TaskForm(instance=data)
    return render(request,'edit_task.html',{'form':form})

def delete_todo(request,id):
    data=TaskModel.objects.get(pk=id)
    data.delete()
    return redirect('/')
    


