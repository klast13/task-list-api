# Generated by Django 4.2.3 on 2023-07-14 14:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 14, 14, 43, 47, 152327, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
