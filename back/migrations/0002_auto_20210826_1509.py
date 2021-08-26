# Generated by Django 3.2.6 on 2021-08-26 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hotel',
            options={'ordering': ['cit'], 'verbose_name': 'Hotel', 'verbose_name_plural': 'Hotels'},
        ),
        migrations.RenameField(
            model_name='hotel',
            old_name='hotel_code',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='hotel',
            old_name='hotel_name',
            new_name='name',
        ),
    ]
