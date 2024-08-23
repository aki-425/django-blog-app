from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.shortcuts import render,get_object_or_404,redirect
from django.http import Http404, HttpResponse
from django.db.models import Q
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


from django.views.generic import ListView,DetailView,CreateView,DeleteView
from blog.forms import CommentForm,ReplyForm
from .models import Post,Category,Tag,Comment,Reply



class PostListView(ListView):  # データベースの一覧を標示
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "post"
    paginate_by = 5
    
    #更新順に並び替える
    def get_queryset(self):
        posts = super().get_queryset()
        
        return  posts.order_by("-updated_at")


class PostDetailView(DetailView):#データベースの詳細を表示
    model = Post
    template_name = "blog/post_detail.html"
    paginate_by = 5
    
    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        #公開済み　or　ログインしている人だけ公開
        if post.is_published or self.request.user.is_authenticated:
                                    
            return post 
        else:
            raise Http404
        
class CategoryPostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "post"
    paginate_by = 5
    
    def get_queryset(self):
        slug = self.kwargs['slug']
        self.category = get_object_or_404(Category,slug =slug)
        
       
        return  super().get_queryset().filter(category = self.category)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       
        
        context["category"] = self.category
        return context
    
class TagPostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "post"
    paginate_by = 5
    
    def get_queryset(self):
        slug = self.kwargs['slug']
        self.tag = get_object_or_404(Tag,slug =slug)
        
       
        return  super().get_queryset().filter(tag = self.tag)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = self.tag
        return context
    
class SearchPostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "post"
    paginate_by = 5
    
    def get_queryset(self):
        self.query = self.request.GET.get('query') or ""
        
        queryset = super().get_queryset()
        if self.query:
            queryset = queryset.filter(Q(title__icontains=self.query) | Q(title__icontains=self.query))
        if not self.request.user.is_authenticated:
            queryset.filter(is_published=True)  
        self.post_count = len(queryset)
        
        
        return queryset 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.query
        context["post_count"] = self.post_count
        return context
    
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    
    def form_valid(self, form): 
        comment = form.save(False)
        post_pk = self.kwargs['post_pk']
     
        post = get_object_or_404(Post, pk=post_pk) 
        comment.post = post
        comment.save()
        return redirect('post-Detail',pk=post_pk)
    def get_context_data(self, **kwargs) :
        context =super().get_context_data(**kwargs)
        post_pk = self.kwargs["post_pk"]
        context["post"] = get_object_or_404(Post,pk=post_pk)
        return context 
    
class ReplyCreateView(CreateView):
    model = Reply
    form_class = ReplyForm
    template_name = "blog/comment_form.html"
    
    def form_valid(self, form): 
        reply = form.save(False)
        comment_pk = self.kwargs['comment_pk']
        comment = get_object_or_404(Comment,pk=comment_pk)
        
        reply.comment = comment
        reply.save()
        return redirect('post-Detail',pk=comment.post.pk)
    def get_context_data(self, **kwargs) :
        context =super().get_context_data(**kwargs)
        comment_pk = self.kwargs["comment_pk"]
        context["comment"] = get_object_or_404(Comment,pk=comment_pk)
        return context 
    
class CommentDeleteView(LoginRequiredMixin,DeleteView):
    model = Comment
    template_name = "blog/comment_delete.html"
    
    def get_success_url(self) -> str:
        return reverse("post-Detail", kwargs={"pk":self.object.post.pk})
                                
    
class ReplyDeleteView(LoginRequiredMixin,DeleteView):
    model = Reply
    template_name = "blog/comment_delete.html"
    
    def get_success_url(self):
        return reverse("post-Detail", kwargs={"pk":self.object.comment.post.pk})
                                
    
    
    
    


