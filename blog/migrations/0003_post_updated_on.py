# Generated by Django 4.2.18 on 2025-01-16 10:54

from django.db import migrations, models


class Migration(migrations.Migration):
 # the dependencies refer to the previous migration, 0002_post_excerpt, and the operations are to add a field with the details we gave.
    dependencies = [
        ('blog', '0002_post_excerpt'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
