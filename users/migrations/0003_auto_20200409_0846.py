# Generated by Django 3.0.4 on 2020-04-09 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200408_1516'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['group', '?']},
        ),
        migrations.AddField(
            model_name='tag',
            name='index',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tag',
            name='group',
            field=models.CharField(choices=[('hobbies', 'Хобби'), ('personal', 'Личное'), ('other', 'Остальное')], default='other', max_length=32),
        ),
    ]
