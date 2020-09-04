# Generated by Django 3.0.8 on 2020-08-24 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='pheat',
            field=models.FloatField(default=37.0),
        ),
        migrations.AddField(
            model_name='patient',
            name='pid',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='psymptom',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='ptime',
            field=models.DateField(null=True),
        ),
    ]
