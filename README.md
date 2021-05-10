[![Django Project CI/CD](https://github.com/Artificial-Ninoligence/stolen-goods/actions/workflows/ci-cd.yml/badge.svg?branch=main&event=push)](https://github.com/Artificial-Ninoligence/stolen-goods/actions/workflows/ci-cd.yml)

#  **Stolen Goods** | https://www.stolengoods.wtf
![alt sg-banner](docs/doc-stolengoods-banner.png)

# 1. Project Details:
## University:
* Code University of Applied Sciences
## Semester:
* Spring Semester 2021

## Module Details:
* Module Coordinator: Dr. Adam Roe
* Modules:
  * SE01: Software Development Basic
  * SE19: Web Technology Basic
* Module Coordinator: Prof. Dr. Peter Ruppel
* Module:
  * SE05: Relational Database
* Module Coordinator: Prof. Dr. Ulrich von Zadow
* Module:
  * E10: Automated SOftware Testing

## Technical Details:
* Programming Language:
  * Python 3.9.2
  * Javascript
  
* NOT Programming Language:
  * HTML
  * CSS

* Web Framework:
  * Django 3.2
  * Bootstrap 5

* Testing Framework:
  * Django pytest
  * Pytest
  * Coverage
  * Pytest-Cov

* Database:
  * Development Stage (Localhost):
    * SQLite3
    * PostgreSQL 13
  * Production Stage:
    * AWS RDS PostgreSQL 12.6

* Static Files Storage System:
  * AWS S3 Bucket

* Web Hosting Platform:
  * Heroku

* Paypal Integration:
  * Paypal Sandbox with Business Account

# 2. Project Intro
"Stolen Goods" is a fun parody project simulating an international e-commerce that sells items from criminals to collectors around the world. Even though this is only a parody, this web application has a fully functioning features like any other e-commerce platform.

# 3. Database
Django uses Object Relational Mapper that can be connected to any database. This project uses SQLite3 during the development stage for its simple fungtionality purpose and PostgreSQL for its scalability in production. PostgreSQL is used both in localhost with DataGrip and online with AWS RDS. This project has 11 relational database tables excluding the default django classes (i.e. auth_permission, auth_group, etc.).

# 4. Project Objective
* The main objective of this project is to implement the knowledge in web development and software engineering gained in spring semester 2021 by programming a fully-functional software that runs a web application.

* My private goal is to prove the superiority of Python over other programming languages by creating a web application only with a Python Web Framework: Django.

# 3 Project Setup
* Clone / Download the repository

* Make sure you have python 8.x or higher, othwerwise [Upgrade Your Python](https://www.python.org/downloads/) or run "brew upgrade python" on your terminal

* Create a virtual env "python -m venv <YOUR_VENV_NAME>" or "mkvirtualenv <YOUR_VENV_NAME>"

* Activate virtualenv "Source <YOUR_VENV_NAME>/bin/activate" or "workon <YOUR_VENV_NAME>"

* Install all the modules "pip install -r requirements.txt"

* All the credentils from in configurations/settings.py are saved in .env file. Please assign your own credentials to all variables provided in this repo file: ".env-secrets"  

* Create the database:
  * "python manage.py makemigrations"
  * "python manage.py migrate"

* Create an admin "python manage.py createsuperuser"

* Set up the local server: "python manage.py runserver"

* To login as an admin go to 'http://127.0.0.1:8000/stolen-goods-admin/'

# 4. Relational Database
Everytime we add or change the database, the django application will not be automatically connected. This is why we always need to re-run:
* "python manage.py makemigrations"

* "python manage.py migrate"

* "python manage.py createsuperuser"

# 4a. Setup
For the database setup, I assumed that you atleast have Postgres.app, if not [Download here](https://postgresapp.com/downloads.html)

* Activate your postgres service on postgres app or run "pg_start"

* Open DataGrip or your prefered IDE for database
* ## SQLite3 Setup:
  * Upload the .sqlite3 file "New => Data Source => SQLite3 => File"

  * Click "Test connection" and then "ok"

![alt sqlite3 setup](docs/database/SQLite-Setup.png)
![alt sqlite3 tables](docs/database/SQLite3Tables.png)

* ## PostgreSQL (Localhost):
  * Connecting PostgreSQL 13.2 "New => Data Source => PostgreSql"

  * Fill in the credentials

  * Click "Test connection" and then "ok"

![alt postgresql local setup](docs/database/PostgreSQL-LocalSetup.png)

* ## PostgreSQL (AWS RDS):
  * Signin to your [AWS](https://signin.aws.amazon.com/signin?redirect_uri=https%3A%2F%2Fconsole.aws.amazon.com%2Fconsole%2Fhome%3Ffromtb%3Dtrue%26hashArgs%3D%2523%26isauthcode%3Dtrue%26nc2%3Dh_ct%26src%3Dheader-signin%26state%3DhashArgsFromTB_us-east-1_89ab805abe155024&client_id=arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&forceMobileApp=0&code_challenge=3yzEx5_jmEbzHM1BYCd2CjiMWXVN0KDTdhVDC3KaBfU&code_challenge_method=SHA-256) or [Signup](https://portal.aws.amazon.com/billing/signup?refid=em_127222&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start)

  * Create Database, choose PostgreSQL

  * Copy your "Endpoint" under "Connectivity & Security"

  * Open DataGrip and "New => Data Source => PostgreSql"

  * Paste your endpoint in the "Host" input

  * Type in your AWS RDS username in the "USER"

  * Type in the password for that username

  * Click "Test connection" and then "ok"

![alt postgresql aws rds setup](docs/database/PostgreSQL-RDS-Setup.png)
![alt postgresql tables and schema](docs/database/PostgreSQL-Tables.png)

# 4b. Entity-Relationship Model
## Relationships:
* One-to-One:
  * (One) User => (One) UserProfile

* One-to-Many:
  * (One) Category => (Many) Product
  
  * (One) Product => (Many) ProductGallery
  
  * (One) Product => (Many) ReviewRating

  * (One) Product => (Many) CartItem

  * (One) Cart => (Many) CartItem

  * (One) CustomUser => (Many) CartItem

  * (One) CustomUser => (Many) ReviewRating

  * (One) CustomUser => (Many) Payment

  * (One) CustomUser => (Many) Order

  * (One) Payment => (Many) Order

  * (One) Order => (Many) OrderProduct

  * (One) Product => (Many) OrderProduct

  * (One) Payment => (Many) OrderProduct

  * (One) CustomUser => (Many) OrderProduct

## PostgreSQL 13.2:
* 11 Relational Database Tables

* 7 Django-Default Relational Database Tables

* 1 Honeypot Admin Package Relational Database Table

![alt postgres ERM](docs/database/ERM-SG-PostgreSQL13-2-AWS-RDS.png)

## SQLite3:
* 11 Relational Database Tables

* 7 Django-Default Relational Database Tables

* 2 SQLite-Default Relational Database Tables

* 1 Honeypot Admin Package Relational Database Table

![alt sqlite3 ERM](docs/database/ERM-SG-SQLite3.png)

# 4c. Database Queries used in this Project
## INSERT TABLE table_name();
* Create a python class in your_app_name/models.py

* On the terminal run:
  * python manage.py makemigrations
  * python manage.py migrate

## INSERT INTO table_name(parameter); VALUES(argument);
* user = CustomUser.objects.create_user(email="admin@stolengoods.wtf", username="admin", pasword="admin")

## INSERT INTO user_profiles(id, first_name, last_name, user_id); VALUES(1, "nino", "lindenberg", 1);
* current_user = request.user

* profile = UserProfile()

* profile.user_id = user.id

* profile.save()

## SELECT * FROM table_name;
* products = Product.objects.all()

## SELECT * FROM table_a INNER JOIN ON table_a.table_b_id = table_b.id;
* current_user = request.user

* cart_items_from_current_user = CartItem.objects.filter(user=current_user)

## SELECT * FROM table_name WHERE boolean_column='True' ORDER BY id;
* products = Product.objects.all().filter(is_available=True).order_by('id')

## SELECT username FROM custom_users WHERE username = auth_user.username;
## UPDATE custom_user SET password = "new password";
* user = User.objects.get(username__exact=request.user.username)

* user.set_password("new_password")

* user.save()

# 5. CI / CD
The CI/CD implemented in this project is using the GitHub Actions which is written in YAML syntax in a .yaml or .yml file and saved in .github/workflows directory.

## Continuous Integration (CI):
CI is the practice of automating the integration of code changes from multiple contributors or contributions into a single software project.

* The main jobs in this CI:
  * 3 jobs in which each will be running on 3 different python versions (3.7, 3.8, 3.9)
  
  * Using docker vm container from GitHub to check the health of PostgreSQL used in this project
  
  * Linting with Flake8 to make sure that the code is written based on a good clean code convention
  
  * Testing with "Pytest-Cov" to make sure that the program will not break in production

## Continuous Deployment (CD):
CD is a strategy for software releases wherein any code commit that passes the automated testing phase is automatically released into the production environment, making changes that are visible to the software's users. 

* The job for the CD in this project is created to make sure that only codes which have passed the Pytest-Cov will be pushed to Heroku to be deployed into the production stage
# 6. Paypal Sandbox
For demo purpose, this project uses "Paypal Sandbox Integration" with Javascript. To process the purchase. please use this credentials:

* Paypal Sandbox Account: maxi.musterfrau@gmail.com

* Paypal Sandbox Password: yxcasdqwe123!

## Thank you for your time and interest!