# Generated by Django 4.2 on 2023-04-11 11:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="image",
            field=models.ImageField(null=True, upload_to=""),
        ),
    ]