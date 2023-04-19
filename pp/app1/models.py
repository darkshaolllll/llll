from django.db import models

class person(models.Model):
    name=models.CharField("姓名",max_length=50,default='')
    age=models.IntegerField("年龄",default=0)
    def __str__(self) -> str:
        return f"姓名:{self.name}, 年龄：{self.age}"
    class Meta:
        db_table="person"
        
# Create your models here.
