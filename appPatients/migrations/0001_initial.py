# Generated by Django 4.2.4 on 2023-08-04 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('PatientID', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=30, verbose_name='Name')),
                ('lastName', models.CharField(max_length=30, verbose_name='Lastname')),
                ('registrationDate', models.DateTimeField(auto_now_add=True, verbose_name='RegistrationDate')),
                ('phone', models.CharField(max_length=30, verbose_name='Phone')),
                ('gender', models.CharField(max_length=30, verbose_name='Gender')),
                ('maritalStatus', models.CharField(max_length=15, verbose_name='MaritalStatus')),
                ('nationality', models.CharField(max_length=15, verbose_name='Nationality')),
                ('city', models.CharField(max_length=30, verbose_name='City')),
                ('address', models.CharField(max_length=120, verbose_name='Address')),
                ('documentType', models.CharField(max_length=30, verbose_name='DocumentType')),
                ('documentNumber', models.CharField(max_length=30, verbose_name='DocumentNumber')),
                ('birthDate', models.DateField(verbose_name='BirthDate')),
                ('email', models.EmailField(max_length=30, verbose_name='Email')),
                ('insuranceType', models.CharField(max_length=15, verbose_name='InsuranceType')),
                ('occupation', models.CharField(max_length=30, verbose_name='Occupation')),
            ],
        ),
    ]
