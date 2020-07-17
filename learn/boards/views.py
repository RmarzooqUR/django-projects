from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Boards, Topics, User, Post
from .forms import newTopicForm, newPostForm
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.utils import timezone
from django.utils.decorators import method_decorator
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


@login_required
def newTopic(request, pk):
    board = get_object_or_404(Boards, pk=pk)
    # user = User.objects.first()
    if request.method == 'POST':
        form = newTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = request.user
            topic.save()
            return redirect('boardTopics', pk=board.pk)
    else:
        form = newTopicForm()

    return render(request, template_name='boards/newTopic.html', context={'board':board, 'form':form})

def postsFeed(request, pk,pk2):
    board = get_object_or_404(Boards, pk=pk)
    topic = get_object_or_404(Topics, pk=pk2)
    topic.viewCount += 1
    topic.save()
    return render(
        request,
        template_name='boards/postFeed.html',
        context={'topic':topic, 'board':board}
    )

@login_required
def newPost(request, pk, pk2):
    board = Boards.objects.get(pk=pk)
    topic = Topics.objects.get(pk=pk2)
    # user = User.objects.first()
    if request.method == 'POST':
        form = newPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            post.topic = topic
            post.save()
            return redirect('postsList', pk=board.pk, pk2=topic.pk)
    else:
        form = newPostForm()
    return render(request, 'boards/newPost.html', context={'form':form, 'board':board, 'topic':topic})


@method_decorator(login_required, name='dispatch')
class EditPostView(UpdateView):
    model = Post
    fields=('msg','description')
    template_name = 'boards/update_post.html'
    pk_url_kwarg = 'post_pk'
    context_object_name = 'post'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(created_by=self.request.user)

    def form_valid(self, form):
        post = form.save(commit=False)
        post.updated_by = self.request.user
        post.updated_at = timezone.now()
        post.save()
        return redirect('postsList', pk=post.topic.board.pk, pk2=post.topic.pk)
