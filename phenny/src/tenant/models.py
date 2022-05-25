from django.db import models


class Member(models.Model):
    status_list = [
        ('CREATED', 'CREATED'),
        ('COMPLETED', 'COMPLETED')
    ]

    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    status = models.CharField(max_length=30, choices=status_list, default='CREATED')
