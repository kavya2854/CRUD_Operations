# Generated by Django 4.2.6 on 2023-12-12 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_employee_comm'),
    ]

    operations = [
        migrations.AddField(
            model_name='dept',
            name='deptblock',
            field=models.CharField(default='A', max_length=100),
        ),
    ]
