# Generated by Django 3.1.7 on 2021-04-17 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0015_auto_20210417_0010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='accepted_responses',
        ),
        migrations.RemoveField(
            model_name='post',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='responses',
        ),
    ]
