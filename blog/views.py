from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

# Create your views here.
from markdown import markdown

from blog.models import Blog, Category, Tag
from comment.models import Comment


def index(request):
    return render(request, 'index.html')


def blog(request):
    # 以创建博客时间倒序
    blog_time = Blog.objects.order_by('-created_time')
    # 阅读量排序
    hotviews = Blog.objects.order_by('-views')[:3]
    # 分类
    categorys = Category.objects.order_by('name')

    # 最近评论
    comments = Comment.objects.order_by('-created_time')[:3]

    # 分页
    page = request.GET.get('page')
    # 每页显示5个
    contacts = listing(blog_time, page, limit=10)
    return render(request, 'blog.html', {'hotviews': hotviews,
                                         'categorys': categorys,
                                         'comments': comments,
                                         'contacts': contacts})


# 单个分类 内容显示
def categorys(request, **kwargs):
    id = kwargs['id']
    # 反向查询
    # 通过获取到的id查询该分类对象
    category = Category.objects.get(id=id)
    # 通过外键关联词Category查询文章：
    cate_blogs = category.Category.all().order_by('-created_time')

    # 分页
    # 获取当前页面数
    page = request.GET.get('page')
    #
    contacts = listing(cate_blogs, page, limit=10)
    return render(request, 'categorys_blog.html', {'contacts': contacts,
                                                   'category': category})


# 单个博客显示
def blog_single(request, **kwargs):
    # 获取url参数文章id,
    id = kwargs['id']
    # 查询该id文章的所有内容
    singleblog = Blog.objects.filter(id=id).first()
    # 调用views_count，阅读数计数
    Blog.views_count(singleblog)
    # 博客评论显示
    sblog = Blog.objects.get(id=id)
    # 用related_name反向查询该文章的所有评论表的信息
    blog_comment = sblog.comment_blog.all().order_by('-created_time')[:5]
    # 获取该文章的所有标签
    tag = sblog.tags.all()[0]
    # 查询分类
    cate_name = Category.objects.order_by('name')

    # makrdown渲染
    singleblog_body = markdown(singleblog.body)

    return render(request, 'single-post.html', {'singleblog': singleblog,
                                                "cate_name": cate_name,
                                                'blog_comment': blog_comment,
                                                'singleblogs_body': singleblog_body,
                                                'tag': tag,
                                                })


# 搜索标题，并显示搜索内容
def search(request):
    # 获取input  name属性的值
    search = request.GET.get('search')
    # 通过filter过滤title的内容，title__contains：精确大小写，title__icontains:忽略大小写
    # 'contains': 'LIKE BINARY %s',
    # 'icontains': 'LIKE %s',
    search_datas = Blog.objects.filter(title__icontains=search)
    return render(request, 'search.html', {'contacts': search_datas})


# 归档

def regroup(request):
    tags = Tag.objects.all()
    return render(request, 'regroup.html', {'tags': tags})


# 标签
def tag(request, **kwargs):
    name = kwargs['tag']
    tag = Tag.objects.filter(name=name)[0]
    # 通过related_name查询该标签的所有博客
    blog = tag.Tag.all()
    return render(request, 'tag.html', {'blogs': blog,
                                        'tag': tag})


# 分页
def listing(Queryset, page, limit):
    """
    :param Queryset:   要展示的对象列表QuerySet
    :param page: 获取当前页数
    :param limit: 每页显示的个数
    :return: contacts:返回一个分页对象contacts
    """
    # 分页

    # 1.获取要展示的对象列表QuerySet，每页显示2个
    paginator = Paginator(Queryset, limit)
    # 获取请求的page数
    # page = request.GET.get('page')
    # 2.将列表和每页个数传递给Paginator，返回一个分页对象contacts
    try:
        # 获取某页对应的记录
        contacts = paginator.page(page)
    except  PageNotAnInteger:
        # 如果请求的页数不是整数，则返回第一页
        contacts = paginator.page(1)
    except  EmptyPage:
        # 如果请求的页面不存在,则返回最后一页
        # Paginator.num_pages：页面总数。
        contacts = paginator.page(paginator.num_pages)
    return contacts
