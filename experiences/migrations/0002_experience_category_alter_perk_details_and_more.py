# Generated by Django 4.1.4 on 2023-01-23 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('experiences', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.category'),
        ),
        migrations.AlterField(
            model_name='perk',
            name='details',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='perk',
            name='explanation',
            field=models.TextField(blank=True, default=''),
        ),
    ]
