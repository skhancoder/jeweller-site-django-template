# Generated by Django 2.2.4 on 2020-08-06 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rjjewellers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoldImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.DeleteModel(
            name='Subscriber',
        ),
    ]