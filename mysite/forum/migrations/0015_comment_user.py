# Generated by Django 2.0.3 on 2018-05-08 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_userprofile_image'),
        ('forum', '0014_remove_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=2, on_delete=None, to='personal.UserProfile'),
            preserve_default=False,
        ),
    ]
