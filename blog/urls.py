from django.urls import path
from blog.views import (PostListView,CommentDeleteView,
                        ReplyDeleteView,
                       PostDetailView,CategoryPostListView,
                       TagPostListView,SearchPostListView,
                       CommentCreateView,ReplyCreateView)

urlpatterns = [path("", PostListView.as_view(), name='Post-List'),
               path("post/<int:pk>/",PostDetailView.as_view(), name='post-Detail'),
               path("category/<str:slug>", CategoryPostListView.as_view(),name='category-Post-List'),
               path("tag/<str:slug>", TagPostListView.as_view(),name='tag-Post-List'),
               path("search/",SearchPostListView.as_view(),name='search-Post-List'),
               path("comment/<int:post_pk>",CommentCreateView.as_view(),name='comment'),
               path("reply/<int:comment_pk>",ReplyCreateView.as_view(),name='reply'),
               path("comment/<int:pk>/delete/",CommentDeleteView.as_view(),name='comment-delete'),
               path("reply/<int:pk>/delete/",ReplyDeleteView.as_view(),name='reply-delete'),
               
]
               