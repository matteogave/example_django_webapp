from django.shortcuts import render, redirect
from django.http import HttpResponse
from app_1.models import TaskList
from app_1.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required #solo se loggato esegue questa views
def section_task(request):

    if request.method=="POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manage = request.user
            instance.save()
        messages.success(request,("New task is added successfully"))
        return redirect(section_task)

    else:
        all_task = TaskList.objects.filter(manage=request.user)
        paginator = Paginator(all_task,4) #numero risultati da visualizzare per ogni pagina
        page = request.GET.get('pg')
        all_task = paginator.get_page(page)

        context = {
                'section_text': 'Section task page',
                'all_task': all_task
        }
        return render(request, 'section_task.html', context)

@login_required
def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.delete()
    else:
        messages.error(request,("Access restricted, You're not allowed!"))

    return redirect(section_task)

@login_required
def edit_task(request, task_id):
    if request.method=="POST":

        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
        messages.success(request,("Task is edited successfully"))
        return redirect(section_task)
    else:
        task_obj_ref = TaskList.objects.get(pk=task_id)
        context = {
                'edit_text': 'Edit task page',
                'task_obj': task_obj_ref
        }
        return render(request, 'edit_task.html', context)

@login_required
def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done=True
        task.save()
    else:
        messages.error(request,("Access restricted, You're not allowed!"))

    return redirect(section_task)

@login_required
def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done=False
    task.save()
    return redirect(section_task)

def index(request):
    context = {
            'index_text': 'Welcome homepage'
    }
    #return HttpResponse('Welcome to the first task..Hello world')
    return render(request, 'index.html', context)

def contact(request):
    context = {
            'contact_text': 'Contact page'
    }
    #return HttpResponse('Welcome to the first task..Hello world')
    return render(request, 'contact.html', context)

def about(request):
    context = {
            'about_text': 'About page'
    }
    #return HttpResponse('Welcome to the first task..Hello world')
    return render(request, 'about.html', context)
