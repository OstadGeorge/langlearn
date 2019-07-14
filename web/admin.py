# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Person, Word, List

# Register your models here.
admin.site.register(Person)
admin.site.register(Word)
admin.site.register(List)
