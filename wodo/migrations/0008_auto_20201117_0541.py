# Generated by Django 3.1.2 on 2020-11-17 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wodo', '0007_auto_20201110_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filtercache',
            name='userF',
            field=models.ForeignKey(default='specsoid', on_delete=django.db.models.deletion.SET_DEFAULT, to='wodo.appuser', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='hired',
            name='date',
            field=models.DateField(default='2020-11-17'),
        ),
    ]
