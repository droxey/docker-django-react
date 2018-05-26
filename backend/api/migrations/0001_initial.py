# Generated by Django 2.0.5 on 2018-05-23 06:19

import api.models
import autoslug.fields
import colorfield.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title for this Example.', max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
                ('introduction', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(help_text='The User that created this Example.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Syntax Example',
                'verbose_name_plural': 'Syntax Examples',
                'get_latest_by': 'created_on',
            },
        ),
        migrations.CreateModel(
            name='Highlight',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('bkg_color', colorfield.fields.ColorField(default='#000000', max_length=18)),
                ('text_color', colorfield.fields.ColorField(default='#FFFFFF', max_length=18)),
                ('code', models.TextField(help_text='The exact code to highlight in the referenced Snippet.')),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(help_text='The User that created this Highlight.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Syntax Highlight',
                'verbose_name_plural': 'Syntax Highlights',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the Language. Example: Python.', max_length=64)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=api.models.Language._get_name, slugify=api.models.Language._get_slug)),
                ('notes', models.TextField(blank=True, null=True)),
                ('homepage', models.URLField(blank=True, help_text='The homepage for this Language.', max_length=255, null=True)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(help_text='The User that created this Language.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Programming Language',
                'verbose_name_plural': 'Programming Languages',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title for this Snippet.', max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
                ('code', models.TextField(help_text='The full code for this Snippet.')),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(help_text='The User that created this Snippet.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('example', models.ForeignKey(help_text='The Example associated with this Snippet.', on_delete=django.db.models.deletion.CASCADE, to='api.Example')),
                ('language', models.ForeignKey(help_text='The Language associated with this Snippet.', on_delete=django.db.models.deletion.CASCADE, to='api.Language')),
            ],
            options={
                'verbose_name': 'Syntax Snippet',
                'verbose_name_plural': 'Syntax Snippets',
            },
        ),
        migrations.AddField(
            model_name='highlight',
            name='snippet',
            field=models.ForeignKey(help_text='The Snippet associated with this Highlight.', on_delete=django.db.models.deletion.CASCADE, to='api.Snippet'),
        ),
        migrations.AddField(
            model_name='example',
            name='language',
            field=models.ForeignKey(help_text='The Language associated with this Example.', on_delete=django.db.models.deletion.CASCADE, to='api.Language'),
        ),
        migrations.AlterOrderWithRespectTo(
            name='snippet',
            order_with_respect_to='example',
        ),
        migrations.AlterOrderWithRespectTo(
            name='highlight',
            order_with_respect_to='snippet',
        ),
    ]
