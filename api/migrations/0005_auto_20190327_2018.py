# Generated by Django 2.1.7 on 2019-03-27 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190327_2016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='word',
        ),
        migrations.AddField(
            model_name='video',
            name='word',
            field=models.ManyToManyField(to='api.Word'),
        ),
    ]
