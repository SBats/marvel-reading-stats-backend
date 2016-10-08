# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-08 18:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marvelId', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('thumbnail', models.ImageField(upload_to='')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='CharacterEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marvel.Character')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marvel.Character')),
            ],
        ),
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marvelId', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('variantDescription', models.TextField()),
                ('description', models.TextField()),
                ('pageCount', models.PositiveSmallIntegerField()),
                ('url', models.URLField()),
                ('date', models.DateField()),
                ('thumbnail', models.ImageField(upload_to='')),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='ComicCharacter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marvel.Character')),
                ('comic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marvel.Comic')),
            ],
        ),
        migrations.CreateModel(
            name='ComicEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marvel.Comic')),
            ],
        ),
        migrations.CreateModel(
            name='ComicSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marvel.Comic')),
            ],
        ),
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marvelId', models.IntegerField()),
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('suffix', models.CharField(max_length=200)),
                ('fullName', models.CharField(max_length=600)),
                ('url', models.URLField()),
                ('thumbnail', models.ImageField(upload_to='')),
            ],
            options={
                'ordering': ('firstName',),
            },
        ),
        migrations.CreateModel(
            name='CreatorComic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marvel.Comic')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marvel.Creator')),
            ],
        ),
        migrations.CreateModel(
            name='CreatorEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marvel.Creator')),
            ],
        ),
        migrations.CreateModel(
            name='CreatorSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marvel.Creator')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marvelId', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('start', models.PositiveSmallIntegerField()),
                ('end', models.PositiveSmallIntegerField()),
                ('thumbnail', models.ImageField(upload_to='')),
                ('characters', models.ManyToManyField(through='marvel.CharacterEvent', to='marvel.Character')),
                ('comics', models.ManyToManyField(through='marvel.ComicEvent', to='marvel.Comic')),
                ('creators', models.ManyToManyField(through='marvel.CreatorEvent', to='marvel.Creator')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marvelId', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('startYear', models.PositiveSmallIntegerField()),
                ('endYear', models.PositiveSmallIntegerField()),
                ('thumbnail', models.ImageField(upload_to='')),
                ('characters', models.ManyToManyField(through='marvel.CharacterSeries', to='marvel.Character')),
                ('comics', models.ManyToManyField(through='marvel.ComicSeries', to='marvel.Comic')),
                ('creators', models.ManyToManyField(through='marvel.CreatorSeries', to='marvel.Creator')),
                ('events', models.ManyToManyField(related_name='SeriesEvent', to='marvel.Event')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='SeriesEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marvel.Event')),
                ('seriesList', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marvel.Series')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='seriesList',
            field=models.ManyToManyField(through='marvel.SeriesEvent', to='marvel.Series'),
        ),
        migrations.AddField(
            model_name='creatorseries',
            name='seriesList',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marvel.Series'),
        ),
        migrations.AddField(
            model_name='creatorevent',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marvel.Event'),
        ),
        migrations.AddField(
            model_name='creator',
            name='comics',
            field=models.ManyToManyField(through='marvel.CreatorComic', to='marvel.Comic'),
        ),
        migrations.AddField(
            model_name='creator',
            name='events',
            field=models.ManyToManyField(through='marvel.CreatorEvent', to='marvel.Event'),
        ),
        migrations.AddField(
            model_name='creator',
            name='seriesList',
            field=models.ManyToManyField(through='marvel.CreatorSeries', to='marvel.Series'),
        ),
        migrations.AddField(
            model_name='comicseries',
            name='seriesList',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marvel.Series'),
        ),
        migrations.AddField(
            model_name='comicevent',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marvel.Event'),
        ),
        migrations.AddField(
            model_name='comic',
            name='characters',
            field=models.ManyToManyField(through='marvel.ComicCharacter', to='marvel.Character'),
        ),
        migrations.AddField(
            model_name='comic',
            name='creators',
            field=models.ManyToManyField(through='marvel.CreatorComic', to='marvel.Creator'),
        ),
        migrations.AddField(
            model_name='comic',
            name='events',
            field=models.ManyToManyField(through='marvel.ComicEvent', to='marvel.Event'),
        ),
        migrations.AddField(
            model_name='comic',
            name='seriesList',
            field=models.ManyToManyField(through='marvel.ComicSeries', to='marvel.Series'),
        ),
        migrations.AddField(
            model_name='characterseries',
            name='seriesList',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marvel.Series'),
        ),
        migrations.AddField(
            model_name='characterevent',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marvel.Event'),
        ),
        migrations.AddField(
            model_name='character',
            name='comics',
            field=models.ManyToManyField(through='marvel.ComicCharacter', to='marvel.Comic'),
        ),
        migrations.AddField(
            model_name='character',
            name='events',
            field=models.ManyToManyField(through='marvel.CharacterEvent', to='marvel.Event'),
        ),
        migrations.AddField(
            model_name='character',
            name='seriesList',
            field=models.ManyToManyField(through='marvel.CharacterSeries', to='marvel.Series'),
        ),
    ]