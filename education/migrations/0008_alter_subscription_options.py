# Generated by Django 4.2.6 on 2023-11-03 10:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("education", "0007_subscription"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="subscription",
            options={"verbose_name": "подписка", "verbose_name_plural": "подписки"},
        ),
    ]
