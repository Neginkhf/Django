# Generated by Django 2.2.3 on 2019-07-21 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stuff',
            name='markdown',
        ),
    ]
