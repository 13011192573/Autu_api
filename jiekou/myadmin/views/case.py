# -*- coding:utf-8 -*-  
# __author__ = "zhangjunjie"
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from common.models import Project,Module,TestCase
from django.core.paginator import Paginator
import requests,json
from datetime import datetime
import time

def index(request,pIndex):
    '''浏览信息'''
    mod=TestCase.objects
    mywhere = []
    ckw = request.GET.get('casekeyword', None)
    if ckw:
        list = mod.filter(case_name__contains=ckw)
        mywhere.append("casekeyword=" + ckw)
    else:
        list = mod.filter()

    ukd = request.GET.get('userkeyword', None)
    if ukd:
        list = mod.filter(create_person__contains=ukd)
        mywhere.append("userkeyword=" + ukd)
    elif None:
        list = mod.filter()

    proname = request.GET.get('proname', '')
    if proname != '':
        list = mod.filter(pro_name=proname)
        mywhere.append("proname=" + proname)

    module_name = request.GET.get('module_name', '')
    if module_name != '':
        list = mod.filter(module_name=module_name)
        mywhere.append("module_name=" + module_name)


    pIndex = int(pIndex)
    p=Paginator(list,14)
    maxpages = p.num_pages  # 最大页数
    # 判断页数是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list1=p.page(pIndex)
    plist=p.page_range
    context={'clist':list1,'plist':plist,'pIndex':pIndex, 'mywhere': mywhere}
    return render(request,'myadmin/case/index.html',context)


def debug(request):
    if request.method == "POST":
        url = request.POST.get("url", "")  # URL
        method = request.POST.get("method", "")  # 方法
        header = request.POST.get("header", "")  # header
        par_type = request.POST.get("type", "")  # 参数类型
        par_body = request.POST.get("parameter", "")  # 参数

        if header == "":
            header = "{}"

        try:
            header = json.loads(header)
            print(header)

        except json.decoder.JSONDecodeError:
            return JsonResponse({"result": "header类型错误"})

        if par_body == "":
            par_body = "{}"

        try:
            payload = json.loads(par_body.replace("\'", "\""))
        except json.decoder.JSONDecodeError:
            return JsonResponse({"result": "参数类型错误"})

        result_text = None
        if method == "get":

            r = requests.get(url, params=payload, headers=header)
            result_text = r.text


        if method == "post":

            if par_type == "form":
                r = requests.post(url, data=payload, headers=header)
                result_text = r.text

            if par_type == "json":
                r = requests.post(url, json=payload, headers=header)
                result_text = r.text

        return JsonResponse({"result": result_text})
    else:
        return JsonResponse({"result": "请求方法错误"})

def case_assert(request):
    """
    测试用例的断言
    """
    if request.method == "POST":
        result_text = request.POST.get("result", "")
        assert_text = request.POST.get("assert", "")
        assert_type = request.POST.get("assert_type", "")

        if result_text == "" or assert_text == "":
            return JsonResponse({"result": "断言的文本不能为空"})

        if assert_type == "contains":
            assert_list = assert_text.split(">>")
            for assert_value in assert_list:
                if assert_value not in result_text:
                    return JsonResponse({"result": "断言失败"})
                else:
                    return JsonResponse({"result": "断言成功"})

        elif assert_type == "mathches":
            if assert_text != result_text:
                return JsonResponse({"result": "断言失败"})
            else:
                return JsonResponse({"result": "断言成功"})

    else:
        return JsonResponse({"result": "请求方法错误"})


