# Generated by Django 3.2.19 on 2023-09-12 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('local', '0029_alter_localjobtestresult_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='localinstance',
            name='password',
        ),
    ]