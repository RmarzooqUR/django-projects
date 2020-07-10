from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Boards, Topics, User
from .forms import newTopicForm, newPostForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return HttpResponse(
        'Hello world, you are at home. Go to <ul>'+
        '<li><a href="/boards">Boards</a></li>'+
        '<li><a href="/accounts">Accounts</li>'+
        '</ul>'
    )

def boardsHome(request):
    boards = Boards.objects.all()
    return render(request, template_name='boards/boards.html', context={'boards' : boards})

def boardTopics(request, pk):
    try:
        board = Boards.objects.get(pk=pk)
    except Boards.DoesNotExist:
        raise Http404
    return render(request, template_name='boards/board.html', context={'board':board})


@login_required(redirect_field_name='login')
def newTopic(request, pk):
    board = get_object_or_404(Boards, pk=pk)
    user = User.objects.first()
    if request.method == 'POST':
        form = newTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            return redirect('boardTopics', pk=board.pk)
    else:
        form = newTopicForm()

    return render(request, template_name='boards/newTopic.html', context={'board':board, 'form':form})

def postsFeed(request, pk,pk2):
    board = get_object_or_404(Boards, pk=pk)
    topic = get_object_or_404(Topics, pk=pk2)
    return render(
        request,
        template_name='boards/postFeed.html',
        context={'topic':topic, 'board':board}
    )

@login_required(redirect_field_name='login')
def newPost(request, pk, pk2):
    board = Boards.objects.get(pk=pk)
    topic = Topics.objects.get(pk=pk2)
    user = User.objects.first()
    if request.method=='POST':
        form = newPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = user
            post.topic = topic
            post.save()
            return redirect('boardTopics', pk=board.pk)
    else:
        form = newPostForm()
    return render(request, 'boards/newPost.html', context={'form':form, 'board':board, 'topic':topic})