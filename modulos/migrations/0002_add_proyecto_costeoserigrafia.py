# Generated by Django 4.2 on 2023-05-15 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("modulos", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="costeoserigrafia",
            name="proyecto",
            field=models.CharField(max_length=255, default=None, blank=True, null=True),
        ),
    ]