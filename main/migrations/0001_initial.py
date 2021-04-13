# Generated by Django 3.1.7 on 2021-04-04 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sqdata',
            fields=[
                ('x', models.FloatField(help_text='Longitude coordinate for squirrel sighting point', max_length=25)),
                ('y', models.FloatField(help_text='Latitude coordinate for squirrel sighting point', max_length=25)),
                ('unique_squirrel_id', models.CharField(help_text='Hectare ID" + "Shift" + "Date" (MMDD) + "Hectare Squirrel Number.', max_length=40)),
                ('hectare', models.CharField(help_text='ID tag derived from hectare grid', max_length=20)),
                ('shift', models.CharField(help_text='Value is either "AM" or "PM," to communicate whether the sighting session occurred in the morning or late afternoon', max_length=20)),
                ('date', models.IntegerField(help_text='Sighting date', max_length=20)),
                ('hectare_squirrel_number', models.IntegerField(help_text='Number within the chronological sequence of squirrel sightings for a discrete sighting session', max_length=30)),
                ('age', models.CharField(help_text='Value is either Adult or Juvenile.', max_length=10)),
                ('primary_fur_color', models.CharField(max_length=30)),
                ('highlight_fur_color', models.CharField(max_length=30)),
                ('combination_of_primary_and_highlight_color', models.CharField(max_length=30)),
                ('color_notes', models.TextField(blank=True)),
                ('location', models.CharField(max_length=50)),
                ('above_ground_sighter_measurement', models.CharField(max_length=10)),
                ('specific_location', models.TextField(blank=True)),
                ('running', models.BooleanField(default=False)),
                ('chasing', models.BooleanField(default=False)),
                ('climbing', models.BooleanField(default=False)),
                ('eating', models.BooleanField(default=False)),
                ('foraging', models.BooleanField(default=False)),
                ('other_activities', models.TextField(blank=True)),
                ('kuks', models.BooleanField(default=False)),
                ('quaas', models.BooleanField(default=False)),
                ('moans', models.BooleanField(default=False)),
                ('tail_flags', models.BooleanField(default=False)),
                ('tail_twitches', models.BooleanField(default=False)),
                ('approaches', models.BooleanField(default=False)),
                ('indifferent', models.BooleanField(default=False)),
                ('runs_from', models.BooleanField(default=False)),
                ('other_interactions', models.TextField(blank=True)),
                ('lat_long', models.CharField(max_length=50)),
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]