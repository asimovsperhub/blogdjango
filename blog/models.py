from django.contrib.auth.models import User
from django.db import models


# Create your models here.

##后台添加博客数据模型

# 分类
from mdeditor.fields import MDTextField


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='分类')

    # 返回对象本身的字段，而不是QuerySet[]
    def __str__(self):
        return self.name

    class Meta:
        # db_table   指定数据表名称
        db_table = 'category'
        ##复数
        verbose_name = '分类'
        ##复数->单数
        verbose_name_plural = verbose_name


# 标签
class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='标签')
    # 文章id
    # blog_id=models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        # db_table   指定数据表名称
        db_table = 'tag'
        ##复数
        verbose_name = '添加标签'
        ##复数->单数
        verbose_name_plural = verbose_name

# 文章
class Blog(models.Model):
    # 标题
    title = models.CharField(max_length=100, verbose_name='博客标题')
    # 封面,upload_to图片上传后存储的目录，如果没有则会自动创建
    img = models.ImageField(upload_to='static/images/blog_img/', verbose_name='封面',blank=True)
    # 简介,允许为空
    excerpt = models.CharField(max_length=200, blank=True, verbose_name='博客简介')
    # 正文
    # body = models.TextField(verbose_name='正文')
    # 使用富文本编辑器的Textfield
    body=MDTextField()
    # 创建时间
    created_time = models.DateTimeField(verbose_name='创建时间')
    # 阅读量,只可以是正整数或0
    views = models.PositiveIntegerField(default=0, verbose_name='阅读量')
    # Category外键，级联删除,related_name：相当于
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='Category')
    # 一篇文章可以有多个标签，同一个标签下也可能有多篇文章，所以我们使用 ManyToManyField，表明这是多对多的关联关系
    tags = models.ManyToManyField(to=Tag,verbose_name='标签',related_name='Tag')
    # readcount=models.IntegerField(verbose_name='阅读量')
    # User外键，django后台user
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        # db_table   指定数据表名称
        db_table = 'blog'
        ##复数
        verbose_name = '添加博客'
        ##复数->单数
        verbose_name_plural = verbose_name

    # 按照自定义的格式输出内容
    def __str__(self):
        return self.title

    # 只要有访问（查询）到这篇文章，views自加一
    def views_count(self):
        self.views += 1
        return self.save(update_fields=['views'])
    # 在后台显示标签列表
    # def tag_list(self):
    #     return ','.join([i.name for i in self.tags.all()])
