- 关系型数据库：存储一些格式化的数据结构， 这样可以便于表与表之间进行连接操作，即使不是每一个元组都需要所有的字段，但数据库会为每个元组分配所有的字段，但从另一个角度来说它也是关系型数据性能瓶颈的一个因素

- 非关系型数据库：以键值对存储，它的结构不固定，每一个元组可以有不一样的字段，每个元组看根据需要增加一下自己的键值对，这样就不会局限于固定的结构，可以减少一些时间和空间的开销。

MongoDB的结构
- 数据库
- 集合（相当于关系型数据库的表）
- 文档（mongoDB的核心，类似于SQLite数据库的每一行数据）
- 元数据

mogodb中的insert()和save()的区别：
  ● 如果插入的数据带_id字段，如果数据库里已经存在这个_id的数据，insert方法会报错，而save方法会更新数据

```python
function ( obj ){
    if ( obj == null || typeof( obj ) == "undefined" )
        throw "can't save a null";
    if ( typeof( obj ) == "number" || typeof( obj) == "string" )
        throw "can't save a number or string"
    //若没有设置_id，调用insert方法.否则调用update.
    if ( typeof( obj._id ) == "undefined" ){
        obj._id = new ObjectId();
        return this.insert( obj );
    }
    else {
        return this.update( { _id : obj._id } , obj , true );
    }
}
```

> use mydb

使用 use 命令创建数据库

> db

查看当前连接的数据库

> show dbs

查看所有的数据库
