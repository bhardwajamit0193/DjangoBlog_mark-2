# Generated by Django 3.1.3 on 2020-12-17 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0005_auto_20201217_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippets',
            field=models.CharField(default='Click above To Read Blog Post.......', max_length=50),
        ),
    ]