# Generated by Django 2.2.6 on 2019-10-30 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0004_auto_20191030_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturestatus',
            name='view_complete_sec',
            field=models.FloatField(default=0, help_text='영상시청 완료시간'),
        ),
    ]
