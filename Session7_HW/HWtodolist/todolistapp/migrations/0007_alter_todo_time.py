# Generated by Django 4.0.3 on 2022-04-06 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolistapp', '0006_alter_todo_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='time',
            field=models.DateField(null=True),
        ),
    ]
