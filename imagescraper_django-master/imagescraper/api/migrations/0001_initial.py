# Generated by Django 2.1.4 on 2018-12-21 13:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrawlerUrls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('url', models.URLField(blank=True, max_length=500, null=True)),
                ('depth', models.IntegerField(default=1)),
                ('status', models.BooleanField(default=False)),
                ('createdOn', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['createdOn'],
            },
        ),
        migrations.CreateModel(
            name='ImageUrls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, max_length=500, null=True)),
                ('pageUrl', models.URLField(blank=True, max_length=500, null=True)),
                ('createdOn', models.DateTimeField(default=django.utils.timezone.now)),
                ('parentUrl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.CrawlerUrls', verbose_name='Website Url')),
            ],
            options={
                'ordering': ['createdOn'],
            },
        ),
        migrations.CreateModel(
            name='ScrapedUrls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('url', models.URLField(blank=True, max_length=500, null=True)),
                ('depth', models.IntegerField(default=2)),
                ('createdOn', models.DateTimeField(default=django.utils.timezone.now)),
                ('parentUrl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.CrawlerUrls', verbose_name='Website Url')),
                ('relatedUrl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ScrapedUrls', verbose_name='Website Url')),
            ],
            options={
                'ordering': ['createdOn'],
            },
        ),
    ]
