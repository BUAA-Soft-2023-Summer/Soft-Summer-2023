# Django入门

## 一、环境配置

对于不同的项目，支持的Python版本不同，所以对于不同的环境，需要单独配置环境。给不同项目单独配置的环境叫做**虚拟环境**，管理虚拟环境的工具叫做 Conda，在这里我们选择Anaconda。

Anaconda下载地址：

- 官网：[ ](https://www.anaconda.com/)https://www.anaconda.com/
- 清华镜像：[ ](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/)https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/（选择最新版本即可）

1.在安装时，注意勾选添加至环境变量中。
2.安装 Anaconda 后，使用 conda 指令新建一个虚拟环境，用于开发 Django 项目。

```
conda create --name django python=3.9   # 虚拟环境名为django，python版本指定3.9
```

3.激活虚拟环境。每次运行项目，都需要保证在虚拟环境中，如果测试命令行前出现 (django) 说明成功进入虚拟环境。

``` python
conda activate django
```

4.安装django依赖

``` python
pip install django
```

5.安装pymysql

```python
pip install pymysql
```

## 二、创建项目

###### 法一：命令行创建

1.在某个文件夹打开终端，输入以下指令创建Django项目

```
django-admin toDoList
```

2.创建一个app，app 用于实现业务逻辑，包含数据库模型的建立、建立路由和API响应前端的请求。

``` 
python manage.py startapp api
```

###### 法二：Pycharm创建

进入Pycharm，点击导航栏文件处，选择新建项目。

![pPM637t.png](https://s1.ax1x.com/2023/08/14/pPM637t.png)

## 三、项目结构

创建完成后的项目结构为：

```txt
toDoList
| 
|-- api            # app目录
|   |-- __init__.py     # python包声明
|   |-- admin.py
|   |-- apps.py         # app配置文件(一般不用修改)
|   |-- models.py       # 数据库模型配置(数据库表的创建与更新，很重要)
|   |-- tests.py        # 测试模块(一般不用修改)
|   `-- views.py        # 视图编写文件（API实现业务逻辑，响应前端的请求，很重要）
|-- toDoList
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py     # 项目配置文件(很重要) --- 建议大家出错 or 跑不起来以后首先检查该文件配置是否合适
|   |-- urls.py         # 后端路由设置(很重要)
|   `-- wsgi.py         # uwsgi运行入口(一般不用修改)
|-- manage.py           # django命令行工具(一般不用修改)
`-- db.sqlite3          # 数据库文件
```

重点需要修改的文件为：

- toDoList/models.py：数据库模型设置，在这里要建立数据库表项及其属性
- toDoList/views.py：编写api的文件，在这里要编写和规划所有的请求处理函数。
- api/settings.py：项目总配置文件，在这里实现跨域设置、app信息等
- api/urls.py：后端路由设置，在这里指定后端API的路由，以供前端发送请求
- db.sqlite3：数据库文件，无需修改

### 项目预设置

1. 添加app信息：

    - 若是在 Pycharm 中创建的项目，在 toDoList/settings.py 中已自动添加好 app 信息，无需再度添加

    - 如果是命令行创建，则需在 settings 文件的 `INSTALLED_APPS` 中添加 app 名字。如下

        ```python
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'api'  # 加入自己定义的 app
        ]
        ```

2. 路由分发：在小型项目里，不同 app 全部 api 的路由可以放在一个文件`toDoList/urls.py`。（路由的写法参考以下[链接](https://docs.djangoproject.com/zh-hans/4.2/topics/http/urls/)）

    ```python
    urlpatterns = [
        path('api/create/', api.views.create),#创建任务
        path('api/delete/', api.views.delete),#删除任务
    ]
    ```

    处理 URL 请求的过程可以总结于以下的流程：

    1. Django 从配置文件中根据 ROOT——URLCONF 找到主路由文件；默认情况下，该文件在项目同名目录下的urls.py
    2. Django 加载 主路由 文件中的 urlpatterns 变量 [很多路由的列表]
    3. 依次匹配 urlpatterns 中的 path ，匹配到第一个合适的中断后续匹配
    4. 匹配成功–调用对应的视图函数处理请求，返回响应
    5. 匹配失败–返回404响应

3. 数据库配置：大家需要提前阅读 [web开发：数据库]，拥有自己的的账户，密码。然后在 settings 文件的`DATABASES `修改信息如下：

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'xxx',#数据库名
            'USER': 'xxx',#用户名
            'PASSWORD': 'xxx',#密码
            'HOST': 'xxxx',
            'PORT': '3306'#端口
        }
    }
    ```

## 四、toDoList实现思路

### 确定功能

假设：任务标题唯一，可作为任务的标识

目前我们要实现的功能为：

- 新增任务：前端发送 任务标题、任务内容、任务结束时间，后端新建任务创建时间，并将所有信息存到数据库中。
- 删除任务：前端发送需要删除的任务id，后端删除数据库中对应任务。
- 更新任务：前端发送更新的任务内容，后端存储到数据库。
- 根据时间搜索任务：前端发送时间，后端搜索返回所有截止日期早于改时间的任务。
- 根据标题搜索任务：前端发送标题，后端搜索返回指定任务详细信息。
- 获取任务：后端返回所有任务。

### 创建数据库模型

数据库模型：

- 是一个Pyhton类，它是由django.db.models.Model派生出来的子类
- 一个模型类代表数据库中的一张数据表
- 模型类中每一个类属性都代表数据库中的一个字段
- 模型是数据交互的接口，是表示和操作数据库的方式和方法

1. 根据功能需要一个表来存储所有的任务。所有的字段包括：任务标题、任务内容、任务创建时间、任务结束时间。修改`api/models.py`文件如下：

```python
from django.db import models
STATUS_ITEMS = [
    (0, '未完成'),
    (1, '已完成')
]
# Create your models here.
class ItemInfo(models.Model):
    title = models.CharField(max_length=128, null=False, primary_key=True, verbose_name='标题')
    content = models.TextField(null=True, default='用户暂未添加描述', verbose_name='描述')
    status = models.IntegerField(choices=STATUS_ITEMS, verbose_name='状态')
    createTime = models.DateTimeField(null=False, verbose_name='创建时间')
    endTime = models.DateField(null=True, verbose_name='结束时间')
```

> 注：
>
> * 上述语句相当于告诉数据库目前需要一个表叫做 `ItemInfo`，这个表里面储存的数据分别是 `title`，`content`，`status` 还有 `createTime` 和 `endTime`。每一个字段的类型由后面的 `xxxField` 指定。以 `CharField` 为例， `max_length=128` 代表该项最多储存 128 字节的字符，`null=False` 意味着在新建某一条数据的时候该项不能为空， `primary_key` 意为该项是该表的主键，目前对主键不需要太多了解，需要知道两个点：一个表里只能有一个主键，而且表里面主键的值不能重复(加在这里的目的就是我想要让这一项不允许重复，便于后面的查找)。如果自己不定义的话数据库会默认创建一个自增的 `id` 作为主键，也是可以的。而 `verbose_name` 是我加的注释，意为告诉自己每一项都是干什么用的，这个意义不大。其他类型同理。
> * 有关于 `status` 其实可以直接设置为一个 `Integerfield` 的类型然后储存 `0` 和 `1` 分别代表进行中和完成，这里这样写纯粹是为了增强代码可读性。
> * 每一个类型具体的参数含义以及使用可参考[官方文档](https://docs.djangoproject.com/zh-hans/4.2/ref/models/fields/#field-types)

如果不指定的话数据库会默认创建一个自增的id，后续会用到，无需手动创建：

````python
id = models.AutoField(primary_key=True)
````

2. 在修改数据库模型之后，**一定要**生成迁移文件，并应用新的数据库模型。在终端输入以下指令。

```python
python manage.py makemigrations # 生成迁移文件
python manage.py migrate        # 迁移数据库模型
```

在数据库里，就能看见新的表格，如下：

![pPM6lnA.png](https://s1.ax1x.com/2023/08/14/pPM6lnA.png)

### 实现功能

一个业务功能的实现，一般分为两步：编写业务逻辑处理函数、指定路由。以新增任务为例：

①在`api/views.py`实现逻辑：

```python
def create(request):
    if request.method=="POST":
        # 获取传入的基本信息
        title=request.POST.get("title")
        content = request.POST.get('content')
        endTime = request.POST.get('endTime')
        try:
            # 检查之前是否有计划与新建计划标题相同
            cnt = ItemInfo.objects.filter(title=title).count()
            if cnt != 0:
                return JsonResponse({'message': 'fail', 'error': 'title exists'}, status=422)
            if title is None or endTime is None:
                return JsonResponse({'message': 'fail', 'error': 'message missing'}, status=400)
            ItemInfo.objects.create(title=title,content=content,status=0, createTime=datetime.now(),endTime=endTime)
            return JsonResponse({'message': 'success'}, status=200)
        except Exception as e:
            return JsonResponse({'message': 'fail', 'error': str(e)}, status=400)
    else:
        return JsonResponse({'message': 'fail', 'error': "请求方式错误！"}, status=400)
```

HTTP八大请求详情可见 [HTTP八大请求](https://buaa-goodbro2021.github.io/SE-Labs/docs/else/res/httprequest/)，常用GET和POST。

- GET：用于获取资源，请求中不应该包含数据体。
- POST：用于提交数据，数据被包含在请求体中，处理该请求服务器可能会建立或更新资源。

②在`toDoList/urls.py`新增路由：

```python
from django.contrib import admin
from django.urls import path

import api.views

urlpatterns = [
    path('api/create/', api.views.create),#创建 任务
]
```

同理可在`api/views.py`实现其他功能，代码如下：

```python
# 删除计划
def delete(request):
    # 获取基础信息
    data = json.loads(request.body)
    title = data.get('title')
    try:
        # 检查是否有该条计划
        cnt = ItemInfo.objects.filter(title=title).count()
        if cnt == 0:
            return JsonResponse({'message': 'fail', 'error': 'title is not exist'}, status=422)
        ItemInfo.objects.get(title=title).delete()
        return JsonResponse({'message': 'success'}, status=200)
    except Exception as e:
        return JsonResponse({'message': 'fail', 'error': str(e)}, status=400)
# 修改计划
def update(request):
    data = json.loads(request.body)
    title = data.get('title')
    content = data.get('content')
    status = data.get('status')
    endTime = data.get('endTime')

    obj = ItemInfo.objects.get(title=title)
    if obj is None:
        return JsonResponse({'message': 'fail', 'error': 'title is not exist'}, status=422)
    if content is not None:
        obj.content = content
    if endTime is not None:
        obj.endTime = endTime
    if status is not None:
        if status == '未完成':
            obj.status = 0
        elif status == '已完成':
            obj.status = 1
    obj.save()
    return JsonResponse({'message': 'success'}, status=200)

def searchByTitle(request):
    data = json.loads(request.body)
    title = data.get('title')
    obj = ItemInfo.objects.get(title=title)
    if obj is None:
        return JsonResponse({'message': 'fail', 'error': 'title is not exist'}, status=422)
    return JsonResponse({
        'title': obj.title,
        'content': obj.content,
        'status': '未完成' if obj.status == 0 else '已完成',
        'createTime': obj.createTime.strftime("%Y-%m-%d %H:%M:%S"),     # 人为设定返回的日期格式
        'endTime': obj.endTime
    }, status=200)

def getJson(answer):
    result = []
    for item in answer:
        # answer 是一个 QuerySet 对象，需要遍历把每一项取出来，然后再得到有用信息
        title = item.title
        endTime = item.endTime
        # 每一条信息形成字典后加入到 result 中
        info = {
            'title': title,
            'endTime': endTime
        }
        result.append(info)
    return JsonResponse({'message': 'success', 'result': result}, status=200)


# 根据日期查找
def searchByDate(request, year, month, day):
    if request.method != 'GET':
        return JsonResponse({'message': 'fail', 'error': 'invalid request'}, status=400)

    time = date(year, month, day)
    # 将内容首先按照 endTime 升序排列以后筛选 endTime <= time 的内容
    answer = ItemInfo.objects.order_by('endTime').filter(endTime__lte=time)
    return getJson(answer)


def getAll(request):
    if request.method != 'GET':
        return JsonResponse({'message': 'fail', 'error': 'invalid request'}, status=400)

    answer = ItemInfo.objects.order_by('endTime')
    return getJson(answer)

```

在`toDoList/urls.py`新增路由为：

```python
urlpatterns = [
    path('api/delete/', api.views.delete),#删除任务
    path('api/update/', api.views.update),#更新任务信息
    path('api/titleGet/', api.views.searchByTitle),#通过标题搜索任务
    path('api/dateGet/<int:year>/<int:month>/<int:day>', api.views.searchByDate),#通过日期搜索任务
    path('api/all/', api.views.getAll)#获取所有任务
]
```

### 运行项目、测试逻辑

#### 运行项目

运行项目的指令为：

```python
python manage.py runserver 0.0.0.0:8000
```

运行成功后，将提示运行在 http://127.0.0.1:8000/，浏览器打开即可。

#### 测试逻辑

前后端分离开发时，后端的测试，需要借助工具模拟前端请求，向后端相应的路由发送请求，并查看响应数据。测试工具有apifox、postman。

下面以apifox为例，下载地址：https://apifox.com/

下面以新增任务为例。运行项目后，新增任务的详细信息如下：

- 路由：http://127.0.0.1:8000/api/create/

- 请求数据：任务标题`title`，任务内容`content`，任务截止时间`endTime`

- 响应数据：JSON格式，错误信息`message` 和错误类型`error`

- 响应样例：

    ```json
    {
        'message': 'fail',
        'error': "请求方式错误！"
    }
    ```

apifox使用方法如下：

![pPM6C6J.png](https://s1.ax1x.com/2023/08/14/pPM6C6J.png)

同理可测试其他路由。



最后推荐教程如下：

https://super-buaa-2021.github.io/Djangobook/
https://www.liujiangblog.com/course/django/2
https://www.bilibili.com/video/BV1b5411c7Sa/





