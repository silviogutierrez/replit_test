# Generated by Django 4.0.1 on 2022-02-10 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("example", "0003_alter_choice_question"),
    ]

    operations = [
        migrations.AlterField(
            model_name="choice",
            name="choice_text",
            field=models.CharField(max_length=200, verbose_name="choice"),
        ),
    ]
