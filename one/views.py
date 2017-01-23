# coding=utf-8
import sys

from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.core.paginator import Paginator
from django.shortcuts import render

from models import Daily

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    dailylist = Daily.objects.order_by('-id').all()[:5]  # 查询所有的信息
    print(type(dailylist))  # 打印结果类型与结果值
    for s in dailylist:
        print (s.hp_title.decode('utf-8'))
    context_dict = {'content': dailylist}

    return render(request, 'one/index.html', context_dict)


def about(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'one/about.html', context_dict)


def search(request):
    result_list = []
    limit = 5  # 每页显示的记录数

    if request.method == 'POST':
        query = request.POST['query'].strip()

        if query:
            # Run our Bing function to get the results list!
            result_list = Daily.objects.order_by('-id').filter(hp_content__contains=query)
            paginator = Paginator(result_list, limit)  # 实例化一个分页对象

            page = request.GET.get('page')  # 获取页码
            try:
                result_list = paginator.page(page)  # 获取某页对应的记录
            except PageNotAnInteger:  # 如果页码不是个整数
                result_list = paginator.page(1)  # 取第一页的记录
            except EmptyPage:  # 如果页码太大，没有相应的记录
                result_list = paginator.page(paginator.num_pages)  # 取最后一页的记录

    else:
        query = request.GET.get('query')
        result_list = Daily.objects.order_by('-id').filter(hp_content__contains=query)
        paginator = Paginator(result_list, limit)  # 实例化一个分页对象

        page = request.GET.get('page')  # 获取页码
        try:
            result_list = paginator.page(page)  # 获取某页对应的记录
        except PageNotAnInteger:  # 如果页码不是个整数
            result_list = paginator.page(1)  # 取第一页的记录
        except EmptyPage:  # 如果页码太大，没有相应的记录
            result_list = paginator.page(paginator.num_pages)  # 取最后一页的记录

    return render(request, 'one/search.html', {'result_list': result_list, 'query': query})
