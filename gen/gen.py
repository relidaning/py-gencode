# !/usr/bin/python
# -*- coding: utf-8 -*-
# coding="utf-8"
import os
import sys
from functools import reduce

import jinja2 as jj

class Generator(object):

    def __init__(self, db, database, package, module, table, saveat):

        self.database = database

        #生成时需要参数
        self.package = package
        self.module = module
        self.table = table
        self.Domain = table.title().replace('_', '')
        self.domain = reduce(lambda x,y: x+y.title(), table.split('_'))
        self.saveat = saveat

        basePath = ''
        if getattr(sys, 'frozen', False):
            basePath = sys._MEIPASS
        else:
            basePath = os.path.abspath(".")

        templatesPath = basePath + '\\gen\\templates'
        print('templatesPath:', templatesPath)

        self.env = jj.Environment(
            loader=jj.FileSystemLoader(templatesPath)
        )

        #业务信息
        self.getBusiness(db)

    def getBusiness(self, db):

        tableName = db.executeSql(' SELECT TABLE_COMMENT FROM information_schema.`TABLES` WHERE TABLE_SCHEMA = \''+self.database+
                      '\' and TABLE_NAME = \''+self.table+'\' ')[0][0]
        results = db.executeSql(' SELECT column_name, data_type, column_comment, column_key FROM information_schema.COLUMNS WHERE table_name = "'+self.table+'" AND table_schema = "'+self.database+'" ')
        cols = []   #字段列表
        primaryKey = ''
        primaryKeyType = ''
        for result in results:
            col = result[0].lower()
            if(result[1] in ['int', 'bigint', 'tinyint', 'integer']):
                colType = 'int'
            elif(result[1] in ['char', 'varchar']):
                colType = 'String'
            elif (result[1] in ['date', 'datetime', 'time', 'timestamp']):
                colType = 'Date'
            elif (result[1] in ['decimal', 'double', 'float']):
                colType = 'Float'
            propName = result[2]
            key = result[3]
            d = {'colName':col, 'colType':colType, 'prop':reduce(lambda x,y: x+y.title(), col.split('_')), 'propName':propName}
            cols.append(d)
            if key=='PRI':
                primaryKey = col
                primaryKeyProp = reduce(lambda x,y: x+y.title(), col.split('_'))
                primaryKeyType = colType
                colType = colType

        self.business = {"package": self.package,
                         "module": self.module,
                         "table": self.table,
                         "Domain": self.Domain,
                         "domain": self.domain,
                         "tableName": tableName,
                         "primaryKey": primaryKey,
                         "PrimaryKey": primaryKey.capitalize(),
                         "primaryKeyProp": primaryKeyProp,
                         "PrimaryKeyProp": primaryKeyProp.title(),
                         "primaryKeyType": primaryKeyType,
                         "cols": cols}
    def businessPath(self):
        return self.saveat+os.sep+'genCode'+os.sep+'java'+os.sep+self.module+os.sep

    def genController(self):
        print('genController')
        template = self.env.get_template('controller.java')
        tar = self.jinjaRender(template)
        self.createDirIfNotExists(self.businessPath()+'controller')
        tarFile = open(self.businessPath()+'controller'+os.sep+self.table.title().replace('_', '') + 'Controller.java', 'w')
        tarFile.write(tar)

    def genDomain(self):
        print('genDomain')
        template = self.env.get_template('domain.java')
        tar = self.jinjaRender(template)
        self.createDirIfNotExists(self.businessPath()+ 'domain')
        tarFile = open(self.businessPath()+'domain'+ os.sep + self.table.title().replace('_', '') + '.java', 'w')
        tarFile.write(tar)

    def genMapperJava(self):
        print('genMapper')
        template = self.env.get_template('mapper.java')
        tar = self.jinjaRender(template)
        self.createDirIfNotExists(self.businessPath()+ 'mapper')
        tarFile = open(self.businessPath()+'mapper' + os.sep + self.table.title().replace('_', '') + 'Mapper.java', 'w')
        tarFile.write(tar)

    def genMapperXml(self):
        print('genMapperXml')
        template = self.env.get_template('mapper.xml')
        tar = self.jinjaRender(template)
        self.createDirIfNotExists(self.saveat+os.sep+'genCode'+os.sep+'resources'+os.sep+self.module)
        tarFile = open(self.saveat+os.sep+'genCode'+os.sep+'resources'+os.sep+self.module+os.sep + self.table.title().replace('_', '') + 'Mapper.xml', 'w')
        tarFile.write(tar)

    def genService(self):
        print('genService')
        template = self.env.get_template('service.java')
        tar = self.jinjaRender(template)
        self.createDirIfNotExists(self.businessPath()+'service')
        tarFile = open(self.businessPath()+'service'+ os.sep + 'I' +self.table.title().replace('_', '') + 'Service.java', 'w')
        tarFile.write(tar)

    def genServiceImpl(self):
        print('genServiceImpl')
        template = self.env.get_template('serviceImpl.java')
        tar = self.jinjaRender(template)
        self.createDirIfNotExists(self.businessPath()+'service'+os.sep+'impl')
        tarFile = open(self.businessPath()+'service'+os.sep+'impl'+ os.sep + self.table.title().replace('_', '') + 'ServiceImpl.java', 'w')
        tarFile.write(tar)

    def jinjaRender(self, template):
        return template.render(self.business)

    def createDirIfNotExists(self, dir):
        if not os.path.exists(dir):
            os.makedirs(dir)

if __name__ == '__main__':
    # gen = Generator('com.shakeit', 'gencode', 's_user', 'e:')
    # gen.genController()

    # if not os.path.exists('e:/genCode/java/controller'):
    #     os.makedirs('e:\\genCode/java/controller')

    pass