# Generated by Django 2.0.5 on 2018-08-18 05:36

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0032_auto_20180817_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reocurring',
            name='weekdays',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Mon', 'Mon'), ('Tue', 'Tue'), ('Wed', 'Wed'), ('Thur', 'Thur'), ('Fri', 'Fri'), ('Sat', 'Sat'), ('Sun', 'Sun')], max_length=28, null=True),
        ),
    ]
