# Generated by Django 3.2.7 on 2021-09-06 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20210906_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='from_box',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to', to='api.box'),
        ),
    ]
