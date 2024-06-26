# Generated by Django 5.0.3 on 2024-04-16 10:49

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymeusers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='humocard',
            name='expired',
            field=models.DateTimeField(default=datetime.datetime(2028, 4, 15, 10, 49, 54, 182858, tzinfo=datetime.timezone.utc), editable=False),
        ),
        migrations.AlterField(
            model_name='humocard',
            name='pin_code',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(3), django.core.validators.MaxValueValidator(4)]),
        ),
        migrations.AlterField(
            model_name='uzcard',
            name='expired',
            field=models.DateTimeField(default=datetime.datetime(2028, 4, 15, 10, 49, 54, 182858, tzinfo=datetime.timezone.utc), editable=False),
        ),
        migrations.AlterField(
            model_name='uzcard',
            name='pin_code',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(3), django.core.validators.MaxValueValidator(4)]),
        ),
        migrations.AlterField(
            model_name='visaclassic',
            name='expired',
            field=models.DateTimeField(default=datetime.datetime(2028, 4, 15, 10, 49, 54, 182858, tzinfo=datetime.timezone.utc), editable=False),
        ),
        migrations.AlterField(
            model_name='visaclassic',
            name='pin_code',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(3), django.core.validators.MaxValueValidator(4)]),
        ),
        migrations.AlterField(
            model_name='visagold',
            name='expired',
            field=models.DateTimeField(default=datetime.datetime(2028, 4, 15, 10, 49, 54, 182858, tzinfo=datetime.timezone.utc), editable=False),
        ),
        migrations.AlterField(
            model_name='visagold',
            name='pin_code',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(3), django.core.validators.MaxValueValidator(4)]),
        ),
    ]
