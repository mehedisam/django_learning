# Generated by Django 5.2 on 2025-06-24 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0005_review_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='num_ratings',
            field=models.IntegerField(default=0),
        ),
    ]
