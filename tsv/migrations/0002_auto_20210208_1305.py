# Generated by Django 3.1.3 on 2021-02-08 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsv', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='happiness',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='answers',
            name='wake_up',
            field=models.CharField(max_length=30, null=True),
        ),
    ]