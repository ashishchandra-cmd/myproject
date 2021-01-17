# Generated by Django 3.0.4 on 2021-01-17 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_type_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_name', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('team_description', models.TextField()),
                ('team_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trlloapp.Team_Type')),
            ],
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board_title', models.CharField(max_length=200)),
                ('team_visible', models.CharField(choices=[('private', 'Private'), ('public', 'Public')], max_length=20)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trlloapp.Team')),
            ],
        ),
    ]
