# Generated by Django 3.2.15 on 2023-10-04 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='temperature',
            name='value',
            field=models.CharField(default='DEFAULT VALUE', max_length=200),
        ),
    ]