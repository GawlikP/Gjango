# Generated by Django 2.1.7 on 2019-03-01 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gjango_main', '0006_auto_20190301_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='lv',
            field=models.IntegerField(default=1),
        ),
    ]