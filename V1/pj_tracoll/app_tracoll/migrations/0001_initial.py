# Generated by Django 4.2.2 on 2023-06-12 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('PO', 'Poet'), ('SI', 'Singer'), ('BA', 'Band')], default='SI', max_length=2)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name', 'type'],
            },
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('PO', 'Poem'), ('SO', 'Song')], default='SO', max_length=2)),
                ('language', models.CharField(choices=[('ES', 'ES'), ('FR', 'FR'), ('EN', 'EN')], max_length=2)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=2000)),
                ('state', models.CharField(choices=[('W', '(W) Not translated'), ('L', '(L) Translated & Not reviewed'), ('E', ' (E) Reviewed & Editable'), ('W', ' (V) Translated')], default='W', max_length=1)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_tracoll.author')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
