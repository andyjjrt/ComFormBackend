# Generated by Django 3.2.7 on 2021-09-05 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_profile_forms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='forms',
            field=models.JSONField(default='{"forms": list}'),
        ),
    ]
