# Generated by Django 3.2.9 on 2021-11-09 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ca', '0003_countdownmusic_days_left'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countdownmusic',
            name='days_left',
            field=models.IntegerField(),
        ),
    ]
