# Generated by Django 4.2.4 on 2023-08-29 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapplication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='date',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
