# Generated by Django 4.2.4 on 2023-08-08 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood_donate', '0002_alter_homenav_drop_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='appdown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('app', models.ImageField(upload_to='media/')),
                ('url', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='appfooter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('url', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=100)),
                ('heading', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='appfooter1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('url', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=100)),
                ('heading', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='gettouch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='socialicon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon1', models.ImageField(upload_to='media/')),
                ('url1', models.CharField(max_length=100)),
            ],
        ),
    ]