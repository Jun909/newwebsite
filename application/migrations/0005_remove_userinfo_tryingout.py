# Generated by Django 5.1.1 on 2024-10-31 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='tryingout',
        ),
    ]
