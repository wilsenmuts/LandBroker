# Generated by Django 2.2.6 on 2020-02-04 08:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('landbroker', '0004_sell_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell',
            name='date_box',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
