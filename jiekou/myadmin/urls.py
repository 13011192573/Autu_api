#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__=v_zhangjunjie02
from django.conf.urls import url


from myadmin.views import index,users,project,module,case,job,utils

urlpatterns = [
    # 后台首页
    url(r'^$', index.index, name="myadmin_index"),

    # 用户注册路由
    url(r'^register$', index.register, name="myadmin_register"),
    url(r'^doregister$', index.doregister, name="myadmin_doregister"),
    # 用户登录和退出路由配置
    url(r'^login$', index.login, name="myadmin_login"),
    url(r'^dologin$', index.dologin, name="myadmin_dologin"),
    url(r'^logout$', index.logout, name="myadmin_logout"),

    url(r'^users/(?P<pIndex>[0-9]+)$', users.index, name='myadmin_users_index'),
    url(r'^usersa/(?P<pIndex>[0-9]+)$', users.indexa, name='myadmin_usersa_index'),
    url(r'^users/resetpd/(?P<uid>[0-9]+)$', users.resetpassword, name='myadmin_users_resetpd'),
    url(r'^users/updatepd/(?P<uid>[0-9]+)$', users.updatepd, name='myadmin_pd_update'),
    url(r'^users/add$', users.add, name='myadmin_users_add'),
    url(r'^users/insert$', users.insert, name='myadmin_users_insert'),
    url(r'^users/del/(?P<uid>[0-9]+)$', users.delete, name='myadmin_users_del'),
    url(r'^users/edit/(?P<uid>[0-9]+)$', users.edit, name='myadmin_users_edit'),
    url(r'^users/update/(?P<uid>[0-9]+)$', users.update, name='myadmin_users_update'),


    #项目路由
    url(r'^project/(?P<pIndex>[0-9]+)$', project.index, name='myadmin_project_index'),
    url(r'^project/add$', project.add, name='myadmin_project_add'),
    url(r'^project/insert$', project.insert, name='myadmin_project_insert'),
    url(r'^project/del/(?P<pid>[0-9]+)$', project.delete, name='myadmin_project_del'),
    url(r'^project/edit/(?P<pid>[0-9]+)$', project.edit, name='myadmin_project_edit'),
    url(r'^project/update/(?P<pid>[0-9]+)$', project.update, name='myadmin_project_update'),

    #模块路由

    url(r'^module/(?P<pIndex>[0-9]+)$', module.index, name='myadmin_module_index'),
    url(r'^module/add$', module.add, name='myadmin_module_add'),
    url(r'^module/insert$', module.insert, name='myadmin_module_insert'),
    url(r'^module/del/(?P<mid>[0-9]+)$', module.delete, name='myadmin_module_del'),
    url(r'^module/edit/(?P<mid>[0-9]+)$', module.edit, name='myadmin_module_edit'),
    url(r'^module/update/(?P<mid>[0-9]+)$', module.update, name='myadmin_module_update'),

    #用例路由
    url(r'^case/(?P<pIndex>[0-9]+)$', case.index, name='myadmin_case_index'),
    url(r'^case/add$', case.add, name='myadmin_case_add'),
    url(r'^case/del/(?P<cid>[0-9]+)$', case.delete, name='myadmin_case_del'),
    url(r'^case/edit/(?P<cid>[0-9]+)$', case.edit, name='myadmin_case_edit'),
    url(r'^case/update_case/(?P<cid>[0-9]+)', case.update, name='myadmin_case_update'),
    url(r'^case/debug/$', case.debug, name='myadmin_case_debug'),
    url(r'^case/assert_case/$', case.case_assert, name='myadmin_case_assert'),
    url(r'^case/save_case/$', case.save_case, name='myadmin_case_save'),
    url(r'^case/run/(?P<cid>[0-9]+)$', case.interval_time, name='myadmin_case_run'),
    url(r'^case/stop/(?P<cid>[0-9]+)$', case.stop_case, name='myadmin_stop_case'),




    #测试任务路由
    url(r'^job/(?P<pIndex>[0-9]+)$', job.start_job, name='myadmin_report_index'),

    #Json格式化工具
    url(r'^utils$',utils.Json_API, name='utils'),

]
