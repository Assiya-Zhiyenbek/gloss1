# Generated by Django 2.2.4 on 2020-02-20 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_like_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
