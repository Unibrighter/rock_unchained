# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
	title=models.CharField(max_length=100)
	category=models.CharField(max_length=50, blank=True)
	
