# Generated by Django 5.0.2 on 2024-02-12 08:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentStatuses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='RetreatCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='RetreatPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/img/retreats/')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('surname', models.CharField(max_length=15)),
                ('telephone', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=254)),
                ('password_hash', models.CharField(max_length=15)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('links_media', models.TextField()),
                ('avatar', models.ImageField(upload_to='static/img/avatars/')),
            ],
        ),
        migrations.CreateModel(
            name='UserStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=128)),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_market_app.cities')),
                ('country_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_market_app.countries')),
            ],
        ),
        migrations.CreateModel(
            name='Retreats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('links_preview', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('date_start', models.DateTimeField()),
                ('date_stop', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('retreat_form', models.BooleanField()),
                ('rating', models.DecimalField(decimal_places=1, default=5.0, max_digits=2)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_market_app.retreatcategories')),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_market_app.locations')),
                ('photo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_market_app.retreatphotos')),
                ('tags', models.ManyToManyField(to='web_market_app.tags')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_market_app.users')),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('status_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_market_app.paymentstatuses')),
                ('retreat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_market_app.retreats')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_market_app.users')),
            ],
        ),
        migrations.CreateModel(
            name='Feedbacks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('retreat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_market_app.retreats')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_market_app.users')),
            ],
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('retreat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_market_app.retreats')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_market_app.users')),
            ],
        ),
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('tickets_amount', models.IntegerField()),
                ('booking_coast', models.DecimalField(decimal_places=2, max_digits=8)),
                ('retreat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_market_app.retreats')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_market_app.users')),
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='status_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_market_app.userstatus'),
        ),
    ]
