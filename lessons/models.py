from django.db import models

class Account(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    email = models.Charfield(max_length=200, null=False)
    password = models.Charfield(max_length=200, null=False)
    Address = models.Charfiels(max_length=200, null=True)

class Subscription(models.Model):
    id = models.IntegerField(primary_key=True)
    account_id = models.ForeignKey(
        'Account', 
        on_delete=models.CASCADE,
    )
    status = models.CharField(max_lenght=45, null=False)
    subscription_date = models.DateTimeField(auto_now=True)

class Status(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, null=False)

class Lesson(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField(auto_now=False)
    description = models.Charfield(max_length=200, null=False)

class Students(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=200, null=False)
    last_name = models.CharField(max_length=200, null=False)
    birthdate = models.DateField(auto_now=False)
    email = models.Charfield(max_length=200, null=False)