# Generated by Django 4.2.1 on 2023-05-09 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_create_homepage"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="homepage",
            options={"verbose_name": "Home Page", "verbose_name_plural": "Home Pages"},
        ),
        migrations.AddField(
            model_name="homepage",
            name="banner_title",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
