# Generated by Django 4.1.7 on 2023-03-22 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="age",
            field=models.IntegerField(default=0, verbose_name="年龄"),
        ),
        migrations.AlterModelTable(
            name="person",
            table="person",
        ),
    ]
