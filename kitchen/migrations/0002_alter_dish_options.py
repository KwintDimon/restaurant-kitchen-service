# Generated by Django 5.0.5 on 2024-05-06 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dish',
            options={'verbose_name': 'dish', 'verbose_name_plural': 'dishes'},
        ),
    ]
