# Generated by Django 3.2.16 on 2022-11-29 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20221129_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tc',
            field=models.BooleanField(default=True),
        ),
    ]
