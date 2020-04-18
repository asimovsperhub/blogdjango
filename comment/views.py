from django.shortcuts import render, redirect

# Create your views here.
from blog.models import Blog
from comment.models import Comment


def comment(request, **kwargs):
    # 通过id查找
    id = kwargs['id']
    blog_ = Blog.objects.filter(id=id).first()
    #
    if request.method == 'POST':
        # 获取name=comment的text内容
        comment = request.POST.get('comment')
        if  comment:
            # 实例化数据模型
            cmt = Comment()
            # 评论和blog绑定
            cmt.blog = blog_
            # 评论数自加
            cmt.count += 1
            cmt.text = comment
            cmt.save()
    # else:
    # 可以审核评论

    # 重定向到该博客显示页面
    return redirect('/blog/%s' % id)
