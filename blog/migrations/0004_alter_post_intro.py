# Generated by Django 4.1.4 on 2022-12-09 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_category_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='intro',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
