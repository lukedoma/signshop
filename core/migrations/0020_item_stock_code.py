# Generated by Django 2.1.7 on 2020-12-05 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_refund'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='stock_code',
            field=models.CharField(default='SBOH1060Z', max_length=100),
            preserve_default=False,
        ),
    ]