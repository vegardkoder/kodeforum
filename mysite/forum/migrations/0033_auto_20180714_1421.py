# Generated by Django 2.0.3 on 2018-07-14 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0032_auto_20180712_1233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tittel',
            new_name='title',
        ),
    ]