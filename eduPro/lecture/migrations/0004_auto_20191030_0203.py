# Generated by Django 2.2.6 on 2019-10-30 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0003_article_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturestatus',
            name='view_complete_sec',
            field=models.DecimalField(decimal_places=5, default=0, help_text='영상시청 완료시간', max_digits=6),
        ),
    ]
