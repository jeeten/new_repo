# Generated by Django 2.2.1 on 2019-05-17 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('brandid', models.AutoField(db_column='BrandId', primary_key=True, serialize=False)),
                ('companyid', models.IntegerField(db_column='CompanyId')),
                ('brandname', models.CharField(db_column='BrandName', max_length=200)),
                ('brandlogo', models.CharField(blank=True, db_column='BrandLogo', max_length=200, null=True)),
                ('status', models.IntegerField(db_column='Status')),
                ('addeddate', models.DateTimeField(db_column='AddedDate')),
                ('lastupdateddate', models.DateTimeField(db_column='LastUpdatedDate')),
            ],
            options={
                'db_table': 'Brand',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('categoryid', models.AutoField(db_column='CategoryId', primary_key=True, serialize=False)),
                ('industryid', models.IntegerField(db_column='IndustryId')),
                ('categoryname', models.CharField(db_column='CategoryName', max_length=200)),
                ('parentid', models.IntegerField(db_column='ParentId')),
                ('categorylevel', models.IntegerField(db_column='CategoryLevel')),
                ('categoryicon', models.CharField(blank=True, db_column='CategoryIcon', max_length=255, null=True)),
                ('categorytype', models.IntegerField(db_column='CategoryType')),
                ('status', models.IntegerField(db_column='Status')),
                ('addeddate', models.DateTimeField(db_column='AddedDate')),
                ('lastupdateddate', models.DateTimeField(db_column='LastUpdatedDate')),
                ('categorycode', models.IntegerField(blank=True, db_column='CategoryCode', null=True)),
                ('foodcoupon', models.IntegerField(blank=True, db_column='FoodCoupon', null=True)),
                ('aliasname', models.CharField(blank=True, db_column='AliasName', max_length=1000, null=True)),
                ('weightage', models.CharField(blank=True, db_column='Weightage', max_length=20, null=True)),
                ('sortorder', models.IntegerField(blank=True, db_column='SortOrder', null=True)),
                ('categorydepth', models.IntegerField(blank=True, db_column='CategoryDepth', null=True)),
                ('isb2b', models.IntegerField()),
            ],
            options={
                'db_table': 'Category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('stateid', models.IntegerField(db_column='StateId')),
                ('cityname', models.CharField(db_column='CityName', max_length=100)),
                ('citycode', models.CharField(blank=True, db_column='CityCode', max_length=100, null=True)),
                ('status', models.IntegerField(db_column='Status')),
                ('addeddate', models.DateTimeField(db_column='AddedDate')),
                ('lastupdateddate', models.DateTimeField(db_column='LastUpdatedDate')),
                ('cityid', models.AutoField(db_column='CityId', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'City',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('companyid', models.AutoField(db_column='CompanyId', primary_key=True, serialize=False)),
                ('companyname', models.CharField(db_column='CompanyName', max_length=200)),
                ('companylogo', models.CharField(blank=True, db_column='CompanyLogo', max_length=200, null=True)),
                ('status', models.IntegerField(db_column='Status')),
                ('addeddate', models.DateTimeField(db_column='AddedDate')),
                ('lastupdateddate', models.DateTimeField(db_column='LastUpdatedDate')),
            ],
            options={
                'db_table': 'Company',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('countryid', models.AutoField(db_column='CountryId', primary_key=True, serialize=False)),
                ('countryname', models.CharField(db_column='CountryName', max_length=200)),
                ('countrycode', models.CharField(db_column='CountryCode', max_length=50)),
                ('countryflagimage', models.CharField(blank=True, db_column='CountryFlagImage', max_length=100, null=True)),
                ('status', models.IntegerField(db_column='Status')),
                ('addeddate', models.DateTimeField(db_column='AddedDate')),
                ('lastupdateddate', models.DateTimeField(db_column='LastUpdatedDate')),
            ],
            options={
                'db_table': 'Country',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Productbarcode',
            fields=[
                ('productbarcodeid', models.AutoField(db_column='ProductBarcodeId', primary_key=True, serialize=False)),
                ('productskuid', models.IntegerField(db_column='ProductSKUId')),
                ('barcode', models.CharField(blank=True, db_column='Barcode', max_length=50, null=True)),
                ('addeddate', models.DateTimeField(db_column='AddedDate')),
                ('lastupdateddate', models.DateTimeField(db_column='LastUpdatedDate')),
                ('source', models.IntegerField(blank=True, null=True)),
                ('sourceinfo', models.CharField(blank=True, max_length=3000, null=True)),
            ],
            options={
                'db_table': 'ProductBarcode',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Name', max_length=125)),
                ('price', models.FloatField(db_column='Price')),
                ('createddate', models.DateTimeField(db_column='CreatedDate')),
            ],
            options={
                'db_table': 'product_product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Productsku',
            fields=[
                ('productskuid', models.AutoField(db_column='ProductSKUId', primary_key=True, serialize=False)),
                ('productid', models.IntegerField(db_column='ProductId')),
                ('productsku', models.CharField(db_column='ProductSKU', max_length=100)),
                ('productskuuqcid', models.IntegerField(db_column='ProductSKUUQCId')),
                ('productimage', models.CharField(db_column='ProductImage', max_length=200)),
                ('status', models.IntegerField(db_column='Status')),
                ('addeddate', models.DateTimeField(db_column='AddedDate')),
                ('lastupdateddate', models.DateTimeField(db_column='LastUpdatedDate')),
                ('isrecommended', models.IntegerField(db_column='IsRecommended')),
                ('hsnc', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'ProductSKU',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Productskuprices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productskupriceid', models.IntegerField()),
                ('productskuid', models.IntegerField()),
                ('programid', models.IntegerField()),
                ('productmrp', models.DecimalField(decimal_places=2, max_digits=7)),
                ('productsp', models.DecimalField(decimal_places=2, max_digits=7)),
                ('taxaggregationid', models.IntegerField()),
                ('status', models.IntegerField()),
                ('addeddate', models.DateTimeField()),
                ('lastupdateddate', models.DateTimeField()),
                ('productbarcodeid', models.IntegerField(blank=True, null=True)),
                ('adcamount', models.IntegerField(blank=True, null=True)),
                ('channel', models.IntegerField()),
                ('productpp', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
            options={
                'db_table': 'productskuprices',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Productskupricestatewise',
            fields=[
                ('productskupricestatewiseid', models.AutoField(db_column='ProductSKUPriceStatewiseId', primary_key=True, serialize=False)),
                ('stateid', models.IntegerField(db_column='StateId')),
                ('productskuid', models.IntegerField(db_column='ProductSKUId')),
                ('productmrp', models.DecimalField(db_column='ProductMRP', decimal_places=2, max_digits=7)),
                ('cessrate', models.IntegerField(db_column='CessRate')),
                ('addeddate', models.DateTimeField(db_column='AddedDate')),
                ('lastupdateddate', models.DateTimeField(db_column='LastUpdatedDate')),
                ('adcamount', models.DecimalField(db_column='ADCAmount', decimal_places=5, max_digits=7)),
                ('status', models.IntegerField(db_column='Status')),
                ('hsncode', models.CharField(blank=True, db_column='HSNCode', max_length=20, null=True)),
                ('cgstrate', models.DecimalField(db_column='CGSTRate', decimal_places=2, max_digits=4)),
                ('sgstrate', models.DecimalField(db_column='SGSTRate', decimal_places=2, max_digits=4)),
                ('igstrate', models.DecimalField(db_column='IGSTRate', decimal_places=1, max_digits=3)),
                ('exemptedflag', models.IntegerField(db_column='ExemptedFlag')),
                ('productsp', models.DecimalField(blank=True, db_column='ProductSP', decimal_places=9, max_digits=14, null=True)),
            ],
            options={
                'db_table': 'ProductSKUPriceStatewise',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Productskuuqc',
            fields=[
                ('productskuuqcid', models.AutoField(db_column='ProductSKUUQCId', primary_key=True, serialize=False)),
                ('productskuuqcfullname', models.CharField(db_column='ProductSKUUQCFullName', max_length=20)),
                ('productskuuqcshortname', models.CharField(db_column='ProductSKUUQCShortName', max_length=10)),
                ('addeddate', models.DateTimeField(db_column='AddedDate')),
                ('lastupdateddate', models.DateTimeField(db_column='LastUpdatedDate')),
                ('measurement', models.CharField(blank=True, db_column='Measurement', max_length=100, null=True)),
                ('level', models.IntegerField(blank=True, db_column='Level', null=True)),
            ],
            options={
                'db_table': 'ProductSKUUQC',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'managed': False},
        ),
    ]