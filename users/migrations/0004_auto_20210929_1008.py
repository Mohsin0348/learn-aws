# Generated by Django 3.2.7 on 2021-09-29 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_unitofhistory_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='block_offensive_word',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='client',
            name='restrict_re_format',
            field=models.BooleanField(default=False),
        ),
    ]
