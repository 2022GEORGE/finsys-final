# Generated by Django 5.0 on 2024-01-02 14:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finsys_App', '0009_rename_payment_terms_updation_fin_payment_terms_updation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fin_anotification',
            name='Modules_List',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_modules_list'),
        ),
    ]
