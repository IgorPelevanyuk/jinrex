# Generated by Django 2.2.4 on 2020-02-28 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_organizator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excursion',
            name='organizator',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_organizator', to='app.Organizator'),
        ),
    ]
