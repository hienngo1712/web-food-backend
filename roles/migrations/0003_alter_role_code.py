# Generated by Django 4.2.20 on 2025-06-24 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0002_alter_role_role_name_rename_role_name_role_rolename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='code',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
