# Generated by Django 3.0.1 on 2020-02-23 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile_email'),
        ('crud', '0020_auto_20200223_0112'),
    ]

    operations = [
        migrations.AddField(
            model_name='evals',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile'),
            preserve_default=False,
        ),
    ]
