from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_course', '0010_merge_20261014_2230'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sitesettings',
            options={
                'verbose_name': 'لینک تلگرام',
                'verbose_name_plural': 'لینک تلگرام',
            },
        ),
    ]