def save_case(request):
    """
    用例创建/编辑保存

    :param request:
    :return:
    """
    if request.method == "POST":
        url = request.POST.get("url", "")
        method = request.POST.get("method", "")
        header = request.POST.get("header", "")
        parameter_type = request.POST.get("par_type", "")
        parameter_body = request.POST.get("par_body", "")
        assert_type = request.POST.get("ass_type", "")
        assert_text = request.POST.get("ass_text", "")
        module_name = request.POST.get("mid", "")
        pro_name = request.POST.get("pro_name","")
        name = request.POST.get("name", "")
        run_time = request.POST.get("run_time", "")




        if name == "":
            return JsonResponse({"status": 10101, "message": "用例名称不能为空"})

        if module_name == "":
            return JsonResponse({"status": 10103, "message": "所属的模块不能为空"})

        if assert_type == "" or assert_text == "":
            return JsonResponse({"status": 10102, "message": "断言的类型或文本不能为空"})

        # 1:GET, 2: POST, 3:DELETE, 4:PUT
        if method == "get":
            method_number = 1
        elif method == "post":
            method_number = 2
        elif method == "put":
            method_number = 3
        elif method == "delete":
            method_number = 4
        else:
            return JsonResponse({"status": 10104, "message": "未知的请求方法"})

        if parameter_type == "form":
            parameter_number = 1
        elif parameter_type == "json":
            parameter_number = 2
        else:
            return JsonResponse({"status": 10104, "message": "未知的参数类型"})

        if assert_type == "contains":
            assert_number = 1
        elif assert_type == "mathches":
            assert_number = 2
        else:
            return JsonResponse({"status": 10104, "message": "未知的断言类型"})
        try:

            case = TestCase()
            case.case_name = name
            case.module_name = module_name
            case.pro_name = pro_name
            case.url = url
            case.method = method_number
            case.header = header
            case.parameter_type = parameter_number
            case.parameter_body = parameter_body
            case.assert_type = assert_number
            case.assert_text = assert_text
            case.create_time = datetime.now()
            case.create_person = request.session['adminuser']['name']
            case.run_time = run_time
            case.stop_status = 0
            case.save()
            context = {"info": "添加成功"}

        except Exception as err:
            print(err)
            context = {"info": "添加失败"}

        return render(request,'myadmin/info.html',context)

    else:
        return JsonResponse({"status": 10100, "message": "请求方法错误"})


def add(request):

    '''加载添加页面'''
    mlist=Module.objects.all()
    plist=Project.objects.all()
    context={'plist':plist,'mlist':mlist}
    return render(request,'myadmin/case/add.html',context)




def delete(request,cid):
    '''删除信息'''
    try:
        ob = TestCase.objects.get(id=cid)
        ob.status=1

        interval_time(request, cid)

        ob.delete()

        context = {"info": "删除成功"}
    except Exception as err:
        print(err)
        context={"info":"删除失败"}
    return render(request,'myadmin/info.html',context)

def edit(request,cid):
    '''加载编辑信息页面'''
    try:
        plist = Project.objects.all()
        mlist = Module.objects.all()
        ob = TestCase.objects.get(id=cid)
        context = {"clist": ob,'plist':plist,'mlist':mlist}
        return render(request, 'myadmin/case/edit.html', context)
    except Exception as err:
        print(err)
        context={"info":"没有要找到编辑信息"}
        return render(request,'myadmin/info.html',context)



def update(request,cid):
    '''执行编辑信息'''
    if request.method == "POST":
        url = request.POST.get("url", "")
        method = request.POST.get("method", "")
        header = request.POST.get("header", "")
        parameter_type = request.POST.get("par_type", "")
        parameter_body = request.POST.get("par_body", "")
        assert_type = request.POST.get("ass_type", "")
        assert_text = request.POST.get("ass_text", "")
        module_name = request.POST.get("mid", "")
        pro_name = request.POST.get("pro_name","")
        name = request.POST.get("name", "")
        cid = request.POST.get("cid", "")
        run_time = request.POST.get("run_time", "")




        if name == "":
            return JsonResponse({"status": 10101, "message": "用例名称不能为空"})

        if module_name == "":
            return JsonResponse({"status": 10103, "message": "所属的模块不能为空"})

        if assert_type == "" or assert_text == "":
            return JsonResponse({"status": 10102, "message": "断言的类型或文本不能为空"})

        # 1:GET, 2: POST, 3:DELETE, 4:PUT
        if method == "get":
            method_number = 1
        elif method == "post":
            method_number = 2
        elif method == "put":
            method_number = 3
        elif method == "delete":
            method_number = 4
        else:
            return JsonResponse({"status": 10104, "message": "未知的请求方法"})

        if parameter_type == "form":
            parameter_number = 1
        elif parameter_type == "json":
            parameter_number = 2
        else:
            return JsonResponse({"status": 10104, "message": "未知的参数类型"})

        if assert_type == "contains":
            assert_number = 1
        elif assert_type == "mathches":
            assert_number = 2
        else:
            return JsonResponse({"status": 10104, "message": "未知的断言类型"})

    try:
        case=TestCase.objects.get(id=cid)
        case.case_name = name
        case.module_name = module_name
        case.pro_name = pro_name
        case.url = url
        case.method = method_number
        case.header = header
        case.parameter_type = parameter_number
        case.parameter_body = parameter_body
        case.assert_type = assert_number
        case.assert_text = assert_text
        case.create_time = datetime.now()
        case.create_person = request.session['adminuser']['name']
        case.run_time=run_time
        case.stop_status=0
        case.save()
        context = {"info": "修改成功"}

    except Exception as err:

        print(err)
        context={"info":"修改失败"}
    return render(request,'myadmin/info.html',context)




