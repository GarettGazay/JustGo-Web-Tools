# Generated by Django 2.0.5 on 2018-08-21 21:35

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0037_auto_20180821_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='reocurring',
            name='patient_gender',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=11, null=True),
        ),
    ]
