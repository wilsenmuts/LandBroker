# Generated by Django 2.2.6 on 2020-02-04 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landbroker', '0005_sell_date_box'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell',
            name='distance',
            field=models.CharField(default='On Road', max_length=35),
        ),
        migrations.AlterField(
            model_name='sell',
            name='map_scan',
            field=models.ImageField(default='bykand.jpg', upload_to='landbroker'),
        ),
    ]