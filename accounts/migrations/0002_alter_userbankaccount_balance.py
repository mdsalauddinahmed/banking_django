# Generated by Django 4.2.9 on 2024-03-26 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbankaccount',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=1000, max_digits=12),
        ),
    ]