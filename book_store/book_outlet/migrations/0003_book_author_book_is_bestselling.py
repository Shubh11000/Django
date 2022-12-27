# Generated by Django 4.1.3 on 2022-12-26 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book_outlet", "0002_alter_book_rating"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="author",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="book",
            name="is_bestselling",
            field=models.BooleanField(default=False),
        ),
    ]
