# Generated by Django 2.2.13 on 2020-11-20 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20201120_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ref_code',
            field=models.CharField(default=22, max_length=30),
            preserve_default=False,
        ),
    ]
