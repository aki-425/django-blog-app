from django.contrib import admin

# Register your models here.
from blog.models import Post,Category,Tag,Comment,Reply

class ReplyInline(admin.StackedInline):
    model = Reply
    
class CommentAdmin(admin.ModelAdmin):
    inlines = [ReplyInline]


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','category','created_at','updated_at','is_published')
    search_fields = ('title','content')
    list_filter = ("category",)
    

    

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Reply)
