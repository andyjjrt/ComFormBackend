# Generated by Django 3.2.7 on 2021-09-06 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20210906_0855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='box',
            name='to',
        ),
        migrations.AddField(
            model_name='box',
            name='from_box',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='to', to='api.box'),
        ),
    ]
