# Generated by Django 2.2.6 on 2019-10-29 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(blank=True, help_text='기자이름', max_length=255, null=True),
        ),
    ]
