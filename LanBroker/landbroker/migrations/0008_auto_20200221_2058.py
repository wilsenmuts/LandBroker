# Generated by Django 2.2.6 on 2020-02-21 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landbroker', '0007_auto_20200217_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='map_scan',
            field=models.ImageField(upload_to='landbroker'),
        ),
    ]
