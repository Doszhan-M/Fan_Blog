# Generated by Django 3.1.7 on 2021-04-12 15:25

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0008_auto_20210411_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=255, unique=True, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_category',
        ),
        migrations.AddField(
            model_name='post',
            name='post_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='board.category', verbose_name='Категория'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='post_picture',
            field=models.ImageField(blank=True, upload_to='board/image/%Y/%m'),
        ),
    ]
