# Generated by Django 4.1.7 on 2023-06-30 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=30)),
                ('degree', models.CharField(max_length=20)),
                ('course', models.CharField(max_length=20)),
            ],
        ),
    ]
