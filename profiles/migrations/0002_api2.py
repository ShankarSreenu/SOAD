# Generated by Django 3.0.2 on 2020-11-27 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Api2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('table_size', models.IntegerField()),
                ('slot_1_status', models.CharField(max_length=20)),
                ('slot_2_status', models.CharField(max_length=20)),
                ('slot_3_status', models.CharField(max_length=20)),
                ('slot_4_status', models.CharField(max_length=20)),
                ('slot_5_status', models.CharField(max_length=20)),
                ('slot_6_status', models.CharField(max_length=20)),
                ('slot_7_status', models.CharField(max_length=20)),
                ('slot_8_status', models.CharField(max_length=20)),
                ('slot_9_status', models.CharField(max_length=20)),
                ('slot_10_status', models.CharField(max_length=20)),
                ('slot_11_status', models.CharField(max_length=20)),
                ('slot_12_status', models.CharField(max_length=20)),
                ('slot_13_status', models.CharField(max_length=20)),
                ('slot_14_status', models.CharField(max_length=20)),
                ('slot_15_status', models.CharField(max_length=20)),
                ('slot_16_status', models.CharField(max_length=20)),
                ('slot_17_status', models.CharField(max_length=20)),
                ('slot_18_status', models.CharField(max_length=20)),
                ('slot_19_status', models.CharField(max_length=20)),
                ('slot_20_status', models.CharField(max_length=20)),
            ],
        ),
    ]
