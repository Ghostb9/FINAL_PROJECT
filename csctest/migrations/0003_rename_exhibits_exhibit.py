# Generated by Django 5.0.4 on 2024-04-11 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csctest', '0002_rename_htmlpage_exhibits'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Exhibits',
            new_name='Exhibit',
        ),
    ]
