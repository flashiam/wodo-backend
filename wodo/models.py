# Create your models here.
from django.db import models
from datetime import date

# Create your models here.
from jsonfield import JSONField
from django.contrib.auth.models import User

today = date.today()

DENIALS= (
    ("NOT SATISFACTORY", "NOT SATISFACTORY"),
    ("WORKER DENIED", "WORKER DENIED")
)

SLOTS = (
    ("MORNING", "MORNING"),
    ("EVENING", "EVENING")
)

STAT = (
    ("UPCOMING", "UPCOMING"),
    ("ONGOING", "ONGOING"),
    ("COMPLETED", "COMPLETED")
)

TRANS_TYPE = (

    ("DEBIT", "DEBIT"),
    ("CREDIT", "CREDIT"),
)
PURPOSE = (
    ("HIRING", "HIRING"),
    ("REFUND", "REFUND"),
    ("ADD MONEY", "ADD MONEY"),
    ("REFERRAL", "REFERRAL"),
    ("NEW USER", "NEW USER"),
    ("TRANSFER", "TRANSFER"),
)

RATING = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)

REPORT_TYPE = (
    ("DUTY DENIAL", "DUTY DENIAL"),
    ("MISBEHAVIOUR", "MISBEHAVIOUR"),
    ("TIME DELAY", "TIME DELAY"),
    ("NOT RESPONDING", "NOT RESPONDING"),
    ("DEMANDING MORE WAGES", "DEMANDING MORE WAGES"),
    ("COMMITMENT ISSUE", "COMMITMENT ISSUE"),
    ("MESSED UP WORK", "MESSED UP WORK"),
    ("NON CONSENTUAL WORK", "NON CONSENTUAL WORK"),
)

ACTIONS = (
    ("COMPLETE REFUND", "COMPLETE REFUND"),
    ("PARTIAL REFUND", "PARTIAL REFUND"),
    ("REPLACEMENT", "REPLACEMENT"),
    ("NO ACTION REQUIRED", "NO ACTION REQUIRED"),
)

STATUS = (
    ("DENIED", "DENIED"),
    ("UNDER REVIEW", "UNDER REVIEW"),
    ("COMPLETED", "COMPLETED"),
)

CITY = (
    ("Bhopal", "Bhopal"),
    ("Pune", "Pune"),
    ("Indore", "Indore"),
    ("Bangalore", "Bangalore"),
)

# Create your models here.
class workers(models.Model):

    workerid = models.CharField(max_length=20, unique=True)
    agreeNo = models.BigIntegerField(null=True, unique=True)
    name = models.CharField(max_length=200)
    img =  models.ImageField(upload_to='prof')
    skills = JSONField(null=True)
    exp = JSONField(default=int, null=True)
    dateBirth = models.DateField(auto_now=False)
    lang = JSONField(null=True)
    wages = models.FloatField(null=True)
    avgWork = models.FloatField(null=True)
    distance = models.FloatField()
    offDay = models.CharField(max_length=20, default='Sunday')
    idType = models.CharField(max_length=20, default='Aadhar Card')
    idValue = models.CharField(max_length=50, default='000000000')
    active = models.BooleanField(default=False)
    gend = models.CharField(max_length=10)
    contact = models.BigIntegerField()
    strtime = models.TimeField(auto_now=False, auto_now_add=False)
    endtime = models.TimeField(auto_now=False, auto_now_add=False)
    add = models.TextField()
    city = models.CharField(max_length=100)
    coor = JSONField(default=float)
    ageid = models.CharField(max_length=20)
    verified = models.BooleanField(default=True, max_length=1)
    updated_at = models.DateTimeField(auto_now=True)
    services = models.CharField(max_length=100, null=True)
    wagestype = models.CharField(max_length=50, null=True)

    def __str__(self): # __str__ for Python 3, __unicode__ for Python 2
        return self.workerid

class appUser(models.Model):
    userID = models.AutoField(primary_key=True, auto_created=True, unique=True, verbose_name="UserID")
    username = models.CharField(max_length = 100, blank=True, serialize=True, unique=True)
    name = models.CharField(max_length=200, blank=True, serialize=True)
    contact = models.BigIntegerField(max_length=200, unique=True, default="9090000000", blank=True, serialize=True)
    profile = models.ImageField(verbose_name= "Profile Image", upload_to= "profile", null=True, blank=True, serialize=True)
    email = models.CharField(max_length=200, unique=False, blank=True, serialize=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.userID

class transaction(models.Model):
    userT = models.ForeignKey(appUser, default='shiva12', verbose_name="User", on_delete=models.SET_DEFAULT, to_field="username")
    amount = models.FloatField(null=False, default=0.0)
    orderID = models.CharField(max_length=100, unique=True)
    transID = models.CharField(max_length=200, unique=True)
    transType = models.CharField(max_length=20, choices=TRANS_TYPE)
    purpose = models.CharField(max_length=30, choices=PURPOSE)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self): # __str__ for Python 3, __unicode__ for Python 2
        return self.transID


