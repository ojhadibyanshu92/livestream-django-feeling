# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-07-09 14:39
from __future__ import unicode_literals

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
            name='Thought',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recorded_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('condition', models.IntegerField(choices=[(0, 'Ecstatic'), (5, 'Passionate'), (10, 'Happy'), (15, 'Optimistic'), (20, 'Content'), (25, 'Board'), (26, 'Tired'), (27, 'Hungry'), (30, 'Pessimistic'), (35, 'Frustrated'), (40, 'Overwhelmed'), (45, 'Worried'), (50, 'Angry'), (55, 'Jealous'), (60, 'Insecure'), (65, 'Guilty'), (70, 'Fear'), (75, 'Grief'), (80, 'Despair'), (85, 'Paranoid')])),
                ('notes', models.TextField(blank=True, default='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thoughts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-recorded_at'],
            },
        ),
    ]
