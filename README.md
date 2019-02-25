# Missouri-Data

Install Requirements.txt

# Settings.py
Need to set the environmnet variable in your bash or zsh.
You can generate your secret key from here:
https://www.miniwebtool.com/django-secret-key-generator/

Set debug = False in settings.py for production

#db.sqlite3
Run command python manage.py for db.sqlite3

# Command for make migrations
python manage.py makemigrations,
python manage.py migrate

# Save csv file data to Django Database
python savecsvdata.py 



# Run the project
python manage.py runserver

# Run Unit Test for APIs
python manage.py test


