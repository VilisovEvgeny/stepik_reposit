# Generated by Django 3.0.4 on 2020-03-11 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='фамилия')),
                ('birth_date', models.DateField(verbose_name='дата рождения')),
                ('city', models.CharField(max_length=30, verbose_name='город')),
            ],
            options={
                'verbose_name': 'автор',
                'verbose_name_plural': 'авторы',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='название жанра')),
            ],
            options={
                'verbose_name': 'жанр',
                'verbose_name_plural': 'жанры',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='заголовок')),
                ('publish_date', models.DateField(verbose_name='дата публикации')),
                ('authors', models.ManyToManyField(related_name='author_books', to='library.Author', verbose_name='авторы')),
                ('genres', models.ManyToManyField(related_name='genre_books', to='library.Genre', verbose_name='жанры')),
            ],
            options={
                'verbose_name': 'книга',
                'verbose_name_plural': 'книги',
            },
        ),
    ]