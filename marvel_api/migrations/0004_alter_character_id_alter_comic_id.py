# Generated by Django 5.0 on 2023-12-24 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marvel_api', '0003_alter_character_description_alter_character_imgurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='comic',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
