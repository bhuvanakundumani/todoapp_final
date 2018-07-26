from django.shortcuts import render,redirect,get_object_or_404
from .models import Category,Todolist
from .forms import TodoForm
from django.utils import timezone
import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

error='blah'
# Create your views here.

def list_todo(request):
    todolist=Todolist.objects.all()
    categories=Category.objects.all()
    return render(request,'todolist.html',{'todolist' : todolist})

def new_list(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        todo1=form.save(commit=False)
       # today_date = datetime.date.today()
        #print(today_date)
        #if todo1.due_date<today_date:
         #   raise forms.ValidationError(error)

        #print(todo1.due_date)
        todo1.save()
        #form.save()
        return redirect(list_todo)

    return render(request, 'todolist_new.html', {'form':form})

def edit_list(request,id):
    todo = get_object_or_404(Todolist, pk=id)
    form = TodoForm(request.POST or None, instance=todo)

    if form.is_valid():
        #print(todo.due_date)


        form.save()
        return redirect(list_todo)

    return render(request,'todolist_new.html',{'form':form})

def delete_list(request,id):

    todo=get_object_or_404(Todolist,pk=id)
    if request.method =='POST':
        todo.delete()
        return redirect(list_todo)

    return render(request,'confirm.html',{'todo':todo})