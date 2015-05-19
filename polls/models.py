from django.db import models

import datetime
from django.utils import timezone
# Create your models here.
class Question(models.Model):
    """
    创建Question 类，django会自动db中创建一个表
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """
           可以在数据库操作中显示字符串
        """
        return self.question_text

    def was_published_recently(self):
        """
            自定义方法，是否最近发表
        """
        return self.pub_date >= timezone.now() + datetime.timedelta(days=1)


class Choice(models.Model):
    """
    创建Choice类，django会自动在db中创建一个表：
    """
    question = models.ForeignKey(Question)     # 引入关系 one question, many choice
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """
            可以在数据库操作中显示字符串
        """
        return self.choice_text