# Generated by Django 3.1.1 on 2022-05-05 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('local', '0013_auto_20220426_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localinstancejobqueue',
            name='instance_id',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='localinstancejobqueue',
            name='job_id',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='localjob',
            name='status',
            field=models.CharField(blank=True, choices=[('NOT_START', 'NOT_START'), ('IN_QUEUE', 'IN_QUEUE'), ('RUNNING', 'RUNNING'), ('FAILED', 'FAILED'), ('FINISHED', 'FINISHED'), ('CANCELED', 'CANCELED')], default='IN_QUEUE', max_length=30, null=True),
        ),
    ]
