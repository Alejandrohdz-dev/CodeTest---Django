# Generated by Django 3.1.4 on 2020-12-19 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MasterProductsConfigurable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('model', models.TextField(blank=True, null=True)),
                ('group_by_model', models.TextField(blank=True, null=True)),
                ('sku', models.TextField(blank=True, null=True)),
                ('yr_es', models.TextField(blank=True, db_column='YR_es', null=True)),
                ('yr_fr', models.TextField(blank=True, db_column='YR_fr', null=True)),
                ('name_single_product', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('qty', models.TextField(blank=True, null=True)),
                ('ean1', models.TextField(blank=True, null=True)),
                ('color_group_hex', models.TextField(blank=True, null=True)),
                ('color_child', models.TextField(blank=True, null=True)),
                ('status', models.TextField(blank=True, null=True)),
                ('weight', models.TextField(blank=True, null=True)),
                ('brand', models.TextField(blank=True, null=True)),
                ('price', models.TextField(blank=True, null=True)),
                ('special_price', models.TextField(blank=True, null=True)),
                ('short_description', models.TextField(blank=True, null=True)),
                ('long_description', models.TextField(blank=True, null=True)),
                ('cross_selling', models.TextField(blank=True, null=True)),
                ('cross_selling_cart', models.TextField(blank=True, null=True)),
                ('size_chart', models.TextField(blank=True, null=True)),
                ('image1', models.TextField(blank=True, null=True)),
                ('image2', models.TextField(blank=True, null=True)),
                ('image3', models.TextField(blank=True, null=True)),
                ('image4', models.TextField(blank=True, null=True)),
                ('image5', models.TextField(blank=True, null=True)),
                ('image6', models.TextField(blank=True, null=True)),
                ('image7', models.TextField(blank=True, null=True)),
                ('image8', models.TextField(blank=True, null=True)),
                ('image9', models.TextField(blank=True, null=True)),
                ('application_advice', models.TextField(blank=True, null=True)),
                ('attribute_format_container', models.TextField(blank=True, null=True)),
                ('vegetal_active', models.TextField(blank=True, null=True)),
                ('attribute_container', models.TextField(blank=True, null=True)),
                ('attribute_coverage', models.TextField(blank=True, null=True)),
                ('inci', models.TextField(blank=True, null=True)),
                ('variant_icon', models.TextField(blank=True, null=True)),
                ('attribute_face', models.TextField(blank=True, null=True)),
                ('attribute_esencia', models.TextField(blank=True, null=True)),
                ('attribute_line', models.TextField(blank=True, null=True)),
                ('attribute_hair_type', models.TextField(blank=True, null=True)),
                ('attribute_type_perfume', models.TextField(blank=True, null=True)),
                ('attribute_effect', models.TextField(blank=True, null=True)),
                ('attribute_texture', models.TextField(blank=True, null=True)),
                ('attribute_type_skin', models.TextField(blank=True, null=True)),
                ('attribute_zone', models.TextField(blank=True, null=True)),
                ('attribute_color', models.TextField(blank=True, null=True)),
                ('attribute_ip_solar', models.TextField(blank=True, null=True)),
                ('attribute_action', models.TextField(blank=True, null=True)),
                ('attribute_class', models.TextField(blank=True, null=True)),
                ('attribute_type_product', models.TextField(blank=True, null=True)),
                ('attribute_type_care', models.TextField(blank=True, null=True)),
                ('attribute_need', models.TextField(blank=True, null=True)),
                ('category_1_1', models.TextField(blank=True, null=True)),
                ('category_1_2', models.TextField(blank=True, null=True)),
                ('category_1_3', models.TextField(blank=True, null=True)),
                ('category_2_1', models.TextField(blank=True, null=True)),
                ('category_2_2', models.TextField(blank=True, null=True)),
                ('category_2_3', models.TextField(blank=True, null=True)),
                ('category_3_1', models.TextField(blank=True, null=True)),
                ('category_3_2', models.TextField(blank=True, null=True)),
                ('category_3_3', models.TextField(blank=True, null=True)),
                ('category_4_1', models.TextField(blank=True, null=True)),
                ('category_4_2', models.TextField(blank=True, null=True)),
                ('category_4_3', models.TextField(blank=True, null=True)),
                ('category_5_1', models.TextField(blank=True, null=True)),
                ('category_5_2', models.TextField(blank=True, null=True)),
                ('category_5_3', models.TextField(blank=True, null=True)),
                ('category_6_1', models.TextField(blank=True, null=True)),
                ('category_6_2', models.TextField(blank=True, null=True)),
                ('category_6_3', models.TextField(blank=True, null=True)),
                ('category_7_1', models.TextField(blank=True, null=True)),
                ('category_7_2', models.TextField(blank=True, null=True)),
                ('category_7_3', models.TextField(blank=True, null=True)),
                ('category_8_1', models.TextField(blank=True, null=True)),
                ('category_8_2', models.TextField(blank=True, null=True)),
                ('category_8_3', models.TextField(blank=True, null=True)),
                ('category_9_1', models.TextField(blank=True, null=True)),
                ('category_9_2', models.TextField(blank=True, null=True)),
                ('category_9_3', models.TextField(blank=True, null=True)),
                ('category_10_1', models.TextField(blank=True, null=True)),
                ('category_10_2', models.TextField(blank=True, null=True)),
                ('category_10_3', models.TextField(blank=True, null=True)),
                ('category_11_1', models.TextField(blank=True, null=True)),
                ('category_11_2', models.TextField(blank=True, null=True)),
                ('category_11_3', models.TextField(blank=True, null=True)),
                ('category_12_1', models.TextField(blank=True, null=True)),
                ('category_12_2', models.TextField(blank=True, null=True)),
                ('category_12_3', models.TextField(blank=True, null=True)),
                ('category_13_1', models.TextField(blank=True, null=True)),
                ('category_13_2', models.TextField(blank=True, null=True)),
                ('category_13_3', models.TextField(blank=True, null=True)),
                ('category_14_1', models.TextField(blank=True, null=True)),
                ('category_14_2', models.TextField(blank=True, null=True)),
                ('category_14_3', models.TextField(blank=True, null=True)),
                ('attribute_beauty', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'master_products_configurable',
                'managed': True,
            },
        ),
    ]
