from django.shortcuts import render
from django.http import Http404
from .models import Post
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.published.all()
    return render(request,
        'blog/list.html',
        {'posts': posts})


# def post_detail(request, id):
#      post = get_object_or_404(Post,
#         id=id,
#         status=Post.Status.PUBLISHED)
#      try:
#           post = Post.published.get(id=id)
#      except Post.DoesNotExist:
#           raise Http404("No Post found.")
 

#      return render(request,
#         'blog/detail.html',
#         {'post': post})

# def post_detail(request, year, month, day, post):
#     post = get_object_or_404(Post,
#     status=Post.Status.PUBLISHED,
#     slug=post,
#     publish__year=year,
#     publish__month=month,
#     publish__day=day)
#     return render(request,'blog/post/detail.html',{'post': post})


class Post(models.Model):
 def get_absolute_url(self):
    return reverse('blog:post_detail',
                   args=[self.publish.year,
                    self.publish.month,
                    self.publish.day,
                    self.slug])

 
 


 
def post_list(request):
    posts = Post.published.all()
    context = {
        'posts':posts
    }
    return render(request, 'blog/list.html',context)