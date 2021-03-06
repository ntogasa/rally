# Generated by Django 3.0.3 on 2020-08-24 20:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Expedition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='no title', max_length=200)),
                ('description', models.CharField(default='no description', max_length=200)),
                ('date_published', models.DateField(default=django.utils.timezone.now)),
                ('leader', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Plans',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(default='no description', max_length=1000)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expedition.Expedition')),
            ],
        ),
    ]
