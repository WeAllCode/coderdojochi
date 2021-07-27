# Generated by Django 3.2.5 on 2021-07-27 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coderdojochi', '0041_auto_20210723_1013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guardian',
            name='race_ethnicity',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='race_ethnicity',
        ),
        migrations.RemoveField(
            model_name='student',
            name='race_ethnicity',
        ),
        migrations.AddField(
            model_name='guardian',
            name='ethnicity',
            field=models.CharField(choices=[('Hispanic', 'Hispanic'), ('Not Hispanic', 'Not Hispanic')], default='', max_length=12),
        ),
        migrations.AddField(
            model_name='guardian',
            name='race',
            field=models.CharField(choices=[('White', 'White'), ('Black', 'Black'), ('Asian', 'Asian'), ('American Indian', 'American Indian'), ('Native Hawaiin', 'Native Hawaiin'), ('Middle Eastern', 'Middle Eastern')], default='', max_length=15),
        ),
        migrations.AddField(
            model_name='mentor',
            name='ethnicity',
            field=models.CharField(choices=[('Hispanic', 'Hispanic'), ('Not Hispanic', 'Not Hispanic')], default='', max_length=12),
        ),
        migrations.AddField(
            model_name='mentor',
            name='race',
            field=models.CharField(choices=[('White', 'White'), ('Black', 'Black'), ('Asian', 'Asian'), ('American Indian', 'American Indian'), ('Native Hawaiin', 'Native Hawaiin'), ('Middle Eastern', 'Middle Eastern')], default='', max_length=15),
        ),
        migrations.AddField(
            model_name='student',
            name='ethnicity',
            field=models.CharField(choices=[('Hispanic', 'Hispanic'), ('Not Hispanic', 'Not Hispanic')], default='', max_length=12),
        ),
        migrations.AddField(
            model_name='student',
            name='race',
            field=models.CharField(choices=[('White', 'White'), ('Black', 'Black'), ('Asian', 'Asian'), ('American Indian', 'American Indian'), ('Native Hawaiin', 'Native Hawaiin'), ('Middle Eastern', 'Middle Eastern')], default='', max_length=15),
        ),
    ]