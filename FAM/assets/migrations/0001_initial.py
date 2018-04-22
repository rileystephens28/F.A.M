# Generated by Django 2.0.4 on 2018-04-19 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sources', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cryptocurrency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base', models.CharField(max_length=10)),
                ('quote', models.CharField(max_length=10)),
                ('symbol', models.CharField(max_length=20)),
                ('bid', models.FloatField(default=None, null=True)),
                ('ask', models.FloatField(default=None, null=True)),
                ('last', models.FloatField(default=None, null=True)),
                ('base_volume', models.FloatField(default=None, null=True)),
                ('quote_volume', models.FloatField(default=None, null=True)),
                ('last_updated', models.DateTimeField(default=None, null=True)),
                ('exchange', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sources.CryptoExchange')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('underlying', models.CharField(default=None, max_length=10)),
                ('symbol', models.CharField(max_length=50)),
                ('expiration', models.DateField()),
                ('type', models.CharField(max_length=4)),
                ('strike', models.FloatField()),
                ('bid', models.FloatField()),
                ('ask', models.FloatField()),
                ('last', models.FloatField(default=None)),
                ('volume', models.FloatField(default=None)),
                ('open_interest', models.FloatField(default=None)),
                ('exchange', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sources.OptionExchange')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=500, null=True)),
                ('symbol', models.CharField(max_length=50)),
                ('price', models.FloatField(default=None)),
                ('bid', models.FloatField(default=None)),
                ('ask', models.FloatField(default=None)),
                ('last', models.FloatField(default=None)),
                ('volume', models.FloatField(default=None, null=True)),
                ('high', models.FloatField(default=None, null=True)),
                ('low', models.FloatField(default=None, null=True)),
                ('open_price', models.FloatField(default=None, null=True)),
                ('close_price', models.FloatField(default=None, null=True)),
                ('exchange', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sources.StockExchange')),
            ],
        ),
    ]