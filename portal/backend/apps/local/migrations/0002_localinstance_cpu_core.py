# Generated by Django 3.1.1 on 2022-03-23 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('local', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='localinstance',
            name='cpu_core',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]