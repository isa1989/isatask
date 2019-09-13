from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from .forms import TaskForm, CommentForm
from .models import Task, Comment
from django.contrib.auth.decorators import login_required
from django.http import Http404
import datetime



# Create your views here.

def create(request):
    create_form = TaskForm()
    if request.method == 'POST':
        create_form = TaskForm(request.POST)
        if create_form.is_valid():
            created_form = create_form.save(commit=True)
            return HttpResponseRedirect(reverse('app:detail', kwargs={'pk':created_form.id}))
    return render(request,'post_create.html', context={'form':create_form})




@login_required(login_url='/users/login/')
def list(request):
    list = Task.objects.filter(user=request.user)
    post = Task.objects.all()

    return render(request, 'list.html', context={'list':list,'post':post})



@login_required(login_url='/users/login/')
def detail(request, pk):
    post = get_object_or_404(Task, pk=pk)
    list = Task.objects.filter(user=request.user)
    listt = Task.objects.all()
    if request.user == post.user:
        form = Task.objects.get(pk=pk)

    try:
        request.user == post.other_user
        form = Task.objects.get(pk=pk)

    except ObjectDoesNotExist:
        raise Http404



    comment_form = CommentForm(request.POST or None)

    if comment_form.is_valid():
        comment_form
        comment = comment_form.save(commit=False)
        comment.comm = form
        comment.user = request.user
        comment.save()
        comment_form = CommentForm()
    return render(request, 'post_detail.html', context={'post':post, 'form':form, 'list':list, 'listt':listt, 'comment_form':comment_form,})

@login_required(login_url='/users/login/')
def update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(data=request.POST or None, instance=task)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=True)
        return HttpResponseRedirect(reverse('app:detail', kwargs={'pk':form.instance.id}))
    return render(request,'post_update.html',context={'form':form})


@login_required(login_url='/users/login/')
def delete(request, pk):
    post = get_object_or_404(Task, pk=pk)
    if not request.user == post.user:
        return HttpResponse('sehife tapilmadi')
    post.delete()
    return HttpResponseRedirect(reverse('app:list'))

@login_required(login_url='/users/login/')


def comment_delete(request, pk):
    post = get_object_or_404(Comment, pk=pk)

    request.user == post.user

    post.delete()
    return HttpResponseRedirect(reverse('app:list'))


@login_required(login_url='/users/login/')
def comment_update(request, pk):
    task = get_object_or_404(Comment, pk=pk)
    form = CommentForm(data=request.POST or None, instance=task)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=True)
        return HttpResponseRedirect(reverse('app:detail', kwargs={'pk':form.instance.id}))
    return render(request,'comment_update.html',context={'form':form})


