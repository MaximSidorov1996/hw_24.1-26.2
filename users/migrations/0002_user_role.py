# Generated by Django 4.2.6 on 2023-10-31 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('member', 'member'), ('moderator', 'moderator')], max_length=9, null=True, verbose_name='роль'),
        ),
    ]
