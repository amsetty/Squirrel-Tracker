# Generated by Django 3.1.7 on 2021-03-30 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210329_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sqdata',
            name='date',
            field=models.IntegerField(help_text='Sighting date', max_length=20),
        ),
    ]