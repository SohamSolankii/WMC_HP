# Generated by Django 4.2.2 on 2023-07-17 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_category_creatures_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='addplayers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('players_type', models.CharField(choices=[('one', 'chaser'), ('two', 'keeper'), ('three', 'beaters'), ('four', 'seeker')], default='', max_length=15)),
                ('player_name', models.CharField(max_length=30)),
                ('player_image', models.ImageField(default='', upload_to='game/images')),
            ],
        ),
        migrations.CreateModel(
            name='points',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(default='', max_length=30)),
                ('team_image', models.ImageField(default='', upload_to='game/images')),
                ('MATCHES_PLAYED', models.IntegerField(default=0)),
                ('MATCHES_WON', models.IntegerField(default=0)),
                ('MATCHES_DRAW', models.IntegerField(default=0)),
                ('TOTAL_GOALS_SCORED', models.IntegerField(default=0)),
                ('TOTAL_GOALS_AGAINST', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=30)),
                ('teams_trophies', models.IntegerField()),
                ('teams_image', models.ImageField(default='', upload_to='game/images')),
                ('team_owner', models.CharField(default='', max_length=30)),
                ('team_coach', models.CharField(default='', max_length=30)),
                ('team_captain', models.CharField(default='', max_length=30)),
                ('team_home', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='upcoming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team1', models.CharField(max_length=30)),
                ('team2', models.CharField(max_length=30)),
                ('match_venue', models.CharField(default='', max_length=50)),
                ('match_date', models.DateField()),
                ('match_time', models.TimeField()),
                ('match_desc', models.TextField()),
                ('match_image', models.ImageField(default='', upload_to='game/images')),
            ],
        ),
        migrations.RemoveField(
            model_name='creatures',
            name='type',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Creatures',
        ),
        migrations.AddField(
            model_name='addplayers',
            name='team',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.teams'),
        ),
    ]
