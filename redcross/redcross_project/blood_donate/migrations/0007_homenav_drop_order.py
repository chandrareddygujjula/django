# Generated by Django 4.2.4 on 2023-08-14 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood_donate', '0006_announcement_blood'),
    ]

    operations = [
        migrations.AddField(
            model_name='homenav_drop',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
