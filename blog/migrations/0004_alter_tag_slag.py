# Generated by Django 4.0.2 on 2024-08-17 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_tag_alter_category_slag_alter_post_category_post_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='slag',
            field=models.SlugField(verbose_name='URL'),
        ),
    ]
