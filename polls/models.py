import datetime

from django.db import models
from django.utils import timezone


class Poll(models.Model):
    poll_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    end_pub_date = models.DateTimeField('end_date published')
    poll_description = models.CharField(max_length=200)

    def __str__(self):
        return self.poll_text


class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text
    
