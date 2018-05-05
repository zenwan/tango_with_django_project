from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify
class Category(models.Model):
    # 定义Model字段
    name = models.CharField(max_length=128,unique=True) # 字符串类型
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(blank=False,unique=True) # 别名

    class Meta:
        verbose_name_plural = "Categories"
        #ordering=[]

    def save(self, *args,**kwargs):
        self.slug = slugify(self.name)
        super(Category,self).save(*args,**kwargs)

    def __str__(self):
        return self.name

class Page(models.Model):
    """
    Foreignkey : one to many
    """
    category = models.ForeignKey(Category,on_delete=models.CASCADE) # page 类别
    title = models.CharField(max_length=128,unique=True) # 标题
    url = models.URLField() # url
    views = models.IntegerField(default=0) # 浏览量

    def __str__(self):
        return self.title
