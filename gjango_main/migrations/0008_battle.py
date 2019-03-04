# Generated by Django 2.1.7 on 2019-03-04 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gjango_main', '0007_auto_20190301_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Battle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_id', models.IntegerField(default=-1)),
                ('enemy_id', models.IntegerField(default=-1)),
                ('result', models.BooleanField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Battle',
            },
        ),
    ]
