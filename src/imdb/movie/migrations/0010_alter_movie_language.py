# Generated by Django 4.0.4 on 2022-05-30 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0009_alter_movie_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(choices=[('english', 'ENGLISH'), ('korean', 'Korean')], max_length=10),
        ),
    ]
