# Generated by Django 3.2.5 on 2021-07-22 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coderdojochi', '0039_auto_20210611_1044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='race_ethnicity',
        ),
        migrations.AddField(
            model_name='student',
            name='ethnicity',
            field=models.CharField(choices=[('Hispanic', 'Hispanic'), ('Not Hispanic', 'Not Hispanic')], default='', max_length=255),
        ),
        migrations.AddField(
            model_name='student',
            name='race',
            field=models.CharField(default='', max_length=255),
        ),
    ]