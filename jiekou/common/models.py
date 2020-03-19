
from django.db import models
from datetime import  datetime



class Users(models.Model):
    username = models.CharField(max_length=32)
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
    state = models.IntegerField(default=1)
    create_time = models.DateTimeField()  # 创建时间
    update_time = models.DateTimeField()  # 修改时间

    def toDict(self):
        return {'id':self.id,'username':self.username,'name':self.name,'password':self.password,'state':self.state,'create_time':self.create_time.strftime('%Y-%m-%d %H:%M:%S'),'update_time':self.update_time.strftime('%Y-%m-%d %H:%M:%S')}
        # , 'addtime':self.addtime

    class Meta:
        db_table = "users"  # 更改表名



class Project(models.Model):
    """
    项目表

    操作数据表: 进入django shell (python manage.py shell)
    > from personal.models import Project
    > Project.objects.create(name="test project",describe="this is test project") # 插入数据
    > p = Project.objects.get(id=1) # 查询数据
    > print(p)
    """
    name = models.CharField(max_length=100)
    describe = models.TextField(default="")
    status = models.IntegerField(default=0)
    update_time = models.DateTimeField(default=datetime.now)
    create_time = models.DateTimeField(default=datetime.now)  # 创建时间


    def toDict(self):
        return {'id':self.id,'name':self.name,'describe':self.describe,'status':self.status,'create_time':self.create_time.strftime('%Y-%m-%d %H:%M:%S'),'update_time':self.update_time.strftime('%Y-%m-%d %H:%M:%S')}

    class Meta:
        db_table = "project"  # 更改表名


class Module(models.Model):
    """
    模块表
    """

    name = models.CharField(max_length=100)
    describe = models.TextField(default="")
    create_time = models.DateTimeField(default=datetime.now)
    update_time = models.DateTimeField(default=datetime.now)

    def toDict(self):
        return {'name':self.name,'describe':self.describe,'create_time':self.create_time.strftime('%Y-%m-%d %H:%M:%S'),'update_time':self.update_time.strftime('%Y-%m-%d %H:%M:%S')}

    class Meta:
        db_table = "module"  # 更改表名


class TestCase(models.Model):
    """
    测试用例表
    """

    case_name = models.CharField(max_length=50)
    module_name = models.CharField(max_length=255)
    pro_name = models.CharField(max_length=255)
    url = models.TextField()
    # 1:GET, 2: POST, 3:DELETE, 4:PUT
    method = models.IntegerField()
    header = models.TextField()
    parameter_type = models.IntegerField()  # 1：form-data 2: json
    parameter_body = models.TextField()
    result = models.TextField()
    assert_type = models.IntegerField()  # 1：包含contains 2: 匹配mathches
    assert_text = models.TextField()
    create_time = models.DateTimeField(default=datetime.now)
    status = models.IntegerField(default=0)  # 控制用例的删除
    create_person = models.CharField(max_length=255)
    count = models.IntegerField(default=0)
    run_time = models.IntegerField()
    stop_status = models.IntegerField()



    def toDict(self):
        return {'case_name':self.case_name,'module_name':self.module_name,'pro_name':self.pro_name,'url':self.url,'method':self.method,'header':self.header,'parameter_type':self.parameter_type,'parameter_body':self.parameter_body,'result':self.result,'assert_text':self.assert_text,'create_time':self.create_time.strftime('%Y-%m-%d %H:%M:%S'),'status':self.status,'create_person':self.create_person}

    class Meta:
        db_table = "testcase"  # 更改表名


class TestTask(models.Model):
    """
    任务表
    """
    name = models.CharField(max_length=100)
    describe = models.TextField()
    status = models.IntegerField()  # 未执行、执行中、执行完成、排队中
    cases = models.TextField()  # 存用例的列表
    create_time = models.DateTimeField(default=datetime.now)



    class Meta:
        db_table = "testtask"  # 更改表名


class TestResult(models.Model):
    """
    测试结果表
    """
    name = models.CharField(max_length=100)
    error = models.IntegerField()
    failure = models.IntegerField()
    skipped = models.IntegerField()
    tests = models.IntegerField()
    run_time = models.IntegerField()
    result = models.TextField()
    create_time = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = "testresult"  # 更改表名






