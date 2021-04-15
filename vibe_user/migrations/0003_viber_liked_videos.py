# Generated by Django 3.2 on 2021-04-15 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0004_alter_comment_liked_by'),
        ('vibe_user', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='viber',
            name='liked_videos',
            field=models.ManyToManyField(related_name='liked_videos_list', to='video.Video'),
        ),
    ]
