# Generated by Django 3.2.2 on 2021-08-18 11:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pics')),
                ('title', models.CharField(max_length=100)),
                ('startDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('destination1', models.CharField(max_length=100)),
                ('destination2', models.CharField(max_length=100)),
                ('destination3', models.CharField(max_length=100)),
                ('destination4', models.CharField(max_length=100, null=True)),
                ('destination5', models.CharField(max_length=100, null=True)),
                ('duration', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]