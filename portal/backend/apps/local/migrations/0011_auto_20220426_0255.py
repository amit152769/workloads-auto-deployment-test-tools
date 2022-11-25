# Generated by Django 3.1.1 on 2022-04-26 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('local', '0010_auto_20220331_0057'),
    ]

    operations = [
        migrations.AddField(
            model_name='localinstance',
            name='k8s_controller',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='localinstance',
            name='k8s_role',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='localinstance',
            name='os',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='localinstance',
            name='platform',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
