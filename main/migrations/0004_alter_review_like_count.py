# Generated by Django 4.1 on 2022-11-21 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_review_like_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
    ]
