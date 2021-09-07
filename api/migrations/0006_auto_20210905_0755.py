# Generated by Django 3.2.7 on 2021-09-05 07:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_profile_forms'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(default='UntitledForm', max_length=20)),
                ('description', models.CharField(default='', max_length=100)),
                ('boxes', models.JSONField(default=list)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='forms',
            field=models.JSONField(default=list),
        ),
    ]
