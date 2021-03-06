# Generated by Django 3.2.7 on 2021-10-21 04:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0014_auto_20211020_0438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversation',
            name='connected',
        ),
        migrations.CreateModel(
            name='ConnectedParticipantConversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connection_token', models.UUIDField()),
                ('conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='connected_participants', to='chat.conversation')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='connected_conversation', to='chat.participant')),
            ],
        ),
    ]
