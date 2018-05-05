from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category
from rango.models import Page

def show_category(request,category_name_slug):
    '''
    创建上下文字典，稍后传给模板渲染引擎
    通过分类别名，找到对应分类名
    找不到，抛出异常 DoesNotExist
    :param request:
    :return:
    '''
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug) # Category 有slug字段
        print(":::",category)
        # 检索网页
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['pages']=None
        context_dict['category']=None

    # 渲染模板，返回客户端
    return render(request,'rango/category.html',context_dict)



def index0(request):
    # 构建一个字典，作为上下文传给模板引擎
    # 注意，boldmessage 键对应于模板中的 {{bold message}}

    context_dict = {
        'boldmessage':"Crunchy, creamy, cookie, candy, cupcake!"
    }

    # 返回一个渲染后的响应发给客户端
    # 为了方便，我们使用的是render 函数的简短形式
    # 注意，第二个参数是我们想使用的模板
    return render(request,'rango/index.html',context=context_dict)

def index(request):
    '''
    # 查询数据库，获取存储的分类
    # 按照点赞次数倒序排列
    # 获取前5个分类
    # 分类列表放入 context_dict
    # 传给模板引擎
    :param request:
    :return:
    '''

    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories':category_list,'pages':page_list}

    # 渲染响应，发送给客户端
    return render(request,'rango/index.html',context_dict)


