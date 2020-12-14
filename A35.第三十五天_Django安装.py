'''
安装环境 Django
安装虚拟环境
Windows 下：
1、安装虚拟环境
（管理员身份）
 virtualenv  /ˈvɜ:tʃuəl/
国外源：pip install virtualenv
国内豆瓣源：pip install virtualenv -i https://pypi.douban.com/simple/

2、安装虚拟环境管理包
pip install virtualenvwrapper-win

or

pip install virtualenv virtualenvwrapper-win


【可选】Windows下默认虚拟环境是放在用户名下面的Envs中的，与桌面，我的文档，下载等文件夹在一块的。更改方法：计算机，属性，高级系统设置，环境变量，添加WORKON_HOME

Linux/MacOS 下：
virtualenvwrapper 使得virtualenv变得更好用，所以我们一起安装了
1、安装:
# 安装:
(sudo) pip install virtualenv virtualenvwrapper
2、打开 .bashrc 添加

vi .bashrc
写入
export WORKON_HOME=~/Envs
source /usr/local/bin/virtualenvwrapper.sh
VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3

3、source .bashrc  #读入配置文件，立即生效
虚拟环境使用方法：
mkvirtualenv test：创建运行环境test
workon test: 工作在 test 环境 或 从其它环境切换到 test 环境
deactivate: 退出终端环境
rmvirtualenv test：删除运行环境test
创建的环境是独立的，互不干扰，无需sudo权限即可使用 pip 来进行包的管理。

什么是 pip ？
安装某个包
    pip install 包名
卸载某个包
    pip uninstall 包名
把环境中安装的所有包导出到r.txt文件
    pip freeze > r.txt
查看安装的包
    pip list
下载某个包
    pip download 包名

创建项目步骤
生成初始项目
django-admin.py startproject blog

django-admin.py startproject project_name
特别是在 windows 上，如果报错，尝试用 django-admin 代替 django-admin.py 试试

运行服务
Python manage.py runserver
Error: [WinError 10013] 以一种访问权限不允许的方式做了一个访问套接字的尝试。
是8000端口被其他程序占用了，

由于酷狗经常占用8000端口，我们一开酷狗Django就运行不了了，这时我们也可以考虑更改Django运行端口

网页输出 Hello Word

dir()

request
request HttpRequest 对象
Django 每一个view函数的第一个参数都是request，有没想过request里面到底有什么呢？
当一个路由被请示时，Django创建一个包含请求 元数据的 HttpRequest 对象。 然后Django调入合适的视图，把HttpRequest 作为视图函数的第一个参数 传入。
每个视图要负责返回一个 HttpResponse 对象。

那这个参数是什么类？有什么属性，方法？
['COOKIES', 'FILES', 'GET', 'META', 'POST', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
'__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
 '__subclasshook__', '__weakref__', '_encoding', '_get_post', '_get_raw_host', '_get_scheme', '_initialize_handlers', '_load_post_and_files', '_mark_post_parse_error', '_messages', '
_post_parse_error', '_read_started', '_set_post', '_stream', '_upload_handlers', 'body', 'build_absolute_uri', 'close', 'content_params', 'content_type', 'csrf_processing_done', 'enc
oding', 'environ', 'get_full_path', 'get_host', 'get_port', 'get_raw_uri', 'get_signed_cookie', 'is_ajax', 'is_secure', 'method', 'parse_file_upload', 'path', 'path_info', 'read', 'r
eadline', 'readlines', 'resolver_match', 'scheme', 'session', 'upload_handlers', 'user', 'xreadlines']


创建应用app
一般一个项目有多个app, 当然通用的app也可以在多个项目中使用。
与项目名类似 app name 也需要为合法的 Python 包名，如 blog，news, aboutus 等都是合法的 app 名称。
python manage.py startapp app_name

激活应用：


路由层版本
1.X用的是url
2.X、3.X用的是path

url第一个参数是一个正则表达式
而path第一个参数不支持正则表达式 写什么就匹配什么
如果你觉得path不好用 2.x、3.x给你提供了一个跟url一样的功能
re_path 等价于1.x里面的url功能


修改默认的数据库类型
Django数据库连接默认为SQLite3，打开setting.py可以看到数据库部分的配置如下：

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

即若不修改的话会自动在当前项目下生成文件名为db.sqlite3的SQLite数据库，若想改变数据库连接为MySQL只需修改DABASES部分的配置即可：
修改为mysql：
DATABASES = {
   'default': {
     'ENGINE': 'django.db.backends.mysql',
     'NAME': 'blog',
     'USER': 'root',
     'PASSWORD': 'root',
     'HOST': '127.0.0.1',
     'PORT': 3306,
    }
}

安装mysql模块
pip install mysqlclient


'''