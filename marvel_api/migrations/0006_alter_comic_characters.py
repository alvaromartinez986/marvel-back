# Generated by Django 5.0 on 2023-12-24 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marvel_api', '0005_alter_character_id_alter_comic_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comic',
            name='characters',
            field=models.ManyToManyField(related_name='comics', to='marvel_api.character'),
        ),
    ]