class hired(models.Model):
    hiredID = models.IntegerField(primary_key=True, auto_created=True, default=0, unique=True, verbose_name="HireID")
    userH = models.ForeignKey(appUser, default='shiva12', verbose_name="User", on_delete=models.SET_DEFAULT, to_field="username")
    workerIDH = models.ForeignKey(workers, default= "BHO1001", on_delete=models.SET_DEFAULT, verbose_name="workerID", to_field="workerid")
    orderid = models.ForeignKey(transaction, on_delete=models.CASCADE, verbose_name="orderID", to_field="orderID")
    date = models.DateField(default=today.strftime("%Y-%m-%d"))
    slot = models.CharField(choices=SLOTS, max_length=20)
    status = models.CharField(choices=STAT, max_length=20, default="UPCOMING")
    extension = models.IntegerField(max_length=2, default=1)
    updated_at = models.DateTimeField(auto_now=True)

    def __int__(self): # __str__ for Python 3, __unicode__ for Python 2
        return self.hiredID


class workRating(models.Model):
    ratingID = models.IntegerField(primary_key=True, auto_created=True, default=0, unique=True, verbose_name="RateID")
    userR = models.ForeignKey(appUser, default='shiva12', verbose_name="User", on_delete=models.SET_DEFAULT, to_field="username")
    workerIDR = models.ForeignKey(workers, default= "BHO1001", on_delete=models.SET_DEFAULT, verbose_name="workerID", to_field="workerid")
    rat_1 = models.IntegerField(null=True, choices=RATING)
    rat_2 = models.IntegerField(null=True, choices=RATING)
    rat_3 = models.IntegerField(null=True, choices=RATING)
    rat_4 = models.IntegerField(null=True, choices=RATING)
    comment = models.TextField(null=True)
    hiredOn = models.DateField(null=False, auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __int__(self): # __str__ for Python 3, __unicode__ for Python 2
        return self.ratingID

class saved(models.Model):
    savedID = models.IntegerField(primary_key=True, auto_created=True, default=0, unique=True, verbose_name="SaveID")
    userS = models.ForeignKey(appUser, default='shiva12', verbose_name="User", on_delete=models.SET_DEFAULT, to_field="username")
    workerIDS = models.ForeignKey(workers, default= "BHO1001", on_delete=models.SET_DEFAULT, verbose_name="workerID", to_field="workerid")
    updated_at = models.DateTimeField(auto_now=True)

    def __int__(self): # __str__ for Python 3, __unicode__ for Python 2
        return self.savedID

class filterCache(models.Model):
    CacheID = models.IntegerField(primary_key=True, auto_created=True, default=0, unique=True, verbose_name="CacheID")
    userF = models.ForeignKey(appUser, default='shiva12', verbose_name="User", on_delete=models.SET_DEFAULT, to_field="userID")
    location = JSONField(null=True)
    wages = models.IntegerField(null=False)
    jobs = JSONField(null=False)
    city = models.TextField(default='Bhopal', choices=CITY)
    add = models.TextField(null=True, max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

    def __int__(self): # __str__ for Python 3, __unicode__ for Python 2
        return self.CacheID

class reportWorker(models.Model):
     reportID =models.IntegerField(primary_key=True, auto_created=True, default=0, unique=True, verbose_name="ReportID")
     userRe = models.ForeignKey(appUser, default='shiva12', verbose_name="User", on_delete=models.SET_DEFAULT, to_field="username")
     workerIDW = models.ForeignKey(workers, default= "BHO1001", on_delete=models.SET_DEFAULT, verbose_name="workerID", to_field="workerid")
     reportType = models.CharField(max_length = 200, choices=REPORT_TYPE)
     description = models.TextField(editable=True)
     actionNeed = models.CharField(max_length=200, choices=ACTIONS)
     status = models.CharField(max_length=100, choices= STATUS)
     updated_at = models.DateTimeField(auto_now=True)
     
     def __int__(self): # __str__ for Python 3, __unicode__ for Python 2
        return self.reportID

class dutyDenials(models.Model):
    denyID = models.IntegerField(primary_key=True, auto_created=True, default=0, unique=True, verbose_name="denialID")
    worker = models.ForeignKey(workers, default="BHO1001", on_delete=models.SET_DEFAULT, verbose_name="workerid", to_field="workerid")
    user = models.ForeignKey(appUser, default="shiva12", on_delete=models.SET_DEFAULT, verbose_name="username", to_field="username")
    transid = models.ForeignKey(transaction, on_delete=models.CASCADE, verbose_name="transID", to_field="transID")
    reason = models.CharField(max_length = 100, null=True, choices=DENIALS)
    updated_at = models.DateTimeField(auto_now=True, auto_created=True)

    def __int__(self): # __str__ for Python 3, __unicode__ for Python 2
        return self.denyID

class workerCalls(models.Model):
    callID = models.IntegerField(primary_key=True, auto_created=True, default=0, unique=True, verbose_name="callID")
    workerid = models.ForeignKey(workers, default="BHO1001", on_delete=models.SET_DEFAULT, verbose_name="WorkerID", to_field="workerid")
    userid = models.ForeignKey(appUser, default="BHO1001", on_delete=models.SET_DEFAULT, verbose_name="UserID", to_field="username")
    callSid = models.CharField(max_length=100, null=False, default="123456")
    record = models.URLField(max_length=200, verbose_name="CallRecord", null=True)
    date = models.DateField(auto_now=True, auto_created=True)
    transid = models.CharField(max_length=100, default="HIR00001", null=False)
    updated_at = models.DateTimeField(auto_now=True, auto_created=True)



