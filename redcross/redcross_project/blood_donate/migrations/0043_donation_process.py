# Generated by Django 4.2.4 on 2023-08-30 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood_donate', '0042_remove_address_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='donation_process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('point1', models.CharField(max_length=300)),
                ('point2', models.CharField(max_length=300)),
                ('point3', models.CharField(max_length=300)),
                ('point4', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='image/')),
            ],
        ),
    ]
