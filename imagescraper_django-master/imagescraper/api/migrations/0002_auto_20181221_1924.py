# Generated by Django 2.1.4 on 2018-12-21 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageurls',
            name='pageUrl',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.ScrapedUrls', verbose_name='Image Page Url'),
        ),
    ]
