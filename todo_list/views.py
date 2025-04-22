from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.http import HttpResponse,HttpRequest
from .models import Todo
from .forms import AddNewTodo
# Create your views here.

def created_todo(request):
    if request.method == "POST":
        form = AddNewTodo(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'form was successfully created')
            return redirect('home')
    else:
        form = AddNewTodo()
    context = {
        'create_todo':form
    }
    return render(request,'todo_form.html',context)

def edit_todo(request, todo):
    get_todo = get_object_or_404(Todo,id=todo)
    editform = AddNewTodo(request.POST or None, instance=get_todo)
    if request.method == "POST":
        if editform.is_valid():
            editform.save()
            messages.success(request,f'{get_todo.title} was successfully edited')
            return redirect('home')
    
    context = {
        'edit_todo':editform
    }
    return render(request,'edit_todo.html',context)

def delete_todo(request,delete):
    get_todo = get_object_or_404(Todo,id=delete)
    tag = f"Are you sure you want to delete this entry for {get_todo.title} ?"
    # deleteform = AddNewTodo(request.POST or None, instance=get_todo)
    if request.method =="POST":
            get_todo.delete()
            messages.success(request,f'{get_todo.title} has successfully being deleted')
            return redirect('home')
    cont ={
        'tag':tag
    }
    return render(request,'delete_todo.html',cont)


def mark_done(request,done):
    get_done = get_object_or_404(Todo,id=done)
    get_done.done = not get_done.done
    get_done.save()
    return redirect('home')
    
def home(request):
    todo_list = Todo.objects.all()
    context={
        'list': todo_list
    }
    return render(request,"index.html", context)