## Django

### 安装步骤
1. 进入命令终端 执行: pip install Django=1.11.4
2. 等待下载安装完成即可
3. 验证 ，进入Python环境,执行以下代码
    ```python
    import django
    django.get_version()
    ```

### 创建项目
1. 执行： django-admin startproject djangotest(项目名)
2. 项目目录层级说明
    - manage.py ： 一个命令行工具，可以使我们用多种方式对Django项目进行交互
    - \__init__.py : 一个空文件，告诉Python这个目录应该被看作一个python包
    - settings.py ： 项目的配置文件
    - urls.py : 项目的URL 声明
    - wsgi.py : 项目与WSGI兼容的Web服务器入口

### 基本操作
1. 配置数据库
    - Django默认使用SQLite数据库
    - 在settings.py文件中，通过 DATABASES 选项进行数据库配置
    - 配置Mysql
        1. Python3.x安装的是PyMySQL
        2. 在__init__.py文件中写入两行代码
            - import pymysql
            - pymysql.install_as_MySQLdb()
        3. 配置 settings.py
            ```python
            DATABASES = {
                'default': {
                    #'ENGINE': 'django.db.backends.sqlite3',
                    #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                    'ENGINE': 'django.db.backends.mysql',
                    'NAME': 'djangotestdb', # 库的名字
                    'USER':'root',
                    'PASSWORD':'root123',
                    'HOST':'127.0.0.1',
                    'PORT':'3306',
                }
            }
            ```
2. 创建应用
    - 在一个项目中可以创建多个应用，每个应用进行一种业务的处理
    - 在项目目录下执行
        1. python manage.py startapp myApp
        2. 可能会报错，1.11版本和python3.7版本不兼容
        3. 升级版本： pip install --upgrade Django==2.2.12
    - 目录说明
        1. admin.py 站点配置
        2. models.py 模型
        3. views.py 视图
3. 激活应用
    - 在settings.py文件中，将myApp应用加入到 INSTALLED_APPS 选项中
        ```python
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'myApp',
        ]
        ```
4. 定义模型
    - 概述：有一个数据表，就对应一个模型
    - 在models.py文件中定义模型
        1. 引入 from django.db import models
        2. 模型类需要继承 models.Model 类
        3. 在models.py文件中创建类
            ```python
            class Grades(models.Model):
                gname = models.CharField(max_length=20)
                gdate = models.DateTimeField()
                ggirlnum = models.IntegerField()
                gboynum = models.IntegerField()
                isDelete = models.BooleanField()
            class Students(models.Model):
                sname = models.CharField(max_length=20)
                sgender = models.BooleanField(default=True)
                sage = models.IntegerField()
                scontent = models.CharField(max_length=20)
                isDelete = models.BooleanField(default=False)
                # 关联外键
                sgrade = models.ForeignKey('Grades', on_delete=models.CASCADE)
            ```
        4. 不需要定义主键，在生成时自动添加，并且值为自动增加
5. 在数据库中生成数据表
    - 生成迁移文件， 执行 python manage.py makemigrations 在migrations目录下会生成迁移文件，此时数据库中还没有生成表
    - 执行迁移 ：python manage.py migrate  相当于执行了SQL，创建表
6. 测试数据操作
    - 进入 python shell ： python manager.py shell
    - 引入一些包
        1. from myApp.models import Grades,Students
        2. from django.utils import timezone
        3. from datetime import *
    - 查询表数据,类名.objects.all()
        ```python
        Grades.objects.all()
        ```
    - 添加数据，本质就是创建一个模型类的对象实例
        ```python
        grade1 = Grades()
        grade1.gname = '高一三班'
        grade1.gdate = datetime(year=2017, month=7, day=23)
        grade1.ggirlnum = 5
        grade1.gboynum = 30
        # 保存数据
        grade1.save()
        ```
    - 查询某个对象
        ```python
        g1 = Grades.objects.get(pk=1)
        ```
    - 修改某个对象
        ```python
        g1 = Grades.objects.get(pk=1)
        g1.gboynum = 10
        gi.save()
        ```
    - 删除某个对象
        ```python
        g1 = Grades.objects.get(pk=1)
        gi.delete() # 物理删除
        ```
    - 关联对象
        1. 保存关联对象
            ```python
            g1 = Grades.objects.get(pk=1)

            stu = Students()
            stu.sname = '张三'
            stu.sgender = True
            stu.sage = 20
            stu.scontent = '我叫张三'
            stu.sgrade = g1 # 关联班级
            stu.save()
            ```
        2. 获取关联对象的集合
            ```python
            g1 = Grades.objects.get(pk=1)
            g1.students_set.all() # 获取该班级的所有学生， 类对象.关联类名小写_set.all()
            ```
        3. 创建一个学生，属于某个班级，另一种操作
            ```python
            g1 = Grades.objects.get(pk=1)
            g1.students_set.create(sname=u'李四',.....)
            ```

### 启动服务器
1.格式
    - python manage.py runserver ip:port
    - ip可以不写，不写代表本机ip
    - 端口默认 8000
2. 说明
    -这是一个纯python写的轻量级Web服务器。仅仅在开发测试中使用

### Admin站点管理
1. 概述
    - 内容发布
        1. 添加
        2. 修改
        3. 删除
    - 公告访问
2. 配置Admin应用
    - 在settings.py 文件中添加 INSTALLED_APPS 中添加 django.contrib.admin (默认已添加)
