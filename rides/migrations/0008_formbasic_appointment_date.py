# Generated by Django 2.0.5 on 2018-08-03 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0007_auto_20180802_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='formbasic',
            name='appointment_date',
            field=models.CharField(default='', max_length=8),
        ),
    ]
