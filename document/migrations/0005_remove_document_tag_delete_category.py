# Generated by Django 4.1 on 2022-09-01 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0004_category_alter_document_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='tag',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]