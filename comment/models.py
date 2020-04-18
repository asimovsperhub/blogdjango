from django.db import models

# Create your models here.

#评论模型
class Comment(models.Model):
    # name = models.CharField(max_length=100)
    # email = models.EmailField(max_length=200)
    # url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    # 外键，关联blog app下的Blog数据模型
    blog = models.ForeignKey('blog.Blog', on_delete=models.CASCADE, related_name='comment_blog')
    #
    count=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.text
