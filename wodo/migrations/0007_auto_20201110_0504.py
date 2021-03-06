# Generated by Django 3.1.2 on 2020-11-10 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wodo', '0006_auto_20201109_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='hired',
            name='status',
            field=models.CharField(choices=[('DENIED', 'DENIED'), ('UNDER REVIEW', 'UNDER REVIEW'), ('COMPLETED', 'COMPLETED')], default='UPCOMING', max_length=20),
        ),
        migrations.AlterField(
            model_name='hired',
            name='date',
            field=models.DateField(default='2020-11-10'),
        ),
    ]
