# Generated by Django 4.0.2 on 2022-03-04 14:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('eos', '0002_author_book_bookitem_bookstats_category_publisher_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='biography',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='summary',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='bookitem',
            name='barcode',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='bookitem',
            name='discount',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookitem',
            name='price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookstats',
            name='importPrice',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookstats',
            name='quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookstats',
            name='quantityLeft',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='createdAt',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='publisher',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='numberOfPage',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
