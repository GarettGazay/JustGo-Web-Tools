# Generated by Django 2.0.6 on 2018-08-08 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0020_auto_20180807_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formbasic',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='reoccuring',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
