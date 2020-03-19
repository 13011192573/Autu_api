# -*- coding:utf-8 -*-  
# __author__ = "zhangjunjie" 
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from common.models import Project,Module,TestCase
from django.core.paginator import Paginator
import requests,json
import time
from  datetime import datetime

def add(request):
    """
    创建任务
    :param request:
    :return:
    """
    context = {'type':'add'}
    return render(request, 'myadmin/job/add.html', context)

def start_job(request,pIndex):
    list = TestCase.objects.all()

    p = Paginator(list, 10)
    if pIndex == '':
        pIndex = '1'
    pIndex = int(pIndex)
    list1 = p.page(pIndex)
    plist = p.page_range
    context = {'clist': list1, 'plist': plist, 'pIndex': pIndex}
    return render(request, 'myadmin/case/result.html', context)










