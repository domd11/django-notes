# Generated by Django 4.1 on 2022-09-01 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0007_rename_tag_document_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='category',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
