from django.db import models
from jsonfield import JSONField
from wodo.models import appUser, workers

class articles(models.Model):
    artid = models.IntegerField(primary_key=True, auto_created=True, default=0, unique=True, verbose_name="ArticleID")
    title = models.CharField(max_length=100, null=False, default="Article Title")
    location = models.FileField(upload_to=None, editable=True, serialize=True, verbose_name="File")
    metaTags = JSONField(verbose_name="Meta_Tags", null=False, serialize=True, editable=True)
    updated_at = models.DateTimeField(auto_created=True, auto_now=True, editable=True)
    
    def __str__(self): # __str__ for Python 3, __unicode__ for Python 2
        return self.title

class custRating(models.Model):
    ratid = models.IntegerField(primary_key=True, auto_created=True, default=0, unique=True, verbose_name="RatingID")
    name = models.ForeignKey(appUser, default="shiva12", on_delete=models.SET_DEFAULT, verbose_name="Name", to_field="username", null=False, serialize=True, unique=True)
    rating = models.FloatField(default=5.0, max_length=10, verbose_name="Ratings", null=True, serialize=True)
    review = models.CharField(max_length=200, verbose_name="Review", default="Very good app", null="True", serialize=True)
    updated_at = models.DateTimeField(auto_created=True, auto_now=True, editable=True)

    def __str__(self): # __str__ for Python 3, __unicode__ for Python 2
        return self.ratid

class workerRating(models.Model):
    ratid = models.IntegerField(primary_key=True, auto_created=True, default=0, unique=True, verbose_name="Review ID")
    name = models.ForeignKey(workers, default="BHO1001", on_delete=models.SET_DEFAULT, verbose_name="Name", to_field="workerid", null=False, serialize=True, unique=True)
    rating = models.FloatField(default=5.0, max_length=10, verbose_name="Ratings", null=True, serialize=True)
    review = models.CharField(max_length=200, verbose_name="Review", default="Very good app", null=True, serialize=True)
    updated_at = models.DateTimeField(auto_created=True, auto_now=True, editable=True)

    def __str__(self): # __str__ for Python 3, __unicode__ for Python 2
        return self.ratid

class homeData(models.Model):
    dataid = models.IntegerField(primary_key=True, auto_created=True, default=0, unique=True, verbose_name="Data ID")
    regWorker = models.IntegerField(default=5000, verbose_name="Registered Workers", serialize=True)
    customer = models.IntegerField(default=350000, verbose_name="Happy Customers", serialize=True)
    connection = models.IntegerField(default=5000, verbose_name="Connections", serialize=True)
    updated_at = models.DateTimeField(auto_created=True, auto_now=True, editable=True)

    def __str__(self):
        return self.dataid

class workWithUs(models.Model):
    ageid = models.IntegerField(primary_key=True, auto_created=True, default=0, unique=True, verbose_name="Agent ID")
    name = models.CharField(null=False, max_length=100, default="User", verbose_name="Name")
    contact = models.IntegerField(null=False, max_length=10, default=9630961847, verbose_name="Contact")
    email = models.CharField(null=False, max_length=100, default="xyz@gmail.com", verbose_name="Email")
    username = models.CharField(null=True, max_length=200, default="shiva12", verbose_name="Token")
    timestamp = models.DateTimeField(auto_created=True, auto_now=True, editable=True)

    def __str__(self):
        return self.name