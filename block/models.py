# coding: utf-8
from django.contrib.auth.models import User
from django.db import models


class Demolis(models.Model):
    example4char = models.CharField(u"字符序列", max_length=30)
    example4int = models.IntegerField(u"数字序列")
    sex = models.IntegerField(choices=((1, u"男"), (2, u"女")))
    owner = models.ForeignKey(User, verbose_name="作者")

    create_timestamp = models.DateTimeField(auto_now_add=True)
    last_update_timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.example4char


class Tribe(models.Model):
    name = models.CharField(u"板块名称", max_length=30)
    descrip = models.CharField(u"板块描述", max_length=30)
    owner = models.ForeignKey(User, verbose_name="管理员")

    def __unicode__(self):
        return self.name
