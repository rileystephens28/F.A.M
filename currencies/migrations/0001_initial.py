# Generated by Django 2.0.4 on 2018-11-25 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exchanges', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=10)),
                ('exchange', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exchanges.Exchange')),
            ],
        ),
        migrations.CreateModel(
            name='CurrencyPair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.FloatField(default=None, null=True)),
                ('ask', models.FloatField(default=None, null=True)),
                ('last', models.FloatField(default=None, null=True)),
                ('base_volume', models.FloatField(default=None, null=True)),
                ('quote_volume', models.FloatField(default=None, null=True)),
                ('base', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='base', to='currencies.Currency')),
                ('quote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quote', to='currencies.Currency')),
            ],
        ),
    ]