# Generated by Django 5.1.2 on 2024-12-06 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_rename_custom_id_member_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
