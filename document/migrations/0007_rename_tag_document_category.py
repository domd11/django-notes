# Generated by Django 4.1 on 2022-09-01 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0006_category_document_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='tag',
            new_name='category',
        ),
    ]
