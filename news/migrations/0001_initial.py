# Generated by Django 4.0 on 2022-02-07 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='Slug')),
                ('link', models.CharField(max_length=200, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('link', models.CharField(max_length=200, verbose_name='Ссылка')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('time_created', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='news.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['pk'],
            },
        ),
    ]
