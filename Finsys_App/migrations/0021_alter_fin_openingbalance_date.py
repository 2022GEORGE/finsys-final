# Generated by Django 3.2.23 on 2024-01-18 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finsys_App', '0020_auto_20240118_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fin_openingbalance',
            name='Date',
            field=models.DateField(),
        ),
    ]
