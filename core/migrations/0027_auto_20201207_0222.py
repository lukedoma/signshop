# Generated by Django 2.1.7 on 2020-12-06 14:22
# Generated by Django 2.1.7 on 2020-12-06 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20201206_2345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=150)),
                ('contact_email', models.CharField(max_length=150)),
                ('contact_subject', models.CharField(max_length=150)),
                ('contact_message', models.CharField(max_length=150)),
            ],
        ),
    ]

