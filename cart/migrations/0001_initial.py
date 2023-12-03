import django.db.models.deletion
from django.db import migrations, models


def fix_foreign_keys(apps, schema_editor):
    CartItem = apps.get_model('cart', 'CartItem')  # Replace 'cart' with the actual app name
    Product = apps.get_model('shop', 'Product')  # Replace 'shop' with the actual app name

    # Update the product field with a valid value (replace 1 with a valid product id)
    valid_product = Product.objects.first()  # Replace this with a valid product query
    CartItem.objects.filter(product__name='Black Urban').update(product=valid_product)


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cart_id", models.CharField(blank=True, max_length=250)),
                ("date_added", models.DateField(auto_now_add=True)),
            ],
            options={
                "db_table": "Cart",
                "ordering": ["date_added"],
            },
        ),
        migrations.CreateModel(
            name="CartItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveIntegerField()),
                ("active", models.BooleanField(default=True)),
                (
                    "cart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cart.cart"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="shop.product"
                    ),
                ),
            ],
            options={
                "db_table": "CartItem",
            },
        ),

        # Add the RunPython operation here
        migrations.RunPython(fix_foreign_keys),
    ]
