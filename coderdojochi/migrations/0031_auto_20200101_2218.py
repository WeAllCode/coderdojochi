# Generated by Django 2.2.9 on 2020-01-02 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coderdojochi', '0030_auto_20200101_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='old_end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='old_mentor_end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='old_mentor_start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
