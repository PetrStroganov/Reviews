# Generated by Django 4.1 on 2022-11-21 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_review_like_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(max_length=200, null=True),
        ),
    ]