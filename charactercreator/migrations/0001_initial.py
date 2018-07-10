# Generated by Django 2.0.2 on 2018-07-10 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('armory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('character_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, verbose_name="Character's name")),
                ('level', models.IntegerField(default=0)),
                ('exp', models.IntegerField(default=0)),
                ('hp', models.IntegerField(default=10)),
                ('strength', models.IntegerField(default=1)),
                ('intelligence', models.IntegerField(default=1)),
                ('dexterity', models.IntegerField(default=1)),
                ('wisdom', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Cleric',
            fields=[
                ('character_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='charactercreator.Character')),
                ('using_shield', models.BooleanField(default=False)),
                ('mana', models.IntegerField(default=100)),
            ],
            bases=('charactercreator.character',),
        ),
        migrations.CreateModel(
            name='Fighter',
            fields=[
                ('character_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='charactercreator.Character')),
                ('using_shield', models.BooleanField(default=False)),
                ('rage', models.IntegerField(default=100)),
            ],
            bases=('charactercreator.character',),
        ),
        migrations.CreateModel(
            name='Mage',
            fields=[
                ('character_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='charactercreator.Character')),
                ('has_pet', models.BooleanField(default=True)),
                ('mana', models.IntegerField(default=100)),
            ],
            bases=('charactercreator.character',),
        ),
        migrations.CreateModel(
            name='Thief',
            fields=[
                ('character_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='charactercreator.Character')),
                ('is_sneaking', models.BooleanField(default=False)),
                ('energy', models.IntegerField(default=100)),
            ],
            bases=('charactercreator.character',),
        ),
        migrations.AddField(
            model_name='character',
            name='inventory',
            field=models.ManyToManyField(to='armory.Item', verbose_name='Items the character has'),
        ),
        migrations.CreateModel(
            name='Necromancer',
            fields=[
                ('mage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='charactercreator.Mage')),
                ('talisman_charged', models.BooleanField(default=True)),
            ],
            bases=('charactercreator.mage',),
        ),
    ]
