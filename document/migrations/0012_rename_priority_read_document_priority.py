# Generated by Django 4.1 on 2022-09-02 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0011_document_priority_read'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='priority_read',
            new_name='priority',
        ),
    ]
