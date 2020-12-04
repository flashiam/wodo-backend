# Generated by Django 3.1.2 on 2020-11-03 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wodo', '0003_workers_wagestype'),
    ]

    operations = [
        migrations.AddField(
            model_name='filtercache',
            name='add',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='filtercache',
            name='city',
            field=models.TextField(choices=[('Bhopal', 'Bhopal'), ('Pune', 'Pune'), ('Indore', 'Indore'), ('Bangalore', 'Bangalore')], default='Bhopal'),
        ),
        migrations.AlterField(
            model_name='filtercache',
            name='userF',
            field=models.ForeignKey(default='specsoid', on_delete=django.db.models.deletion.SET_DEFAULT, to='wodo.appuser', to_field='username', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='hired',
            name='userH',
            field=models.ForeignKey(default='specsoid', on_delete=django.db.models.deletion.SET_DEFAULT, to='wodo.appuser', to_field='username', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='reportworker',
            name='userRe',
            field=models.ForeignKey(default='specsoid', on_delete=django.db.models.deletion.SET_DEFAULT, to='wodo.appuser', to_field='username', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='saved',
            name='userS',
            field=models.ForeignKey(default='specsoid', on_delete=django.db.models.deletion.SET_DEFAULT, to='wodo.appuser', to_field='username', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='userT',
            field=models.ForeignKey(default='specsoid', on_delete=django.db.models.deletion.SET_DEFAULT, to='wodo.appuser', to_field='username', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='workrating',
            name='userR',
            field=models.ForeignKey(default='specsoid', on_delete=django.db.models.deletion.SET_DEFAULT, to='wodo.appuser', to_field='username', verbose_name='User'),
        ),
    ]
