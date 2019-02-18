操作说明
---

练习sql案例

### 在命令行模式下登录MySQL数据库，使用SQL语句

- 创建留言数据库: blogdb;

```sql
create database if not exists blogdb;
```

- 在blogdb数据库中创建会员表users和博客文章表blog，结构如下

<img src='screenshoot/sql1.png' width='500' />

创建会员表users

```sql
create table users(
	id int unsigned not null auto_increment primary key,
	name varchar(32) not null unique,
	email varchar(100) default null,
	cdate datetime default null
);
```

博客文章(信息)表blog

```sql
create table blog(
	id int unsigned not null auto_increment primary key,
	title varchar(100) not null,
	abstract varchar(200) not null,
	content text not null,
	uid int unsigned default null,
	pcount int unsigned default 0,
	flag tinyint unsigned default 0,
	cdate datetime
);
```

- 在会员表users中添加>=5条的测试数据

```sql
# 批量添加数据 注意这里的 values 和 value
insert into users value(null, 'p1', 'p1@qq.com', '2019-2-1 11:11'), 
(null, 'p2', 'p2@qq.com', '2019-2-2 11:11'),
(null, 'p3', 'p3@qq.com', '2019-2-3 11:11'),
(null, 'p4', 'p4@qq.com', '2019-2-4 11:11'),
(null, 'p5', 'p5@qq.com', '2019-2-5 11:11');
```

- 在blog博文信息表中添加>=10条的测试数据

```sql
# 批量添加数据
insert into blog values(null, 'title1', 'abstract1', 'content1', 1, 10, 0, '2019-2-1 21:11'), 
(null, 'title2', 'abstrac2', 'content2', 2, 20, 0, '2019-2-2 21:11'),
(null, 'title3', 'abstract3', 'content3', 3, 30, 0, '2019-2-3 21:11'),
(null, 'title4', 'abstract4', 'content4', 4, 40, 0, '2019-2-4 21:11'),
(null, 'title5', 'abstract5', 'content5', 5, 50, 0, '2019-2-5 21:11'),
(null, 'title6', 'abstract6', 'content6', 6, 60, 0, '2019-2-6 21:11'),
(null, 'title7', 'abstract7', 'content7', 7, 70, 0, '2019-2-7 21:11'),
(null, 'title8', 'abstract8', 'content8', 8, 80, 0, '2019-2-8 21:11'),
(null, 'title9', 'abstract9', 'content9', 9, 90, 0, '2019-2-9 21:11'),
(null, 'title10', 'abstract10', 'content10', 10, 100, 0, '2019-2-10 21:11');
```

- 最后将blogdb数据库中的信息导出，并以blogdb.sql文件存储，具体查看文件内容