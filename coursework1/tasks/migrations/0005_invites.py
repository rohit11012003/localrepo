# Generated by Django 4.2.6 on 2023-12-04 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_team_new_is_team_host'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invites',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('teamname', models.CharField(max_length=255)),
                ('teamhost_name', models.CharField(max_length=255)),
            ],
        ),
    ]