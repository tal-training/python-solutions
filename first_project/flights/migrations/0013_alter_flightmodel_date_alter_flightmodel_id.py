# Generated by Django 4.0.5 on 2022-07-02 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0012_alter_flightmodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightmodel',
            name='date',
            field=models.CharField(default='default', max_length=100),
        ),
        migrations.AlterField(
            model_name='flightmodel',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
