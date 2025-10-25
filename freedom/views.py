#from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import FreedomPostForm
from .models import FreedomPost
from django.contrib import messages

def home(request):
    return render(request, 'freedom/home.html')

@login_required
def submit_freedom_post(request):
    if request.method == 'POST':
        form = FreedomPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Your opinion has been submitted successfully!')
            return redirect('freedom:my_freedom_post')
    else:
        form = FreedomPostForm()
    return render(request, 'freedom/submit_post.html', {'form': form})


@login_required
def my_freedom_posts(request):
    posts = FreedomPost.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'freedom/my_posts.html', {'posts': posts})


@login_required
def all_freedom_posts(request):
    category = request.GET.get('category')
    if category:
        posts = FreedomPost.objects.filter(category=category).order_by('-created_at')
    else:
        posts = FreedomPost.objects.all().order_by('-created_at')
    categories = ['Corruption', 'Court Delay', 'Police Injustice', 'Social Issue', 'Other']
    return render(request, 'freedom/all_posts.html', {'posts': posts, 'categories': categories, 'selected_category': category})



@login_required
def admin_freedom_posts(request):
    if not request.user.is_superuser:
        return redirect('index')
    posts = FreedomPost.objects.all().order_by('-created_at')
    return render(request, 'freedom/admin_posts.html', {'posts': posts})

@login_required
def delete_post(request, pk):
    post = get_object_or_404(FreedomPost, pk=pk)
    if post.user == request.user or request.user.is_superuser:
        post.delete()
        messages.success(request, "Post deleted successfully.")
    else:
        messages.error(request, "You are not authorized to delete this post.")
    return redirect('freedom:my_freedom_posts')

@login_required
def upvote_post(request, pk):
    post = get_object_or_404(FreedomPost, pk=pk)
    post.support += 1
    post.save()
    messages.success(request, "You supported this post.")
    return redirect('freedom:all_freedom_posts')

