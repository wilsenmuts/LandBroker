# Generated by Django 2.2.6 on 2020-09-30 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landbroker', '0016_auto_20200714_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
