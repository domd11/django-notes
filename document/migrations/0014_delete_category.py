# Generated by Django 4.1 on 2022-09-02 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0013_category_remove_document_priority'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
