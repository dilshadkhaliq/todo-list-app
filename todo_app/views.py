from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import TodoForm

def index(request):
	todo = Todo.objects.order_by('id')
	form=TodoForm()
	context = {'todo':todo,'form':form}
	return render(request,'todo_app/index.html',context)


@require_POST
def addTodo(request):
	form = TodoForm(request.POST)
	if form.is_valid():
		new_todo = Todo(text=request.POST['text'])
		new_todo.save()
	return redirect('index')

def todocomplete(request,todo_id):
	todo = Todo.objects.get(pk=todo_id)
	todo.complete = True
	todo.save()

	return redirect('index')

def deleteAll(request):
	Todo.objects.all().delete()
	return redirect('index')

def deleteComplete(request):
	Todo.objects.filter(complete=True).delete()
	return redirect('index')


