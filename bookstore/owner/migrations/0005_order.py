# Generated by Django 3.2.6 on 2021-09-02 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0004_alter_book_book_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=30)),
                ('status', models.CharField(choices=[('delivered', 'delivered'), ('intransit', 'intransit'), ('cancelled', 'cancelled'), ('ordered', 'ordered')], default='ordered', max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('exp_delivery_date', models.DateField(null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owner.book')),
            ],
        ),
    ]
