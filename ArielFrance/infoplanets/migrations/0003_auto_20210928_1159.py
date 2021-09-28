# Generated by Django 3.2.7 on 2021-09-28 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infoplanets', '0002_auto_20210927_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='star',
            name='age',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='star',
            name='age_moe',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='star',
            name='density',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='star',
            name='density_moe',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='star',
            name='effective_temperature',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='star',
            name='effective_temperature_moe',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='star',
            name='luminosity',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='star',
            name='luminosity_moe',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='star',
            name='mass',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='star',
            name='mass_moe',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=7, null=True),
        ),
        migrations.AddField(
            model_name='star',
            name='metallicity',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='star',
            name='metallicity_moe',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='star',
            name='radial_velocity',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=18, null=True),
        ),
        migrations.AddField(
            model_name='star',
            name='radial_velocity_moe',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=16, null=True),
        ),
        migrations.AddField(
            model_name='star',
            name='radius',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='star',
            name='radius_moe',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='star',
            name='rotation_period',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='star',
            name='rotation_period_moe',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='star',
            name='rotational_velocity',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='star',
            name='rotational_velocity_moe',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='star',
            name='spectral_type',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='star',
            name='surface_gravity',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='star',
            name='surface_gravity_moe',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=9, null=True),
        ),
    ]
