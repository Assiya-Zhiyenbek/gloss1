# Generated by Django 2.2.4 on 2020-02-23 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0027_auto_20200223_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numberofvideos',
            name='name',
            field=models.CharField(default='number', help_text='number', max_length=500),
            preserve_default=False,
        ),
    ]
