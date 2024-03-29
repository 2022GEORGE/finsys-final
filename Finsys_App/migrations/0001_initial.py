# Generated by Django 5.0 on 2023-12-15 07:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fin_Login_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(blank=True, max_length=255, null=True)),
                ('Last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('User_name', models.CharField(blank=True, max_length=255, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('User_Type', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fin_Payment_Terms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_terms_number', models.IntegerField(blank=True, null=True)),
                ('payment_terms_value', models.CharField(blank=True, max_length=100, null=True)),
                ('days', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fin_Distributors_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Distributor_Code', models.CharField(blank=True, max_length=100, null=True)),
                ('Contact', models.CharField(blank=True, max_length=255, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='image/distributor')),
                ('Start_Date', models.DateField(auto_now_add=True, null=True)),
                ('End_date', models.DateField(blank=True, max_length=255, null=True)),
                ('Admin_approval_status', models.CharField(blank=True, max_length=255, null=True)),
                ('Login_Id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_login_details')),
                ('Payment_Term', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_payment_terms')),
            ],
        ),
        migrations.CreateModel(
            name='Fin_Company_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('Company_Code', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.CharField(blank=True, max_length=255, null=True)),
                ('Contact', models.CharField(blank=True, max_length=255, null=True)),
                ('Address', models.TextField(blank=True, max_length=255, null=True)),
                ('City', models.CharField(blank=True, max_length=255, null=True)),
                ('State', models.CharField(blank=True, max_length=255, null=True)),
                ('Country', models.CharField(blank=True, max_length=255, null=True)),
                ('Pincode', models.IntegerField(blank=True, null=True)),
                ('Pan_NO', models.CharField(blank=True, max_length=255, null=True)),
                ('GST_Type', models.CharField(blank=True, max_length=255, null=True)),
                ('GST_NO', models.IntegerField(blank=True, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='image/company')),
                ('Start_Date', models.DateField(auto_now_add=True, null=True)),
                ('End_date', models.DateField(blank=True, max_length=255, null=True)),
                ('Admin_approval_status', models.CharField(blank=True, max_length=255, null=True)),
                ('Distributor_approval_status', models.CharField(blank=True, max_length=255, null=True)),
                ('Registration_Type', models.CharField(blank=True, max_length=255, null=True)),
                ('Distributor_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_distributors_details')),
                ('Login_Id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_login_details')),
                ('Payment_Term', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_payment_terms')),
            ],
        ),
    ]
