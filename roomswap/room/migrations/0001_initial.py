# Generated by Django 2.1.4 on 2019-04-26 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostel', models.TextField(choices=[(1, 'HIMGIRI'), (2, 'VIDHYANCHAL'), (3, 'MANIMAHESH')])),
                ('room_no', models.CharField(max_length=8)),
                ('desire', models.TextField(verbose_name='desire')),
                ('contact', models.TextField(verbose_name='Contact')),
            ],
        ),
    ]
