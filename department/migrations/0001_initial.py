# Generated by Django 3.2.7 on 2021-09-04 16:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=500)),
                ('picture', models.ImageField(upload_to='')),
                ('banner', models.ImageField(upload_to='')),
                ('admins', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
