# Generated by Django 3.0.4 on 2020-07-24 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'ordering': ['name']},
        ),
    ]
