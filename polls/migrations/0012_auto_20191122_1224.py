# Generated by Django 2.2.4 on 2019-11-22 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20191122_1222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(default=777, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='videofile',
            field=models.FileField(null=True, upload_to='posts/', verbose_name=''),
        ),
    ]
