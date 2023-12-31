# Generated by Django 4.2.2 on 2023-06-13 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_tracoll', '0005_alter_text_language_alter_text_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this translation', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=2000)),
                ('original_text', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='app_tracoll.text')),
                ('user_translator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['title', 'original_text'],
            },
        ),
    ]
