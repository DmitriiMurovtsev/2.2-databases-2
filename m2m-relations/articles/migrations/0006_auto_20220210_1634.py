# Generated by Django 3.1.2 on 2022-02-10 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20220210_1633'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['scopes__is_main'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
    ]
