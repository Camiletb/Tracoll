# Generated by Django 4.2.2 on 2023-06-16 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tracoll', '0014_alter_text_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='status',
            field=models.CharField(choices=[('W', 'Not translated'), ('L', 'Not reviewed'), ('E', 'Reviewed'), ('V', 'Translated')], default='W', help_text='Enter the translation status', max_length=1),
        ),
    ]