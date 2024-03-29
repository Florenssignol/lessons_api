from django.db import models

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    email = models.CharField(max_length=200, null=False)
    password = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255, null=True)
    insert_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

class Subscription(models.Model):
    id = models.AutoField(primary_key=True)
    account_id = models.ForeignKey(
        'Account', 
        on_delete=models.CASCADE,
    )
    subscription_date = models.DateTimeField(auto_now=True)
    status_id = models.ForeignKey(
        'Status', 
        on_delete=models.CASCADE,
    )
    insert_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

class Status(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    insert_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now=False)
    description = models.CharField(max_length=200, null=False)
    subscription_id = models.ForeignKey(
        'Subscription', 
        on_delete=models.CASCADE,
    )
    insert_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    lesson_locked = models.BooleanField()

class Students(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200, null=False)
    last_name = models.CharField(max_length=200, null=False)
    birthdate = models.DateField(auto_now=False)
    email = models.CharField(max_length=200, null=False)
    account_id = models.ForeignKey(
        'Account', 
        on_delete=models.CASCADE,
    )
    lessons = models.ManyToManyField(Lesson)
    insert_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)