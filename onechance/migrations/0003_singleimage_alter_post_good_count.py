# Generated by Django 4.2.6 on 2023-10-08 00:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("onechance", "0002_post_caption"),
    ]

    operations = [
        migrations.CreateModel(
            name="SingleImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("img", models.ImageField(upload_to="images/")),
            ],
        ),
        migrations.AlterField(
            model_name="post",
            name="good_count",
            field=models.IntegerField(blank=True, default=0),
        ),
    ]