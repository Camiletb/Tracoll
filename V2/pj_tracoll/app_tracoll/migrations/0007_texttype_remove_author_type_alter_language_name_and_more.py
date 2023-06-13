# Generated by Django 4.2.2 on 2023-06-13 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_tracoll', '0006_translation'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the text typology: poem, song...', max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.RemoveField(
            model_name='author',
            name='type',
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(help_text='Enter the language', max_length=200),
        ),
        migrations.AlterField(
            model_name='text',
            name='content',
            field=models.TextField(help_text='Enter the text you want translate [Max. 2000 letters]', max_length=2000),
        ),
        migrations.AlterField(
            model_name='text',
            name='language',
            field=models.ForeignKey(blank=True, help_text='Enter the original language', null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_tracoll.language'),
        ),
        migrations.AlterField(
            model_name='text',
            name='state',
            field=models.CharField(choices=[('W', '(W) Not translated'), ('L', '(L) Translated & Not reviewed'), ('E', ' (E) Reviewed & Editable'), ('W', ' (V) Translated')], default='W', help_text='Enter the translation state', max_length=1),
        ),
        migrations.AlterField(
            model_name='text',
            name='title',
            field=models.CharField(help_text='Enter the title [Max. 100 letters]', max_length=100),
        ),
        migrations.AlterField(
            model_name='text',
            name='type',
            field=models.ForeignKey(blank=True, help_text='Enter the type of text', null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_tracoll.texttype'),
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]
