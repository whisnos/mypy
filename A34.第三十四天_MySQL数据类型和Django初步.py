'''
MySQL数据类型
1、整型
tinyint
smallint
mediumint
int
bigint
2、浮点型(float 和 double)
3、定点数(decimal(m,d))
4、字符串(char,varchar,_text)
5、二进制数据
6、日期时间类型
datetime
7、布尔类型(BOOLEAN)

mysql支持的存储引擎　
　mysql 5.5版本之后默认为innodb存储引擎
　　另外还有mysiam、memory、blackhone
　　#memory，在重启mysql或者重启机器后，表内数据清空
　　#blackhole，往表内插入任何数据，都相当于丢入黑洞，表内永远不存记录
InnoDB 存储引擎
　　支持事务,其设计目标主要面向联机事务处理(OLTP)的应用。其特点是行锁设计、支持外键,并支持类似 Oracle 的非锁定读,即默认读取操作不会产生锁。 从 MySQL 5.5.8 版本开始是默认的存储引擎。

MyISAM 存储引擎
　　不支持事务、表锁设计、支持全文索引,主要面向一些 OLAP 数 据库应用,在 MySQL 5.5.8 版本之前是默认的存储引擎(除 Windows 版本外)。数据库系统 与文件系统一个很大的不同在于对事务的支持,MyISAM 存储引擎是不支持事务的。　


第二十节：Django
1. Django是 python 语言写的一个Web框架包，所以你得知道一些 Python 基础知识。
2.其次你最好有一些做网站的经验，懂一些网页 HTML, CSS, JavaScript 的知识。

Django 是一个由 Python 编写的一个开放源代码的 Web 应用框架。

Django的优点
强大的数据库功能
自带强大的后台功能
优雅的网址
具有模板系统
App 可插拔


MVC 与 MTV模型 - 架构模式
MVC 模型
MVC 模式（Model–view–controller）是软件工程中的一种软件架构模式，把软件系统分为三个基本部分：模型（Model）、视图（View）和控制器（Controller）。

MTV 模型
Django 的 MTV 模式本质上和 MVC 是一样的，也是为了各组件间保持松耦合关系，只是定义上有些许不同，Django 的 MTV 分别是指：
M 表示模型（Model）：
编写程序应有的功能，负责业务对象与数据库的映射(ORM)。
T 表示模板 (Template)：
负责如何把页面(html)展示给用户。
V 表示视图（View）：
负责业务逻辑，并在适当时候调用 Model和 Template。
除了以上三层之外，还需要一个 URL 分发器，它的作用是将一个个 URL 的页面请求分发给不同的 View 处理，View 再调用相应的 Model 和 Template，MTV 的响应模式如下所示：


'''