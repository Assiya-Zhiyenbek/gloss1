# Generated by Django 2.2.4 on 2020-02-23 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0024_numberofvideos'),
    ]

    operations = [
        migrations.AddField(
            model_name='numberofvideos',
            name='name',
            field=models.CharField(default=None, help_text='number', max_length=500),
        ),
    ]