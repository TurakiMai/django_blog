# Generated by Django 2.2.1 on 2019-06-24 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Article',
            new_name='article',
        ),
    ]