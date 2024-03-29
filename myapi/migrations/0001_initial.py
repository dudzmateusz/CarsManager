# Generated by Django 3.2.4 on 2022-01-30 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('car_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('make', models.CharField(max_length=60)),
                ('model', models.CharField(max_length=60)),
                ('avg_rating', models.FloatField(default=0.0)),
                ('rates_number', models.IntegerField(default=0)),
            ],
        ),
    ]
