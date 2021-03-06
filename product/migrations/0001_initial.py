# Generated by Django 3.1.6 on 2021-02-25 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='DeliveryFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(unique=True)),
            ],
            options={
                'db_table': 'delivery_fees',
            },
        ),
        migrations.CreateModel(
            name='DeliveryPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(unique=True)),
            ],
            options={
                'db_table': 'delivery_periods',
            },
        ),
        migrations.CreateModel(
            name='DeliveryType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True)),
            ],
            options={
                'db_table': 'delivery_types',
            },
        ),
        migrations.CreateModel(
            name='DetailCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'detail_categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True)),
                ('original_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('discount_percentage', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='ProductColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True)),
            ],
            options={
                'db_table': 'product_colors',
            },
        ),
        migrations.CreateModel(
            name='ProductCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True)),
            ],
            options={
                'db_table': 'product_companies',
            },
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('image_url', models.URLField(max_length=2000, null=True)),
                ('rate', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'product_reviews',
            },
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True)),
            ],
            options={
                'db_table': 'product_sizes',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
            options={
                'db_table': 'sub_categories',
            },
        ),
        migrations.CreateModel(
            name='ReviewLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productreview')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'review_likes',
            },
        ),
        migrations.AddField(
            model_name='productreview',
            name='like_user',
            field=models.ManyToManyField(related_name='user_like_review', through='product.ReviewLike', to='user.User'),
        ),
        migrations.AddField(
            model_name='productreview',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AddField(
            model_name='productreview',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
        migrations.CreateModel(
            name='ProductOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productcolor')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productsize')),
            ],
            options={
                'db_table': 'product_options',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField(max_length=2000)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'db_table': 'product_images',
            },
        ),
        migrations.CreateModel(
            name='ProductDelivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.deliveryfee')),
                ('method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.deliverytype')),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.deliveryperiod')),
            ],
            options={
                'db_table': 'product_deliveries',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productcompany'),
        ),
        migrations.AddField(
            model_name='product',
            name='delivery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productdelivery'),
        ),
        migrations.AddField(
            model_name='product',
            name='detail_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.detailcategory'),
        ),
        migrations.AddField(
            model_name='detailcategory',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.subcategory'),
        ),
    ]
