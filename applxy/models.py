from django.db import models

# Create your models here.
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#     def __str__(self):
#         return self.question_text
#
#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.choice_text


class Person(models.Model):
    # f = models.ManyToManyField("self")
    regTime = models.DateTimeField('register time', default=timezone.now)
    name = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.name


class Purchase(models.Model):
    list = models.ForeignKey(Person, on_delete=models.CASCADE)
    time = models.DateTimeField('purchase time', default=timezone.now)
    days = models.IntegerField(default=0)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.time.strftime('%Y-%m-%d %H:%M:%S')


class Product(models.Model):
    price = models.FloatField()
    days = models.IntegerField()

    def __str__(self):
        return "$ %.1f : %d days" % (self.price, self.days)

