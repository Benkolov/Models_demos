# Generated by Django 4.2.1 on 2023-06-08 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_employees_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='level',
            field=models.CharField(choices=[('jun', 'Junior'), ('mid', 'Middle'), ('sin', 'Senior')], default='jun', max_length=3),
        ),
    ]
