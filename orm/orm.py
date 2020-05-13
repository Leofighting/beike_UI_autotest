# -*- coding:utf-8 -*-
__author__ = "leo"

from orm.field import Field
from utils.my_database import create_pool


class ModelMetaClass(type):
    """定义元类，控制 model 对象的创建"""

    def __new__(cls, table_name, bases, attrs):
        """
        :param table_name: 数据库表名
        :param bases: 父类的元组
        :param attrs: 类的属性方法与值组成的键值对
        """
        if table_name == "Model":
            return super().__new__(cls, table_name, bases, attrs)

        mappings = dict()

        for k, v in attrs.items():
            # 保存类属性与列的映射关系到 mappings 字典中
            if isinstance(v, Field):
                mappings[k] = v

        for k in mappings.keys():
            # 将类的属性移除，使得定义的类字段不污染 User 的字段
            attrs.pop(k)

        attrs["__table__"] = table_name.lower()
        attrs["__mappings__"] = mappings
        return super().__new__(cls, table_name, bases, attrs)


class Model(dict, metaclass=ModelMetaClass):
    """数据库模型基类"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def insert(self, column_list, param_list):
        """插入数据"""
        fields = []
        for k, v in self.__mappings__.items():
            fields.append(k)
        for key in column_list:
            if key not in fields:
                raise RuntimeError("此字段没有发现~~")
        # 检查参数的合法性
        args = self.__check_params(param_list)

        sql = "insert into {} ({}) values ({})".format(self.__table__, ",".join(column_list), ",".join(args))

        res = self.__do_execute(sql)
        print(res)

    @staticmethod
    def __check_params(param_list):
        """检验参数合法性，防止 SQL 注入"""
        args = []
        for param in param_list:
            if "\"" in param:
                param = param.replace("\"", "\\\"")
            param = "\"" + param + "\""
            args.append(param)

        return args

    @staticmethod
    def __do_execute(sql):
        """执行 sql 语句"""
        conn = create_pool()
        cur = conn.cursor()

        if "select" in sql:
            cur.execute(sql)
            result = cur.fetchall()
        else:
            result = cur.execute(sql)
        conn.commit()
        cur.close()
        return result

    def select(self, column_list, where_list):
        """查找数据"""
        args = []
        fields = []

        for k, v in self.__mappings__.items():
            fields.append(k)

        for key in where_list:
            args.append(key)

        for key in column_list:
            if key not in fields:
                raise RuntimeError("此字段不存在~~")

        sql = "select {} from {} where {}".format(','.join(column_list), self.__table__, " and ".join(args))
        result = self.__do_execute(sql)
        return result

    def update(self, set_column_list, where_list):
        """更新数据"""
        args = []
        fields = []

        for key in set_column_list:
            fields.append(key)

        for key in where_list:
            args.append(key)

        for key in set_column_list:
            if key not in fields:
                raise RuntimeError("此字段不存在~~")

        sql = "update {} set {} where {}".format(self.__table__, ",".join(set_column_list), " and ".join(args))
        result = self.__do_execute(sql)
        return result

    def delete(self, where_list):
        """删除数据"""
        args = []
        for key in where_list:
            args.append(key)

        sql = "delete from {} where {}".format(self.__table__, " and ".join(args))
        result = self.__do_execute(sql)

        return result
