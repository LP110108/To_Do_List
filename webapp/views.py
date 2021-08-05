from django.shortcuts import render, get_object_or_404, redirect, reverse
from webapp.models import Task, Status, Type
from webapp.forms import TaskForm
from django.views.generic import TemplateView, View, ListView, CreateView


class ToDoView(ListView):
    context_object_name = 'task'
    template_name = 'to-do_view.html'

    def get_queryset(self):
        return Task.objects.all()


class TaskView(TemplateView):
    template_name = 'task_view.html'

    def get_context_data(self, **kwargs):
        kwargs['task'] = get_object_or_404(Task, pk=kwargs['task_pk'])
        return super().get_context_data(**kwargs)


class ToDoCreate(CreateView):
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, 'to-do_create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(
                summary=form.cleaned_data['summary'],
                description=form.cleaned_data['description']
            )
            return redirect('view')
        else:
            return render(request, 'to-do_create.html', context={'form': form})


class TaskDeleteView(View):
    def get(self, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        task.delete()
        return redirect('main')


class TaskUpdate(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        form = TaskForm(data={
            'summary': task.summary,
            'description': task.description,
        })
        return render(request, 'to-do_update.html', context={'form': form, 'article': task})

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.summary = form.cleaned_data['summary']
            task.description = form.cleaned_data['description']
            task.save()
            return redirect('view')
        else:
            return render(request, 'to-do_update.html', context={'form': form, 'article': task})


def main(request):
    return render(request, 'index.html')
