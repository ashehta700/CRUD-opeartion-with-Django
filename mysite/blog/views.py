from django.shortcuts import render,get_object_or_404 , redirect
from django.http import HttpResponse
from blog.models import Post
from blog.forms import postform
from django.utils import timezone

# Create your views here.



def index(request):
    text =Post.objects.all()
    return render(request , 'blog/index.html' , {"text":text})


def post_detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    return render(request,'blog/post_detail.html',{"post":post})


#new post with form
def post_new(request):
    if request.method == "POST":
        form =postform(request.POST)
        if form.is_valid():
            form.cleaned_data['author']=request.user
            Post.objects.create(**form.cleaned_data)
    else:
        form=postform()
    
    return render(request,'blog/post_edit.html' ,{"form":form})        


#model form for create

def post_edit(request,pk):
    if request.method == "POST":
        form =postform(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.published_date=timezone.now()
            post.save()
            return redirect('index')
    else:
        form=postform()
    
    return render(request,'blog/post_edit.html' ,{"form":form})        



#model form for edit post
def post_new(request):
    if request.method == "POST":
        form =postform(request.POST,instance=post)    
        if request.method == "POST":
            post=form.save(commit=False)
            post.author=request.user
            post.published_date=timezone.now()
            post.save()     
            return redirect('post_detail',pk=post.pk)
        else:
            form=postform(instance=post)
    return render(request,'blog/post_edit.html' ,{"form":form}) 