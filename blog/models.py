from django.db import models




class Category (models.Model):
    name =models.CharField("カテゴリー",max_length=255)
    slug = models.SlugField("URL",unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "カテゴリー"
    
class Tag (models.Model):
    name =models.CharField("タグ",max_length=255)
    slug = models.SlugField("URL",unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "タグ"
    
class Post (models.Model):
    title = models.CharField("タイトル", max_length=200)
    description = models.TextField("本文", blank=True)
    image = models.ImageField('画像',upload_to='upload/',null=True,blank=True)
    created_at = models.DateField( "作成日", auto_now_add=True)
    updated_at = models.DateField( "更新日",auto_now=True)
    is_published = models.BooleanField("公開設定",default=False)
    
    
    category = models.ForeignKey(Category,verbose_name="カテゴリー",on_delete=models.PROTECT,null=True,blank=True)    
    tag = models.ManyToManyField(Tag,verbose_name="タグ",blank=True)
    def __str__(self):
            return self.title
        
    class Meta:
        verbose_name_plural = "ポスト"
        
class Comment(models.Model):
    name = models.CharField("名前",max_length=100)
    text = models.TextField("本文")
    created_at = models.DateField( "作成日", auto_now_add=True)
    post = models.ForeignKey(Post,verbose_name="記事",on_delete=models.CASCADE)    
   
    def __str__(self):
        return self.text[:10]
    class Meta:
        verbose_name_plural = "記事"
        
class Reply(models.Model):
    name = models.CharField("名前",max_length=100)
    text = models.TextField("本文")
    created_at = models.DateField( "作成日", auto_now_add=True)
    comment = models.ForeignKey(Comment,verbose_name="返信",on_delete=models.CASCADE)    
   
    def __str__(self):
        return self.text[:10]
    class Meta:
        verbose_name_plural = "コメント"
