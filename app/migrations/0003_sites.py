# Generated by Django 3.2.5 on 2021-09-26 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210818_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pics')),
                ('title', models.CharField(max_length=400)),
                ('summary', models.CharField(max_length=400)),
            ],
        ),
    ]
