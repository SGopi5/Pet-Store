# Generated by Django 5.0 on 2024-01-05 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_json', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address1', models.CharField(max_length=255)),
                ('address2', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=20)),
                ('payment_details', models.TextField()),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='orderupdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField()),
                ('update_desc', models.CharField(max_length=50)),
                ('deliverd', models.BooleanField()),
                ('time_stamp', models.DateField()),
            ],
        ),
    ]
