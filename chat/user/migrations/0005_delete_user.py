# Generated by Django 3.0.5 on 2021-03-21 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_message'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
