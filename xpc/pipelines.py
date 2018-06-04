# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class MysqlPipeline(object):

    def __init__(self):
        self.conn = None
        self.cur = None

    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='xerxes',
            db='xpc',
            charset='utf8mb4'
        )
        self.cur = self.conn.cursor()


    def process_item(self, item, spider):

        if not hasattr(item, 'table_name'):
            return item


        # 防止重复执行是报错ON DUPLICATE KEY UPDATE {}, 已存在则更新, 未存在则插入
        # cols = list(item.keys())
        # value = list(item.values())
        # 字典无序, 两次执行可能出现不对应的情况
        # cols = list(item.keys())
        # value = list(item[k] for k in cols )

        cols, values = zip(*item.items())


        sql = "INSERT INTO `{}` ({}) VALUES ({}) ON DUPLICATE KEY UPDATE {}".format(


            item.table_name,
            ','.join(cols),
            ','.join(['%s'] * len(values)),
            ','.join(['{}=%s'.format(k) for k in cols])
        )
        # 防止sql注入 %的形式
        self.cur.execute(sql, values * 2)
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print(self.cur._last_executed)
        self.conn.commit()
        return item


    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
























