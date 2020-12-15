'''
20.7 QuerySet 操作
对象关系映射 (ORM)
Manager、QuerySet、Model
Manager：
定义表级方法（表级方法就是影响一条或多条记录的方法），我们可以以models.Manager为父类，定义自己的manager，增加表级方法；
class PersonManager(models.Manager):

    def first_names(self, last_name):
        cursor = connection.cursor()
        cursor.execute("""SELECT DISTINCT first_name FROM people_person WHERE last_name = %s""", [last_name])
        return [row[0] for row in cursor.fetchone()]


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    objects = PersonManager()

# Person.objects.first_names('Lennon')

QuerySet：
Manager类的一些方法会返回QuerySet，QuerySet是一个可遍历结构，包含一个或多个元素，每个元素都是一个Model 实例，它里面的方法也是表级方法，前面说了，Django给我们提供了增加表级方法的途径，那就是自定义manager类，而不是自定义QuerySet类，一般的我们没有自定义QuerySet类的必要；
QuerySet是延迟获取的，只有当用到这个QuerySet时，才会查询数据库求值。另外，查询到的QuerySet又是缓存的，当再次使用同一个QuerySet时，并不会再查询数据库，而是直接从缓存获取（不过，有一些特殊情况）
Model：
从django.db.models模块中继承来，我们定义表的model时，就是继承它，它的功能很强大，通过自定义model的instance可以获取外键实体等

ORM被认为效率不高，比原始的SQL要慢
要有效的使用ORM，意味着需要多少要明白它是如何查询数据库的。
20.7.1 基本操作
数据库接口相关的接口（QuerySet API)
上一节，我们已经学习了，模型的创建和查询
从数据库中查询出来的结果一般是一个集合，这个集合叫做 QuerySet。

from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    click_num = models.IntegerField(default=0)

    def __str__(self):
        return self.title
class Meta:
       verbose_name = '博客模块'
       verbose_name_plural = verbose_name
   Db_table = 'bloginfo'


class Meta介绍
models 中经常会出现一个 class Meta 的内部类，那它的作用是什么呢？
db_table 属性：自定义数据表的名称，是可选属性。默认数据表的命名规则为： 应用名_类名。

　　例如：你创建了一个名为 blog 的应用时，且你为这个应用创建了一个 User 类 的models时，

　　　　   这时django会将会为你创建一张名为 blog_User 的数据表。



verbose_name 属性：自定义一个易于理解的名称，到时候后台会展示，

　　　　verbose_name = '地址', 用来标志这个表时用来存放地址信息的



 verbose_name_plural 属性：
　　　　如果此项没有设置，Django 会使用 verbose_name + "s"来表示。
1.QuerySet 创建对象的方法
objects
语句Book.objects.all()中，objects是一个特殊的属性，需要通过它查询数据库。
模块manager是一个对象，Django模块通过它进行数据库查询。 每个Django模块至少有一个manager，你可以创建自定义manager以定制数据库访问。
from apps.user.models import Blog
print(type(Blog.objects))
<class 'django.db.models.manager.Manager'>

python manage.py shell

>>> from blog.models import Blog

总之，一共有四种方法
# 方法 1
blog_obj = Blog.objects.create(title="python异常", content="讲解python异常处理")

# 方法 2
blog_obj = Blog(title="python异常", content="讲解python异常处理")
blog_obj.save()

# 方法 3
blog_obj = Blog()
blog_obj.title="python异常"
blog_obj.content="讲解python异常处理"
blog_obj.save()

# 方法 4，首先尝试获取，不存在就创建，可以防止重复
(blog_obj, status) = Blog.objects.get_or_create(title="python异常", content="讲解python异常处理")
# 返回值(object, True/False)


注意：前三种方法返回的都是对应的 object，最后一种方法返回的是一个元组，(object, True/False)，创建时返回 True, 已经存在时返回 False

2. 删除符合条件的结果
得到满足条件的结果，然后 delete 就可以(危险操作，正式场合操作务必谨慎)，比如：
Blog.objects.filter(title__contains="python").delete() # 删除 名称中包含 "python"的所有博客文章

如果写成
blog_obj = Blog.objects.filter(title__contains="python")
blog_obj.delete()
效果也是一样的，Django实际只执行一条 SQL 语句。

3.修改，更新某个内容
3.1 修改单个
blog_obj = Blog.objects.get(title="python")
blog_obj.title="Python"
blog_obj.save()  # 最后不要忘了保存！！

3.2 批量修改
Blog.objects.filter(title__contains="python").update(name='Python') # 名称中包含 "python"的所有对象 都改成 Python


单个 object 更新，适合于 .get(), get_or_create(), update_or_create() 等得到的 obj，和新建很类似。

4. 查看，获取对象的方法

Blog.objects.all() # 查询所有博客
Blog.objects.all()[:10] 切片操作，获取10个，不支持负索引，切片可以节约内存，不支持负索引
Blog.objects.get(title="python异常") # 名称为 python异常 的一条，多条会报错
get是用来获取一个对象的，如果需要获取满足条件的一些，就要用到filter

Blog.objects.filter(title="python异常") # 等于Blog.objects.filter(title__exact="python异常") 名称严格等于 "python异常" 的文章
Blog.objects.filter(title__iexact="python异常") # 名称为 python异常 但是不区分大小写，可以找到 python异常, python异常, python异常，这些都符合条件

Blog.objects.filter(title__contains="python异常") # 名称中包含 "python异常"的
Blog.objects.filter(title__icontains="python异常") #名称中包含 "python异常"，且python异常不区分大小写

Blog.objects.filter(title__regex="^python异常") # 正则表达式查询
Blog.objects.filter(title__iregex="^python异常")# 正则表达式不区分大小写

# filter是找出满足条件的，当然也有排除符合某条件的
Blog.objects.exclude(title__contains="python") # 排除包含 python 的Blog对象
Blog.objects.filter(title__contains="python异常").exclude(click_num=0) # 找出名称含有python异常, 但是排除点击数是0的

5. 对结果根据某个字段排序
Blog.objects.all().order_by('click_num')
Blog.objects.all().order_by('-click_num') # 在 column click_num 前加一个负号，可以实现倒序

6. 可对查询集迭代，遍历
blog_queryset = Blog.objects.all()
for b in blog_queryset:
    print(b.title)

7. 链式查询
Blog.objects.filter(title__contains="python").filter(click_num__gte=88)
Blog.objects.filter(title__contains="python").exclude(click_num=88)

# 找出名称含有python异常, 但是排除点击数是0的
Blog.objects.filter(title__contains="python异常").exclude(click_num=0)

8. 查询集切片不支持负索引
Blog.objects.all()[:10] 切片操作，前10条
Blog.objects.all()[-10:] 会报错！！！

# 1. 使用 reverse() 解决
Blog.objects.all().reverse()[:2] # 最后两条
Blog.objects.all().reverse()[0] # 最后一条

# 2. 使用 order_by，在栏目名（column id）前加一个负号
Blog.objects.order_by('-id')[:20] # id最大的20条

应用：分页

9. 对查询集进行去重
一般的情况下，QuerySet 中不会出来重复的，重复是很罕见的，但是当跨越多张表进行检索后，结果并到一起，可能会出来重复的值
all_tag = Tag.objects.filter(taginfo__name='django')
# 去重方法
all_tag = all_tag.distinct()


注意：
(1). 如果只是检查 Blog 中是否有对象，应该用 Blog.objects.all().exists()
(2). QuerySet 支持切片 Blog.objects.all()[:10] 取出10条，可以节省内存
(3). 用 len(Blog.objects.all()) 可以得到Entry的数量，但是推荐用 Blog.objects.count()来查询数量，后者用的是SQL：SELECT COUNT(*)
(4). list(es) 可以强行将 QuerySet 变成 列表
'''