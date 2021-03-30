# Generated by Django 3.1.7 on 2021-03-30 01:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sqdata',
            old_name='above_ground_sighter_measure',
            new_name='above_ground_sighter_measurement',
        ),
        migrations.RenameField(
            model_name='sqdata',
            old_name='Age',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='sqdata',
            old_name='colornotes',
            new_name='color_notes',
        ),
        migrations.RenameField(
            model_name='sqdata',
            old_name='combination_fur_color',
            new_name='combination_of_primary_and_highlight_color',
        ),
        migrations.RenameField(
            model_name='sqdata',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='sqdata',
            old_name='Hectare',
            new_name='hectare',
        ),
        migrations.RenameField(
            model_name='sqdata',
            old_name='Hectare_squirrel_number',
            new_name='hectare_squirrel_number',
        ),
        migrations.RenameField(
            model_name='sqdata',
            old_name='Moans',
            new_name='moans',
        ),
        migrations.RenameField(
            model_name='sqdata',
            old_name='Quass',
            new_name='quaas',
        ),
        migrations.RenameField(
            model_name='sqdata',
            old_name='Shift',
            new_name='shift',
        ),
        migrations.RenameField(
            model_name='sqdata',
            old_name='tail_twiches',
            new_name='tail_twitches',
        ),
        migrations.RenameField(
            model_name='sqdata',
            old_name='unique_sq_id',
            new_name='unique_squirrel_id',
        ),
        migrations.RenameField(
            model_name='sqdata',
            old_name='X',
            new_name='x',
        ),
        migrations.RenameField(
            model_name='sqdata',
            old_name='Y',
            new_name='y',
        ),
    ]
