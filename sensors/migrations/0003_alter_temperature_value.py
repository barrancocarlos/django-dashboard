# Generated by Django 3.2.15 on 2023-10-04 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0002_temperature_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperature',
            name='value',
            field=models.CharField(default='00', max_length=200),
        ),
    ]
