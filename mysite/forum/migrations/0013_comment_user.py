# Generated by Django 2.0.3 on 2018-05-08 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_userprofile_image'),
        ('forum', '0012_remove_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=1, on_delete=None, to='personal.UserProfile'),
            preserve_default=False,
        ),
    ]
