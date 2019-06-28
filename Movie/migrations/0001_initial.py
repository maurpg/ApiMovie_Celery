# Generated by Django 2.2 on 2019-06-27 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=20)),
                ('genere', models.CharField(max_length=50)),
            ],
        ),
    ]