3. 创建管理员用户
    - python manage.py createsuperuser
    - 输入用户名
    - 输入邮箱
    - 输入密码
    - [登录页面](http://127.0.0.1:8000/amdin)
    - 页面汉化： settings.py
        ```python
        LANGUAGE_CODE = 'zh-Hans'
        TIME_ZONE = 'Asia/Shanghai'
        ```
    - 管理数据表: admin.py
        1. 配置
            ```python
            from .models import Grades,Students
            # 注册
            admin.site.register(Grades)
            admin.site.register(Students)
            ```
        2. 自定义管理页面
            - 列表页属性
                1. list_display 显示字段
                2. list_filter 过滤字段
                3. search_fields 搜索字段
                4. list_per_page 分页
            - 添加修改也属性
                1. fields 属性显示的先后顺序
                2. fieldsets 给属性分组
                3. fields 与 fieldsets 不能同时使用
        3. 关联对象
            - 在创建编辑同时创建学生
                ```python
                # admin.TabularInline
                # admin.StackedInline 都可以，只是显示不同
                class StudentsInfo(admin.TabularInline):
                    model = Students
                    extra = 2 # 每次创建2个
                class GradesAdmin(admin.ModelAdmin):
                    inlines = [StudentsInfo]
                ```
        4. 性别布尔值显示问题
            ```python
            class StudentsAdmin(admin.ModelAdmin):

                # 解决布尔值男女显示问题
                def gender(self):
                    if self.sgender:
                        return '男'
                    else:
                        return '女'
                # 设置页面列的名称
                gender.short_description = '性别'

                list_display = ['pk', 'sname', gender, 'sage', 'scontent', 'sgrade', 'isDelete']
            ```
        5. 执行动作的位置
            ```python
            # 执行动作的位置
            actions_on_top = False
            actions_on_bottom = True
            ```
        6. 完整配置
            ```python
            from django.contrib import admin

            # Register your models here.

            from .models import Grades,Students

            # admin.TabularInline 
            # admin.StackedInline 都可以，只是显示不同
            class StudentsInfo(admin.TabularInline):
                model = Students
                extra = 2 # 每次创建2个

            class GradesAdmin(admin.ModelAdmin):

                inlines = [StudentsInfo]
                # 列表属性
                # 显示字段
                list_display = ['pk', 'gname', 'gdate', 'ggirlnum', 'gboynum']
                # 过滤字段
                list_filter = ['gname']
                # 搜索字段
                search_fields = ['gname']
                # 分页
                list_per_page = 5

                # 添加修改也属性
                # 属性显示的先后顺序
                # fields = ['gdate', 'gname', 'gboynum', 'ggirlnum', 'isDelete']
                # 给属性分组
                # fields 与 fieldsets 不能同时使用
                fieldsets = [('num', {'fields': ['gboynum', 'ggirlnum']}), ('base', {'fields': ['gdate', 'gname', 'isDelete']})]
            
            class StudentsAdmin(admin.ModelAdmin):
                # 解决布尔值男女显示问题
                def gender(self):
                    if self.sgender:
                        return '男'
                    else:
                        return '女'
                # 设置页面列的名称
                gender.short_description = '性别'
                list_display = ['pk', 'sname', gender, 'sage', 'scontent', 'sgrade', 'isDelete']
                list_per_page = 2

            # 执行动作的位置
            actions_on_top = False
            actions_on_bottom = True


            # 注册
            admin.site.register(Grades, GradesAdmin)
            admin.site.register(Students, StudentsAdmin)
            ```
        7. 使用装饰器注册
            ```python
            @admin.register(Students)
            class StudentsAdmin(admin.ModelAdmin):

                # 解决布尔值男女显示问题
                def gender(self):
                    if self.sgender:
                        return '男'
                    else:
                        return '女'
                # 设置页面列的名称
                gender.short_description = '性别'

                list_display = ['pk', 'sname', gender, 'sage', 'scontent', 'sgrade', 'isDelete']
                list_per_page = 2

                # 执行动作的位置
                actions_on_top = False
                actions_on_bottom = True
            ```

### 视图的基本使用
1. 概述
    - 在Django中，视图对Web请求进行回应
    - 视图就是一个python函数
2. 定义视图 views.py
    ```python
    from django.http import HttpResponse

    def index(request):
        return HttpResponse('Hello World!')
    ```
3. 配置url
    - 修改项目目录下的urls.py
        ```python
        from django.contrib import admin
        from django.urls import path,include

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', include('myApp.urls'))
        ]
        ```
    - 在myApp应用目录下创建一个urls.py
        ```python
        from django.urls import path

        from . import views

        urlpatterns = [
            path('', views.index)
        ]
        ```

### 模版的基本使用
1. 概述
    - 模版是HTML页面，可以根据视图中传递过来的数据进行填充
    - 创建模版目录
        1. 创建 templates 目录，在其下再创建一个 myApp 目录，因为一个项目可以有多个app，为了做区分
    - 配置模板路径
        1. 修改settings.py文件中的 TEMPLATES 的DIRS
            ```python
            TEMPLATES = [
                {
                    'BACKEND': 'django.template.backends.django.DjangoTemplates',
                    'DIRS': [os.path.join(BASE_DIR, 'templates')],
                    'APP_DIRS': True,
                },
            ]
            ```
        2. 定义了两个模板 grades.html和students.html
            模板语法：
                - {{输出值，可以是变量，也可以是对象.属性}}
                - {%执行代码段%}
        3. 配置视图 views.py 及myAPP下的urls.py
            - views.py
                ```python
                from .models import Grades, Students
                def grades(request):
                    # 去模板获取数据
                    gradesList = Grades.objects.all()
                    # 将数据传递给模板
                    # 模板渲染页面，将渲染好的页面返回给浏览器
                    return render(request, 'myAPP/grades.html',{'grades':gradesList})
                ```
            - urls.py
                ```python
                urlpatterns = [
                    path('', views.index),
                    path('grades/', views.grades)
                ]
                ```
        4. 浏览器输入 http://127.0.0.1:8000/grades