# Generated by Django 4.0.5 on 2022-07-02 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0005_alter_flightmodel_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='flightmodel',
            name='id',
            field=models.UUIDField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='flightmodel',
            name='date',
            field=models.DateField(default='default', max_length=100),
        ),
    ]
