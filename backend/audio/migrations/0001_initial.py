# Generated by Django 4.0.4 on 2022-05-04 08:52

import audio.models
from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('artist', models.CharField(max_length=250)),
                ('artwork', django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format=None, keep_meta=True, quality=-1, size=[500, 500], upload_to='audios/cover/%Y/%m/%d/', validators=[audio.models.validate_file_extension], verbose_name='کاور')),
                ('url', models.FileField(upload_to='audios/')),
                ('durations', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='آخرین به روز رسانی')),
            ],
        ),
    ]