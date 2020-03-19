# -*- coding:utf-8 -*-  
# __author__ = "zhangjunjie"
from django.shortcuts import render
from django.http import HttpResponse
from common.models import Project,Module
from django.core.paginator import Paginator
from  datetime import datetime
#用户信息管理
def index(request,pIndex):
    '''浏览信息'''
    list=Module.objects.all()

    p=Paginator(list,10)
    if pIndex == '':
        pIndex = '1'
    pIndex=int(pIndex)
    list1=p.page(pIndex)
    plist=p.page_range
    context={'mdlist':list1,'plist':plist,'pIndex':pIndex}
    return render(request,'myadmin/module/index.html',context)



def add(request):

    '''加载添加页面'''
    plist=Project.objects.all()
    context={'plist':plist}
    return render(request,'myadmin/module/add.html',context)


def insert(request):
    '''执行添加信息'''
    try:
        ob=Module()
        ob.name=request.POST['modulename']
        ob.describe=request.POST['describe']
        ob.save()
        context={"info":"添加成功"}

    except Exception as err:

        print(err)
        context={"info":"添加失败"}
    return render(request,'myadmin/info.html',context)


def delete(request,mid):
    '''删除信息'''
    try:
        ob = Module.objects.get(id=mid)
        ob.delete()
        context = {"info": "删除成功"}
    except Exception as err:
        print(err)
        context={"info":"删除失败"}
    return render(request,'myadmin/info.html',context)

def edit(request,mid):
    '''加载编辑信息页面'''
    try:
        plist = Project.objects.all()
        ob = Module.objects.get(id=mid)
        context = {"module": ob,'plist':plist}
        return render(request, 'myadmin/module/edit.html', context)
    except Exception as err:
        context={"info":"没有要找到编辑信息"}
        return render(request,'myadmin/info.html',context)



def update(request,mid):
    '''执行编辑信息'''
    try:
        ob=Module.objects.get(id=mid)
        ob.name=request.POST['modulename']
        ob.describe=request.POST['describe']
        ob.save()
        context={"info":"修改成功"}

    except Exception as err:

        print(err)
        context={"info":"修改失败"}
    return render(request,'myadmin/info.html',context)

