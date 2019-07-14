# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Person(models.Model):
    user_name = models.CharField(max_length=300,null=False)
    user_password = models.CharField(max_length=50,null=False)
    email = models.EmailField(null=True)
    from_language = models.CharField(max_length=20)
    to_language = models.CharField(max_length=20)
    register_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.user_name

class Word(models.Model):
    text = models.CharField(max_length=1000)
    meaning = models.CharField(max_length=1000, null=True)
    description = models.CharField(max_length=10000, null=True)
    value = models.IntegerField()
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ('value', )
    
    def __str__(self):
        return "%s -> %d" % (self.text, self.value)

class List(models.Model):
    name = models.CharField(max_length=500)
    words = models.ManyToManyField(Word)

    def __str__(self):
        return self.name