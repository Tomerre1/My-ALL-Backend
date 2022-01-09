# Generated by Django 3.2.9 on 2022-01-09 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('mail', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=40)),
                ('userType', models.CharField(default=None, max_length=40, null=True)),
                ('parentId', models.IntegerField(default=None, null=True)),
            ],
        ),
    ]
