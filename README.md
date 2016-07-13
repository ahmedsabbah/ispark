# iSpark

# Where are the html files?
## Inside folders (authentication, contents, services) there is a folder called templates. Html files are divided among them. There is a file base.html in authentication/templates which is embedded in every html file when run.

# How to run?
## Open the terminal (command line) and navigate to the project folder containing the following folders (authentication, contents, services). Create a virtual environment using library 'virtualenv' (python). Activate the environment then install the requirements in requirements.txt using library 'pip' (python). When done run the following commands in order:

## python manage.py makemigrations
## python manage.py migrate
## python manage.py collectstatic
## python manage.py runserver

# How templates work?
## Open any of the templates, try to copy the way css, js and images are included.
## You will notice that every template fills parts of the base.html file.
## There are basic css/js files included in every html view, they are put in the base.html file, every other file is included in the html file of the view.

# If you can not understand any of the previous, It's okay.
## My only request is changing the way files(css, js, images) are included to match the way they are included in the templates here.
