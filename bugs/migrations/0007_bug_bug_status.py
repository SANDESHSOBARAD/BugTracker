# Generated by Django 3.0.9 on 2022-05-08 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0006_auto_20220508_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='bug_status',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='bugs.BugStatus'),
        ),
    ]
