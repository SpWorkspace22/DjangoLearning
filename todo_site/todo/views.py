from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Todo
from .forms import TodoForm
# Create your views here.


def index(request):
    list_item = Todo.objects.order_by("-date")

    if request.method=='POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()

    page = {
        "forms":form,
        "list":list_item,
        "title":"TODO LIST" 
    }

    return render(request,'index.html',page)


def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')
