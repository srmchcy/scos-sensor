# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-19 20:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Antenna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(help_text=b"Antenna make and model number. E.g. 'ARA CSB-16'.", max_length=255)),
                ('type', models.CharField(blank=True, help_text=b"Antenna type. E.g. 'dipole'.", max_length=255, null=True)),
                ('low_frequency', models.FloatField(blank=True, help_text=b'Low frequency of operational range. [Hz]', null=True)),
                ('high_frequency', models.FloatField(blank=True, help_text=b'High frequency of operational range. [Hz]', null=True)),
                ('gain', models.FloatField(blank=True, help_text=b'Antenna gain in direction of maximum radiation or reception. [dBi]', null=True)),
                ('horizontal_gain_pattern', models.CharField(blank=True, help_text=b'Antenna gain pattern in horizontal plane. Enter as comma-separated floating point numbers. [dBi]', max_length=1023, null=True)),
                ('vertical_gain_pattern', models.CharField(blank=True, help_text=(b'Antenna gain pattern in vertical plane. [dBi]', b'Enter as comma-separated floating point numbers. [dBi]'), max_length=1023, null=True)),
                ('horizontal_beam_width', models.FloatField(blank=True, help_text=b'Horizontal 3-dB beamwidth. [degrees]', null=True)),
                ('vertical_beam_width', models.FloatField(blank=True, help_text=b'Vertical 3-dB beamwidth. [degrees]', null=True)),
                ('cross_polar_discrimintation', models.FloatField(blank=True, help_text=b'Cross-polarization discrimination.', null=True)),
                ('voltage_standing_wave_ratio', models.FloatField(blank=True, help_text=b'Voltage standing wave ratio. [volts]', null=True)),
                ('cable_loss', models.FloatField(blank=True, help_text=b'Loss for cable connecting antenna and preselector. [dB]', null=True)),
                ('steerable', models.NullBooleanField(help_text=b'Defines if the antenna is steerable or not.')),
                ('mobile', models.NullBooleanField(help_text=b'Defines if the antenna is mobile or not.')),
            ],
        ),
        migrations.CreateModel(
            name='Preselector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(help_text=b"Make and model of receiver. E.g., 'Ettus B200'.", max_length=255)),
                ('low_frequency', models.FloatField(blank=True, help_text=b'Low frequency of operational range. [Hz]', null=True)),
                ('high_frequency', models.FloatField(blank=True, help_text=b'High frequency of operational range. [Hz]', null=True)),
                ('noise_figure', models.FloatField(blank=True, help_text=b'Noise Figure. [dB]', null=True)),
                ('max_power', models.FloatField(blank=True, help_text=b'Maximum input power. [dBm]', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RFPath',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rf_path_number', models.PositiveSmallIntegerField(blank=True, help_text=b'RF path number.', null=True)),
                ('low_frequency_passband', models.FloatField(blank=True, help_text=b'Low frequency of filter 1-dB passband. [Hz]', null=True)),
                ('high_frequency_passband', models.FloatField(blank=True, help_text=b'High frequency of filter 1-dB passband. [Hz]', null=True)),
                ('low_frequency_stopband', models.FloatField(blank=True, help_text=b'Low frequency of filter 1-dB stopband. [Hz]', null=True)),
                ('high_frequency_stopband', models.FloatField(blank=True, help_text=b'High frequency of filter 1-dB stopband. [Hz]', null=True)),
                ('lna_gain', models.FloatField(blank=True, help_text=b'Gain of low noise amplifier. [dB]', null=True)),
                ('lna_noise_figure', models.FloatField(blank=True, help_text=b'Noise figure of low noise amplifier. [dB]', null=True)),
                ('cal_source_type', models.CharField(blank=True, help_text=b"E.g., 'calibrated noise source'.", max_length=255, null=True)),
                ('cal_source_enr', models.FloatField(blank=True, help_text=b'Excess noise ratio of calibrated noise source at frequency of RF path. [dB]', null=True)),
                ('preselector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rf_paths', to='capabilities.Preselector')),
            ],
            options={
                'ordering': ('rf_path_number',),
            },
        ),
        migrations.CreateModel(
            name='SensorDefinition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_controller', models.CharField(blank=True, help_text=b'Description of host computer. E.g. Make, model, and configuration.', max_length=1024, null=True)),
                ('antenna', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='capabilities.Antenna')),
                ('preselector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='capabilities.Preselector')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='capabilities.Receiver')),
            ],
        ),
    ]
