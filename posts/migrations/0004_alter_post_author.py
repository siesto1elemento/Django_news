# Generated by Django 4.2.1 on 2024-04-06 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(blank=True, default='anonymous', max_length=100, null=True),
        ),
    ]
