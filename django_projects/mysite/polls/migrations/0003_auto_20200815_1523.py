# Generated by Django 3.0.8 on 2020-08-15 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200815_0639'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Answer',
            new_name='Choice',
        ),
    ]
