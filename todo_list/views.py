from django.shortcuts import render
from .models import Task
# Create your views here.

def create_task(request):
  if request.method=='POST':
    title=request.POST.get('title')
    description=request.POST.get('description')
    priority=request.POST.get('priority')

    Task.objects.create(
      title=title,
      description=description,
      priority=priority
    )
    return redirect('create_task')
  return render(request, 'index.html')