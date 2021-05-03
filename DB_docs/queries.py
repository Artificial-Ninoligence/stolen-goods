"""
### SQL QUERIES ###

# 1. Creating an object in Django Web Framework
# (Django) CustomUser ===> (SQL) accounts_customuser table 

# SQL syntax:
CREATE TABLE accounts_customuser (
    id BIGINT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    password VARCHAR(128) NOT NULL,
    is_admin BOOL DEFAULT 'False',
    is_staff BOOL DEFAULT 'False',
    is_superadmin BOOL DEFAULT 'False',
    is_active BOOL DEFAULT 'False',
    date_joined datetime GETDATE(),
    last_login datetime GETDATE(),
);

CREATE TABLE accounts_userprofile (
    id BIGINT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    dates_of_birth date,
    address_line_1 VARCHAR(255),
    address_line_2 VARCHAR(255),
    profile_picture VARCHAR(100),
    postal_code VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    country VARCHAR(255),
    is_active BOOL DEFAULT 'False',
    date_created datetime GETDATE(),
    date_updated datetime GETDATE(),
    FOREIGN KEY(accounts_customuser_id) INT UNIQUE FOREIGN KEY REFERENCES accounts_customuser(ID)
);
"""

# ORM Syntax in Django:
"""
class Migration(migrations.Migration):

   initial = True
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_superadmin', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dates_of_birth', models.DateField(blank=True, null=True, verbose_name='DoB')),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='Phone Number')),
                ('address_line_1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address Line 1')),
                ('address_line_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='address Line 2')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to=accounts.models.image_storage_path, verbose_name='Profile Picture')),
                ('postal_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='Postal Code')),
                ('city', models.CharField(blank=True, max_length=255, null=True, verbose_name='City')),
                ('state', models.CharField(blank=True, max_length=255, null=True, verbose_name='State')),
                ('country', models.CharField(blank=True, max_length=255, null=True, verbose_name='Country')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
                'ordering': ['-date_created'],
            },
        ),
    ]


# 2. Database Queries (accounts/views.py):

# a. Creating a user
# In Python:
user = CustomUser.objects.create_user(
    first_name="John",
    last_name="Doe",
    email="john.doe@gmail.com",
    username="johndoe",
    password="aiueo123!"
    )
user.save()

# In SQL:
# INSERT INTO accounts_customuser
#            (id,
#             first_name,
#             last_name="Doe",
#             email="john.doe@gmail.com",
#             username="johndoe",
#             password="aiueo123!"
#            );
# VALUES(1,
#        "John",
#        "Doe",
#        "john.doe@gmail.com",
#        "johndoe",
#        "aiueo123!"
#        );
# -----------------------------------------------------

# b. Automatically creating UserProfile data when a new CustomUser data is created:
# In Python:
profile = UserProfile()
profile.user_id = user.id
profile.profile_picture = 'avatar/default-avatar.png'
profile.save()

# In SQL:
# INSERT INTO accounts_userprofile
#            (id,
#             profile_picture
#            );
# VALUES (1,
#         '/Users/ninovationlab/projects/django-ecommerce/media/avatar/default-avatar.png'
#        );
# -------------------------------------------------------

# c. Set a new pasword for CustomUser:
# In Python:
user = User.objects.get(username__exact=request.user.username)
user.set_password(new_password)
user.save()

# In SQL:
# SELECT username FROM accounts_customuser WHERE username = auth_user.username;
# 
# UPDATE account_customuser
# SET password = `new_password`
# -----------------------------------------------------------

# d. OrderProduct and Order
# In Python
order = Order.objects.get(user=request.user, is_ordered=False, order_number=body['orderID'])
order_detail = OrderProduct.objects.filter(order__order_number=order_id)
order = Order.objects.get(order_number=order_id)


# In SQL:
# SELECT * FROM transactions_order
# WHERE transactions_order.accounts_customuser_id=accounts_customuser.id

# SELECT order_number FROM transactions_orderproduct
# INNER JOIN transactions_order
# ON transactions_orderproduct.id=transactions_order.id

# SELECT order_number FROM transactions_order 
# WHERE order_number=id
# ----------------------------------------------------------------------

# 3. CartItem
# In Python:
current_user = request.user
cart_items = CartItem.objects.filter(user=current_user)

# In SQL:
# SELECT * FROM transactions.cartitem 
# WHERE accounts_customuser_id = acounts_customer.id
# ----------------------------------------------------------

# 4. Getting all products with ascending order based on the id
# In Python:
products = Product.objects.all().filter(is_available=True).order_by('id')

# In SQL:
# SELECT * FROM product_product 
# WHERE is_available='True'
# ORDER BY id

# 5. Deleting CartItem
# In Python:
cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
cart_item.delete()

# In SQL:
# SELECT * FROM carts_cartitem
# WHERE carts_cartitem.product_product_id=product_product.id
# AND carts_cartitem.carts_cart_id=carts_cart.id
# ------------------------------------------------------------------

# 6. INDEX
# Table: accounts_userprofile
# Index: date_created in descending order
class UserProfile(models.Model):
    ...
    class Meta:
        ordering = ('-date_created')

# Table: carts_cartitem
# Index: is_active
class CartItem(models.Model):
    ...
    class Meta:
        ordering = ('is_active')

# Table: product_product
# Index: date_created in descending order
class Product(models.Model):
    ...
    class Meta:
        ordering = ('-date_created')

# Table: transactions_payment
# Index: date_created in descending order
#        status in descending order
#        payment_id in descending order
class Payment(models.Model):
    ...
    class Meta:
        ordering = ('-date_created', '-status', '-payment_id',)

# Table: transactions_order
# Index: date_created in descending order
class Order(models.Model):
    ...
    class Meta:
        ordering = ('-date_created')

# Table: transactions_orderproduct
# Index: date_created in descending order
class OrderProduct(models.Model):
    ...
    class Meta:
        ordering = ('-date_created')
"""