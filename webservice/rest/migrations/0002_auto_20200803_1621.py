# Generated by Django 3.0.8 on 2020-08-03 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='deleted_date',
            field=models.DateTimeField(null=True),
        ),
    ]