def run_case(request,cid):

    case = TestCase.objects.get(id=cid)

    case_name = case.case_name
    module_name = case.module_name
    pro_name = case.pro_name
    print("当前运行的case"+case_name)
    url = case.url
    method_num = case.method
    header = case.header
    parameter_number = case.parameter_type
    parameter_body = case.parameter_body
    result = case.result
    assert_num = case.assert_type
    assert_text = case.assert_text
    status = case.status

    if method_num == 1:
        method_type = "get"
    elif method_num == 2:
        method_type = "post"
    elif method_num == 3:
        method_type = "delete"
    elif method_num == 4:
        method_type = "put"
    else:
        return JsonResponse({"status": 10104, "message": "未知的请求方法"})

    if parameter_number == 1:
        parameter_type = "form"
    elif parameter_number == 2:
        parameter_type = "json"
    else:
        return JsonResponse({"status": 10104, "message": "未知的参数类型"})

    if assert_num == 1:
        assert_type = "contains"
    elif assert_num == 2:
        assert_type = "mathches"
    else:
        return JsonResponse({"status": 10104, "message": "未知的断言类型"})

    try:
        header = json.loads(header.replace("\'", "\""))
    except json.decoder.JSONDecodeError:
        return JsonResponse({"result": "header类型错误"})

    try:
        parameter_body = json.loads(parameter_body.replace("\'", "\""))
    except json.decoder.JSONDecodeError:
        return JsonResponse({"result": "参数类型错误"})
    # 发送请求
    result_text = None

    if method_num == 1:
        r = requests.get(url, params=parameter_body, headers=header)
        result_text = r.text
    if method_type == "post":
        if parameter_type == "form":
            r = requests.post(url, data=parameter_body, headers=header)
            result_text = r.text

        if parameter_type == "json":
            r = requests.post(url, json=parameter_body, headers=header)
            result_text = r.text

    #
    if assert_type == "contains":
        assert_list = assert_text.split(">>")
        for assert_value in assert_list:
            if assert_value not in result_text:
                fail_case(request,cid)
            else:
                sucess_case(request,cid)

    elif assert_type == "mathches":
        if assert_text != result_text:
            fail_case(request, cid)
        else:
            sucess_case(request, cid)

    return render(request,'myadmin/info.html')

def interval_time(request,cid):

    if request.method == "POST":
        statusb = request.POST.get("status", "")


        ob = TestCase.objects.get(id=cid)
        ob.stop_status = 1
        ob.save()
        interval = ob.run_time
        interval = interval * 60
        status=int(statusb)
        while True:
            try:

                if status == 0:
                    run_case(request, cid)

                    time.sleep(interval)
                else:

                    context = {"info": "case已停止运行"}

                    return render(request, 'myadmin/info.html', context)


            except Exception as e:
                print(e)

    return render(request, 'myadmin/info.html')

def stop_case(request,cid):
    ob = TestCase.objects.get(id=cid)
    ob.stop_status = 0
    ob.save()

    return render(request, 'myadmin/info.html')



def fail_case(request,cid):


    ob = TestCase.objects.get(id=cid)
    case_name=ob.case_name
    pro_name=ob.pro_name
    module_name=ob.module_name

    ob.result = "运行失败"
    ob.count += 1
    ob.save()
    meg = {"消息内容": "case运行失败请关注",
           "失败的caseid": cid,
           "失败的case名称": case_name,
           "失败的case所属项目": pro_name,
           "失败的case所属模块": module_name,
           }

    # 钉钉机器人
    headers = {"Content-Type": "application/json"}
    data = {"msgtype": "text",
            "text": {
                "content": meg
            }
            }

    json_data = json.dumps(data)
    requests.post(
        url='https://oapi.dingtalk.com/robot/send?access_token=d1a1d8b4f76a204148e0ba6558be6b0cd66d1d5e7b4464051784525ae0b8b9a6',
        data=json_data, headers=headers)

    context = {"info": "运行失败"}
    return render(request,'myadmin/info.html',context)

def sucess_case(request,cid):
    ob = TestCase.objects.get(id=cid)

    ob.result = "运行成功"
    ob.count += 1
    ob.save()
    context = {"info": "运行成功"}
    return render(request, 'myadmin/info.html', context)







