# Generated by Django 5.0.7 on 2024-10-05 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0007_alter_applicant_profile_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='end_year',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='education',
            name='start_year',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
