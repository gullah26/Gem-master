# Generated by Django 3.2 on 2022-11-22 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=55, null=True)),
                ('last_name', models.CharField(max_length=55, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=55)),
                ('message', models.TextField(max_length=1000)),
            ],
        ),
    ]
