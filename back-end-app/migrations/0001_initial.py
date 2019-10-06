# Generated by Django 2.2.5 on 2019-10-06 00:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('created_at', models.TimeField(auto_now_add=True)),
                ('updated_at', models.TimeField(auto_now=True)),
                ('deleted_at', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.TimeField(auto_now_add=True)),
                ('updated_at', models.TimeField(auto_now=True)),
                ('deleted_at', models.TimeField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('created_at', models.TimeField(auto_now_add=True)),
                ('updated_at', models.TimeField(auto_now=True)),
                ('deleted_at', models.TimeField()),
                ('usd_price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('real_price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('euro_price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='back-end-app.Categories')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItens',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.TimeField(auto_now_add=True)),
                ('updated_at', models.TimeField(auto_now=True)),
                ('usd_price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('real_price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('euro_price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='back-end-app.Order')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='back-end-app.Products')),
            ],
        ),
    ]
