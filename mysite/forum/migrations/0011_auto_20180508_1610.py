# Generated by Django 2.0.3 on 2018-05-08 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0010_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=None, to='personal.UserProfile'),
        ),
    ]
