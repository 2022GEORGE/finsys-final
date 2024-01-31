# Generated by Django 3.2.23 on 2024-01-27 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Finsys_App', '0028_auto_20240127_0850'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holiday_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('holiday_name', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('action', models.CharField(blank=True, max_length=255, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
                ('holiday', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.holiday')),
                ('login', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_login_details')),
            ],
        ),
    ]
