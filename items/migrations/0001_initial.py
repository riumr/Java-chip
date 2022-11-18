# Generated by Django 3.2.13 on 2022-11-18 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutThisCoffee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FactSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fieldname', models.TextField()),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.TextField()),
                ('image_url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MainImageUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urls', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ItemPicked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smashed', models.TextField()),
                ('volume', models.TextField()),
                ('amount', models.IntegerField()),
                ('picked_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.item')),
            ],
        ),
        migrations.CreateModel(
            name='ItemDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_title', models.TextField()),
                ('header_image', models.TextField()),
                ('main_text_title', models.TextField()),
                ('main_text_content', models.TextField()),
                ('about_this_coffee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.aboutthiscoffee')),
                ('fact_sheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.factsheet')),
                ('main_images_url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.mainimageurl')),
            ],
        ),
    ]
