# Mysql 数据库的基本操作和数据类型
'''

19.4Mysql 数据库的基本操作和数据类型

19.4.1 MySQL基本操作
库
1增
创建数据库（在磁盘上创建一个对应的文件夹）
create  database db1 charset utf8
create database [IF NOT EXISTS] 库名 [CHARACTER SET xxx]
--xxx为utf8 或者gbk
--[IF NOT EXISTS]此可选项的意思是如果不存在表就创建，如果存在表则不创建。

2.删
删除数据库
drop database [IF EXISTS] 库名;
drop database db1;

3.改
alter database 库名 [CHARACTER SET xxx];    --(一般不需要)
alter  database db1 charset gbk;

4.查
查看数据库
--查看所有数据库
	SHOW DATABASES;
--查看数据库的创建方式
	SHOW CREATE DATABASE 库名;

show databases;
show create database db1;

表
1增
create table t1(id int,name char);
2.删
#删除表
drop table t1;
3.改
#modify是修改的意思
alter table t1 modify name char(6);
#改变name为大写的NAME
alter table t1 change name NAME char(7);
4.查
#查看当前的这张t1表
show create table t1;
#查看所有的表
show tables;
#查看表的详细信息
desc t1;

常用
#查看数据库
show databases;
#查看当前库
show create database db1;
#查看所有的库
select database();
#选择数据库
use 数据库名
#删除数据库
drop database 数据库名
#修改数据库
alter database db1 charset utf8;
'''