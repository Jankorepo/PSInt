# Generated by Django 3.1.3 on 2020-11-23 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pracownik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.DecimalField(decimal_places=0, max_digits=5)),
                ('imie', models.CharField(max_length=60)),
                ('nazwisko', models.CharField(max_length=60)),
                ('login', models.CharField(max_length=32)),
                ('haslo_hash', models.CharField(max_length=256)),
                ('pensja_podstawowa', models.DecimalField(decimal_places=2, default=2800, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Salon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.DecimalField(decimal_places=0, max_digits=5)),
                ('miasto', models.CharField(max_length=45)),
                ('adres', models.CharField(max_length=45)),
                ('kierownik_id', models.ManyToManyField(to='salonyFryzjerskie.Pracownik')),
            ],
        ),
        migrations.CreateModel(
            name='Stanowisko',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.DecimalField(decimal_places=0, max_digits=5)),
                ('nazwa', models.CharField(max_length=45)),
                ('tworzy_uzytkownika', models.BooleanField()),
                ('modyfikuje_uzytkownika', models.BooleanField()),
                ('usuwa_uzytkowinka', models.BooleanField()),
                ('tworzy_spotkanie', models.BooleanField()),
                ('modyfikuje_spotkanie', models.BooleanField()),
                ('usuwa_spotkanie', models.BooleanField()),
                ('wyswietla_spotkanie', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Wizyta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.DecimalField(decimal_places=0, max_digits=5)),
                ('data', models.DateField()),
                ('pracownicy_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='salonyFryzjerskie.pracownik')),
                ('salony_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='salonyFryzjerskie.salon')),
            ],
        ),
        migrations.AddField(
            model_name='pracownik',
            name='salony_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='salonyFryzjerskie.salon'),
        ),
        migrations.AddField(
            model_name='pracownik',
            name='stanowiska_id',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='salonyFryzjerskie.stanowisko'),
        ),
    ]