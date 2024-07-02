# Django-Tutorial
In this Django Tutorial, I have done the important topic's of the Django which an Django Developer should know and which are important.

# Installation process
1) Download Python - https://www.python.org/downloads/
2) Download Virtual Environment - https://pypi.org/project/virtualenv/
3) Download Django package on the command Prompt - pip install django
4) Create a Virtual Environment - virtualenv env
5) Actiavte a Virtual Environment - cd env\Scripts\activate
6) Creating a new django app - python manage.py startapp app-name
7) Run the app - python manage.py runserver
8) If you want to run the app on different server - python manage.py runserver 0.0.0.0:5000


# Topic : Views and urls :
In a Django project, there can be multiple apps, such as payment, about, and home. Each app is created to handle specific features or functionality. Within each app, we define views to process requests and render responses. The URL routing for each app is managed in its own urls.py file, where we map URL patterns to their corresponding views. Finally, we include these app-specific URL patterns in the main project's urls.py file to bind them to the overall application.

# Topic : Template engine and Template Inheritance:
Django has powerfull tool i.e template engine. Template Engine means we can use looping, conditional statement etc as like we do in python. it has its own syntax. For more information go through : 
 https://docs.djangoproject.com/en/5.0/ref/templates/language/#

Template inheritance in Django allows you to create a base template with common elements like header and footer, and then define placeholders for content that will change. Other templates can inherit from this base and override the placeholders with specific content, reducing code duplication and making maintenance easier.

# Important Topic : Models and Migration :
In the models file we write the class which has the attributes of the class we have created for eg. If we create a class as Student and its attributes are name, age, email, address etc and when we make the changes in it we need to write the command as "python manage.py makemigrations" and again we need to write the command "python manage.py migrate" this make the changes. 
And now the question is that how does the Django knows we have made the changes in which class, the django has the its own database like structure which checks the previous structure with the current structure.

More informations about models and migrations

When you define a model in Django by creating a class that inherits from django.db.models.Model, you are essentially defining the structure of the data you want to store in the database. Each model class represents a database table, and each attribute of the class represents a field in that table.

When you make changes to a model, such as adding, removing, or modifying fields, you need to inform Django of these changes so that it can update the database schema accordingly. This is where migrations come into play.

The python manage.py makemigrations command is used to create migration files. These files are Python scripts that describe the changes you've made to your models. Django uses these migration files to determine what changes need to be applied to the database.

The python manage.py migrate command is then used to apply those migrations to the database. This command reads the migration files and executes the necessary SQL commands to alter the database schema.

Django keeps track of the applied migrations in a special table named django_migrations. This table records the migration files that have been applied to the database. When you run makemigrations, Django compares your current models with the ones stored in the last migration to determine what has changed. When you run migrate, Django compares the migrations files that have not been applied to the database with the records in the django_migrations table to determine which migrations need to be executed.

In summary, Django knows what changes have been made to your models by comparing the current state of your models with the historical information stored in migration files and the django_migrations table. This system allows Django to maintain the integrity of your database schema as you develop your application.

Commands :
For making migrations : python manage.py makemigrations
For migrating = python manage.py migrate
