# Generated by Django 3.2.8 on 2021-10-17 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tester', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userAge',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='userDate',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='userEmail',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='userPhone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='userTime',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='userVac',
            field=models.CharField(max_length=20),
        ),
    ]
