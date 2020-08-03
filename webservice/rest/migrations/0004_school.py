# Generated by Django 3.0.9 on 2020-08-03 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0003_auto_20200803_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=10)),
                ('created_date', models.DateTimeField()),
                ('deleted_date', models.DateTimeField(blank=True, null=True)),
                ('fk_faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest.Faculty', verbose_name='Faculty')),
            ],
        ),
    ]