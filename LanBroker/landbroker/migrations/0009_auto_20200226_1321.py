# Generated by Django 2.2.6 on 2020-02-26 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landbroker', '0008_auto_20200221_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='id_card',
            field=models.ImageField(upload_to='landbroker/'),
        ),
        migrations.AlterField(
            model_name='sell',
            name='map_scan',
            field=models.ImageField(upload_to='landbroker/'),
        ),
        migrations.AlterField(
            model_name='sell',
            name='title_scan',
            field=models.ImageField(upload_to='landbroker/'),
        ),
    ]
