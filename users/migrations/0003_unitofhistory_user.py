# Generated by Django 3.2.7 on 2021-09-25 08:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_client_client_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='unitofhistory',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='performer', to=settings.AUTH_USER_MODEL),
        ),
    ]
