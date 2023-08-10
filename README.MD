
### 路由

http://127.0.0.1:8081/api/v1/demo/demo/1/
http://127.0.0.1:8081/api/v1/demo/demo
http://127.0.0.1:8081/api/v1/ss_user/ss_user/2/

### 部分目录说明

- drf_backend
  - apps 应用
    - demo 视图关系
    - ss_suer用户
  - com 说明视图.png





### 一些记录

Django ORM（对象关系映射）提供了丰富的查询和操作数据库的方法。以下是一些常用的 Django ORM 方法：

查询集方法（QuerySet Methods）： 查询集是 Django ORM 中的核心概念，用于查询数据库并返回结果集。

以下是一些常用的查询集方法：

filter(**kwargs)：根据条件过滤结果集。
exclude(**kwargs)：排除满足条件的结果。
get(**kwargs)：获取单个对象，如果不存在或满足条件的对象不唯一，会引发异常。
all()：返回所有对象。
order_by(*fields)：按指定字段排序。
annotate(*args, **kwargs)：对查询结果进行注释（添加额外的字段）。
values(*fields)：返回结果集中指定字段的值。
distinct()：返回去重后的结果集。
count()：返回结果集中的对象数量。
first()：返回结果集中的第一个对象。
last()：返回结果集中的最后一个对象。
聚合方法（Aggregation Methods）： 用于对结果集进行聚合操作，如求和、平均值等。

aggregate(*args, **kwargs)：进行聚合操作，返回聚合结果。
连接方法（Join Methods）： 用于在查询中进行表连接操作。

select_related(*fields)：执行 SQL 中的 INNER JOIN 操作，提前查询相关外键关联的数据。
prefetch_related(*lookups)：执行 SQL 中的 LEFT OUTER JOIN 操作，预先获取相关联的数据。
修改方法（Modification Methods）： 用于修改数据库中的数据。

create(**kwargs)：创建一个新对象并保存到数据库中。
update(**kwargs)：更新满足条件的对象的字段值。
删除方法（Deletion Methods）： 用于删除数据库中的数据。

delete()：删除满足条件的对象。
日期和时间方法（Date and Time Methods）： 用于处理日期和时间字段。

filter(date_field__year=year)：根据年份过滤结果。
filter(date_field__month=month)：根据月份过滤结果。
filter(date_field__day=day)：根据日期过滤结果。
字符串方法（String Methods）： 用于处理字符串字段。

filter(name__contains='keyword')：筛选包含关键词的结果。
filter(name__startswith='prefix')：筛选以指定前缀开头的结果。
以上只是一些常用的 Django ORM 方法，实际上还有更多功能丰富的方法可供使用。

您可以查阅 Django 官方文档以获取更详细的信息：https://docs.djangoproject.com/en/3.2/topics/db/queries/



### 视图继承关系说明

![视图说明](https://gitee.com/brave_wang/drf_backend/blob/master/drf/com/django%E8%A7%86%E5%9B%BE%E5%85%B3%E7%B3%BB%E5%9B%BE.png)

![继承关系](https://gitee.com/brave_wang/drf_backend/blob/master/drf/com/drf.png)