# Generated by Django 3.0.8 on 2020-08-30 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_1', '0004_auto_20200827_0414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='ptime',
            field=models.DateTimeField(null=True),
        ),
    ]