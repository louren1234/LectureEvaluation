# Generated by Django 3.0.1 on 2020-02-21 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0006_auto_20200221_1411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eval',
            name='overall',
        ),
        migrations.RemoveField(
            model_name='eval',
            name='semester',
        ),
    ]
