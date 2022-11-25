# Generated by Django 3.1.1 on 2022-03-24 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('local', '0002_localinstance_cpu_core'),
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('component_type', models.CharField(blank=True, max_length=128, null=True)),
                ('default_version', models.CharField(blank=True, max_length=128, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ComponentParam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component_id', models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='component id')),
                ('param', models.CharField(blank=True, max_length=128, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ComponentVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component_id', models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='component id')),
                ('version', models.CharField(blank=True, max_length=128, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Workload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('owner', models.CharField(blank=True, max_length=128, null=True)),
                ('repo_url', models.CharField(blank=True, max_length=128, null=True)),
                ('repo_type', models.CharField(blank=True, max_length=128, null=True)),
                ('deploy_mode', models.CharField(blank=True, max_length=128, null=True)),
                ('description', models.CharField(blank=True, max_length=128, null=True)),
                ('mail_recevier', models.CharField(blank=True, max_length=128, null=True)),
                ('main_sender', models.CharField(blank=True, max_length=128, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkloadComponentVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workload_id', models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='component id')),
                ('component_version_id', models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='version id')),
                ('version', models.CharField(blank=True, max_length=20, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkloadSystemConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workload_id', models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='component id')),
                ('component_param_id', models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='parameter id')),
                ('version', models.CharField(blank=True, max_length=20, null=True)),
                ('value', models.CharField(blank=True, max_length=512, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]