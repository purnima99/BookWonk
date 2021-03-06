# Generated by Django 3.2.3 on 2021-07-14 07:54

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('bookName', models.CharField(max_length=50, verbose_name='Book Name')),
                ('author', models.CharField(max_length=50, verbose_name='Author')),
                ('genre', models.CharField(max_length=20, verbose_name='Genre')),
                ('location', models.CharField(max_length=100, verbose_name='Location')),
                ('titlePgImg', models.CharField(max_length=100, verbose_name='Title Page Image')),
            ],
        ),
    ]
