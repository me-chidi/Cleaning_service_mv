# Generated by Django 4.2.2 on 2023-07-07 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0014_alter_customer_groups_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking", name="time", field=models.TimeField(default="22:07"),
        ),
    ]