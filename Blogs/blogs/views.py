from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost, Comment
from .forms import BlogPostForm, CommentForm

def index(request):
    """The home page for Blog."""
    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)

def post_detail(request, post_id):
    """Show a single post and its comments."""
    post = get_object_or_404(BlogPost, id=post_id)
    comments = post.comments.order_by('date_added')
    
    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return redirect('blogs:post_detail', post_id=post_id)
    else:
        form = CommentForm()

    context = {'post': post, 'comments': comments, 'form': form}
    return render(request, 'blogs/post_detail.html', context)

@login_required
def new_post(request):
    """Add a new post."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BlogPostForm()
    else:
        # POST data submitted; process data.
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:index')

    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
    """Edit an existing post."""
    post = get_object_or_404(BlogPost, id=post_id)
    
    # Make sure the post belongs to the current user.
    if post.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = BlogPostForm(instance=post)
    else:
        # POST data submitted; process data.
        form = BlogPostForm(instance=post, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blogs:post_detail', post_id=post.id)

    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)

@login_required
def delete_post(request, post_id):
    """Delete an existing post."""
    post = get_object_or_404(BlogPost, id=post_id)
    
    # 允许帖子作者 或者 超级管理员 删除帖子
    if post.owner != request.user and not request.user.is_superuser:
        raise Http404
    
    if request.method == 'POST':
        post.delete()
        return redirect('blogs:index')
        
    context = {'post': post}
    return render(request, 'blogs/delete_post.html', context)

@login_required
def delete_comment(request, comment_id):
    """Delete an existing comment."""
    comment = get_object_or_404(Comment, id=comment_id)
    
    # 允许评论作者 或者 超级管理员 删除评论
    if comment.author != request.user and not request.user.is_superuser:
        raise Http404
        
    post_id = comment.post.id
    # 为了简化，这里直接执行删除
    comment.delete()
    return redirect('blogs:post_detail', post_id=post_id)

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            login(request, new_user)
            return redirect('blogs:index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)

