# Generated by Django 3.2.7 on 2021-09-29 10:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210929_1008'),
        ('chat', '0005_auto_20210926_1007'),
    ]

    operations = [
        migrations.CreateModel(
            name='OffensiveWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='REFormat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expression', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='participant_photo'),
        ),
        migrations.CreateModel(
            name='ClientREFormats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='RE_format', to='users.client')),
                ('expressions', models.ManyToManyField(to='chat.REFormat')),
            ],
        ),
        migrations.CreateModel(
            name='ClientOffensiveWords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='offensive_word', to='users.client')),
                ('words', models.ManyToManyField(to='chat.OffensiveWord')),
            ],
        ),
    ]