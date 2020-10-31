# Generated by Django 3.1.2 on 2020-10-31 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201029_1845'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('discription', models.TextField()),
                ('issue_date', models.DateField()),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('discription', models.TextField()),
                ('starting_date', models.DateField()),
                ('ending_date', models.DateField()),
                ('url', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('workplace', models.CharField(max_length=200)),
                ('discription', models.TextField()),
                ('starting_date', models.DateField()),
                ('ending_date', models.DateField()),
            ],
        ),
    ]
