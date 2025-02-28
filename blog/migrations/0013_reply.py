# Generated by Django 4.0.2 on 2024-08-20 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_comment_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名前')),
                ('text', models.TimeField(verbose_name='本文')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='作成日')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.comment', verbose_name='返信')),
            ],
            options={
                'verbose_name_plural': 'コメント',
            },
        ),
    ]
