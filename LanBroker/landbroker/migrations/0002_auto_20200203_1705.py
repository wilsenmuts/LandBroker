# Generated by Django 2.2.6 on 2020-02-03 17:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('landbroker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sell',
            name='own_full',
        ),
        migrations.RemoveField(
            model_name='sell',
            name='own_lease',
        ),
        migrations.RemoveField(
            model_name='sell',
            name='own_rent',
        ),
        migrations.AddField(
            model_name='sell',
            name='ownership',
            field=models.CharField(default='null', max_length=35),
        ),
        migrations.AddField(
            model_name='sell',
            name='tel_no',
            field=models.CharField(default=django.utils.timezone.now, max_length=35),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sell',
            name='id_card',
            field=models.ImageField(upload_to='landbroker'),
        ),
        migrations.AlterField(
            model_name='sell',
            name='map_scan',
            field=models.ImageField(upload_to='landbroker'),
        ),
        migrations.AlterField(
            model_name='sell',
            name='title_scan',
            field=models.ImageField(upload_to='landbroker'),
        ),
    ]