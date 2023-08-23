# Generated by Django 4.2.4 on 2023-08-23 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(max_length=100)),
                ('prod_quantity', models.CharField(max_length=20)),
                ('prod_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('prod_desc', models.TextField()),
            ],
        ),
    ]
