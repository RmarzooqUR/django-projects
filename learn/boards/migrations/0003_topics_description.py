# Generated by Django 3.0.7 on 2020-06-26 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_auto_20200624_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='topics',
            name='description',
            field=models.CharField(default='indescribable', max_length=255),
        ),
    ]