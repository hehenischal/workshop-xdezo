from django.shortcuts import render,redirect

from .models import Task

# Create your views here.



def index(request):
    tasks = Task.objects.all()
    return render(request, 'task/index.html',{'tasks':tasks})

def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        completed = True if request.POST.get('completed') == 'on' else False
        Task.objects.create(title=title,completed=completed)
        return redirect('home')
    return render(request, 'task/create.html')


def edit(request,id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.completed = True if request.POST.get('completed') == 'on' else False
        task.save()
        return redirect('home')
    return render(request, 'task/create.html',{'task':task})
    

def delete(request,id):
    Task.objects.get(id=id).delete()
    return redirect('home')

