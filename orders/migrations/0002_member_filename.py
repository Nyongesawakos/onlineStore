# Generated by Django 5.1.2 on 2024-10-31 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='filename',
            field=models.FileField(default=255, upload_to=''),
            preserve_default=False,
        ),
    ]
