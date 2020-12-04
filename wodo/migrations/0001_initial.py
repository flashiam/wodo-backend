# Generated by Django 3.1.2 on 2020-10-29 04:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='appUser',
            fields=[
                ('userID', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True, verbose_name='UserID')),
                ('username', models.CharField(blank=True, max_length=100, unique=True)),
                ('name', models.CharField(blank=True, max_length=200)),
                ('contact', models.BigIntegerField(blank=True, default='9090000000', max_length=200, unique=True)),
                ('profile', models.ImageField(blank=True, null=True, upload_to='profile', verbose_name='Profile Image')),
                ('email', models.CharField(blank=True, max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='workers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workerid', models.CharField(max_length=20, unique=True)),
                ('agreeNo', models.BigIntegerField(null=True, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='prof')),
                ('skills', jsonfield.fields.JSONField(null=True)),
                ('exp', jsonfield.fields.JSONField(default=int, null=True)),
                ('dateBirth', models.DateField()),
                ('lang', jsonfield.fields.JSONField(null=True)),
                ('wages', models.FloatField(null=True)),
                ('avgWork', models.FloatField(null=True)),
                ('distance', models.FloatField()),
                ('offDay', models.CharField(default='Sunday', max_length=20)),
                ('idType', models.CharField(default='Aadhar Card', max_length=20)),
                ('idValue', models.CharField(default='000000000', max_length=50)),
                ('active', models.BooleanField(default=False)),
                ('gend', models.CharField(max_length=10)),
                ('contact', models.BigIntegerField()),
                ('strtime', models.TimeField()),
                ('endtime', models.TimeField()),
                ('add', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('coor', jsonfield.fields.JSONField(default=float)),
                ('ageid', models.CharField(max_length=20)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='workRating',
            fields=[
                ('ratingID', models.IntegerField(auto_created=True, default=0, primary_key=True, serialize=False, unique=True, verbose_name='RateID')),
                ('rat_1', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('rat_2', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('rat_3', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('rat_4', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('comment', models.TextField(null=True)),
                ('hiredOn', models.DateField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('userR', models.ForeignKey(default='specsoid', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, to_field='username', verbose_name='User')),
                ('workerIDR', models.ForeignKey(default='test001', on_delete=django.db.models.deletion.SET_DEFAULT, to='wodo.workers', to_field='workerid', verbose_name='workerID')),
            ],
        ),
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0.0)),
                ('orderID', models.CharField(max_length=100, unique=True)),
                ('transID', models.CharField(max_length=200, unique=True)),
                ('transType', models.CharField(choices=[('DEBIT', 'DEBIT'), ('CREDIT', 'CREDIT')], max_length=20)),
                ('purpose', models.CharField(choices=[('HIRING', 'HIRING'), ('REFUND', 'REFUND'), ('ADD MONEY', 'ADD MONEY'), ('REFERRAL', 'REFERRAL'), ('NEW USER', 'NEW USER'), ('TRANSFER', 'TRANSFER')], max_length=30)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('userT', models.ForeignKey(default='specsoid', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, to_field='username', verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='saved',
            fields=[
                ('savedID', models.IntegerField(auto_created=True, default=0, primary_key=True, serialize=False, unique=True, verbose_name='SaveID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('userS', models.ForeignKey(default='specsoid', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, to_field='username', verbose_name='User')),
                ('workerIDS', models.ForeignKey(default='test001', on_delete=django.db.models.deletion.SET_DEFAULT, to='wodo.workers', to_field='workerid', verbose_name='workerID')),
            ],
        ),
        migrations.CreateModel(
            name='reportWorker',
            fields=[
                ('reportID', models.IntegerField(auto_created=True, default=0, primary_key=True, serialize=False, unique=True, verbose_name='ReportID')),
                ('reportType', models.CharField(choices=[('DUTY DENIAL', 'DUTY DENIAL'), ('MISBEHAVIOUR', 'MISBEHAVIOUR'), ('TIME DELAY', 'TIME DELAY'), ('NOT RESPONDING', 'NOT RESPONDING'), ('DEMANDING MORE WAGES', 'DEMANDING MORE WAGES'), ('COMMITMENT ISSUE', 'COMMITMENT ISSUE'), ('MESSED UP WORK', 'MESSED UP WORK'), ('NON CONSENTUAL WORK', 'NON CONSENTUAL WORK')], max_length=200)),
                ('description', models.TextField()),
                ('actionNeed', models.CharField(choices=[('COMPLETE REFUND', 'COMPLETE REFUND'), ('PARTIAL REFUND', 'PARTIAL REFUND'), ('REPLACEMENT', 'REPLACEMENT'), ('NO ACTION REQUIRED', 'NO ACTION REQUIRED')], max_length=200)),
                ('status', models.CharField(choices=[('DENIED', 'DENIED'), ('UNDER REVIEW', 'UNDER REVIEW'), ('COMPLETED', 'COMPLETED')], max_length=100)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('userRe', models.ForeignKey(default='specsoid', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, to_field='username', verbose_name='User')),
                ('workerIDW', models.ForeignKey(default='test001', on_delete=django.db.models.deletion.SET_DEFAULT, to='wodo.workers', to_field='workerid', verbose_name='workerID')),
            ],
        ),
        migrations.CreateModel(
            name='hired',
            fields=[
                ('hiredID', models.IntegerField(auto_created=True, default=0, primary_key=True, serialize=False, unique=True, verbose_name='HireID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('orderid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wodo.transaction', to_field='orderID', verbose_name='orderID')),
                ('userH', models.ForeignKey(default='specsoid', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, to_field='username', verbose_name='User')),
                ('workerIDH', models.ForeignKey(default='test001', on_delete=django.db.models.deletion.SET_DEFAULT, to='wodo.workers', to_field='workerid', verbose_name='workerID')),
            ],
        ),
        migrations.CreateModel(
            name='filterCache',
            fields=[
                ('CacheID', models.IntegerField(auto_created=True, default=0, primary_key=True, serialize=False, unique=True, verbose_name='CacheID')),
                ('location', jsonfield.fields.JSONField(null=True)),
                ('wages', models.IntegerField()),
                ('jobs', jsonfield.fields.JSONField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('userF', models.ForeignKey(default='specsoid', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, to_field='username', verbose_name='User')),
            ],
        ),
    ]
