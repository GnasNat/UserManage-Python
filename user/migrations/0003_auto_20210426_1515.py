# Generated by Django 3.2 on 2021-04-26 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210426_1514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='unit_id',
        ),
        migrations.AddField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
