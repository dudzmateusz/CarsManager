# Generated by Django 3.2.4 on 2022-01-30 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicles',
            name='car_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
