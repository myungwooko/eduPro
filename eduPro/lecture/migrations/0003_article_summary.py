# Generated by Django 2.2.6 on 2019-10-29 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0002_auto_20191029_0248'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='summary',
            field=models.TextField(default=1, help_text='요약'),
            preserve_default=False,
        ),
    ]
