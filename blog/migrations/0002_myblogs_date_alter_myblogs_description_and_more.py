# Generated by Django 4.0 on 2022-01-04 10:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myblogs',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='myblogs',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='myblogs',
            name='image',
            field=models.ImageField(blank=True, upload_to='blog/images/'),
        ),
        migrations.AlterField(
            model_name='myblogs',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]