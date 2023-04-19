from django.db import models

class publisher(models.Model):
    id=models.AutoField('出版社编号',primary_key=True)
    name=models.IntegerField('出版社名称')
    addr=models.CharField('出版社地址',max_length=64)
class bookInfo(models.Model):
    id=models.AutoField('序号',primary_key=True)
    name=models.CharField('图书名称', max_length=50)
    ISBN=models.CharField("图书编号", max_length=50)
    translator=models.CharField('译者', max_length=50,default='')
    date=models.DateField('出版时间', auto_now=False, auto_now_add=True)
    publisher_id=models.ForeignKey(publisher,on_delete=models.CASCADE)
class author(models.Model):
    id=models.AutoField('序号',primary_key=True)
    name=models.CharField('姓名', max_length=50)
    sex=models.CharField('性别', max_length=50)
    age=models.IntegerField('年龄')
    tel=models.CharField('联系方式', max_length=50)
class user(models.Model):
    id=models.AutoField('序号',primary_key=True)
    username=models.CharField('用户名', max_length=50)
    email=models.CharField('邮箱', max_length=50)
    mobile=models.IntegerField('手机号码')
# Create your models here.
