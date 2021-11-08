# Generated by Django 3.2.8 on 2021-10-24 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('author', models.TextField()),
                ('publication_date', models.DateField()),
                ('isbn', models.TextField(max_length=30)),
                ('page_count', models.TextField(max_length=10)),
                ('link_to_cover', models.SlugField()),
                ('publication_language', models.TextField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TemporaryInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.TextField()),
                ('info', models.TextField()),
            ],
        ),
    ]