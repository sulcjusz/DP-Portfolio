# Generated by Django 3.2.8 on 2021-10-30 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gbapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('title',)},
        ),
    ]
