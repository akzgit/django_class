# Generated by Django 4.2.4 on 2023-08-10 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmpDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.CharField(max_length=20)),
                ('empname', models.CharField(max_length=50)),
                ('empemail', models.EmailField(max_length=254)),
                ('empcontact', models.BigIntegerField()),
            ],
            options={
                'db_table': 'EmpDetails',
            },
        ),
    ]
