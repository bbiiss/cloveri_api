# Generated by Django 2.2.6 on 2022-02-15 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='element',
            name='element_test',
        ),
        migrations.AlterField(
            model_name='element',
            name='children',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
