# soloassisment

    pyenv local 3.7.0 # this sets the local version of python to 3.7.0
    python3 -m venv .venv # this creates the virtual environment for you
    source .venv/bin/activate # this activates the virtual environment
    pip install --upgrade pip [ this is optional]  # this installs pip, and upgrades it if required.
   

We now need to configure the database, which you saw was already detailed in the settings.py file. As django has a built-in admin tool, it already knows some of the tables that it needs to use. We can set this up with the command:

codio:

    python3 manage.py migrate
    
pycharm :

    python manage.py migrate
    
You should see a number of steps being run, each hopefully ending ... OK If not, then look to the errors in the terminal. If you see one that says 'NameError: name 'os' is not defined', then go back and add the import for the 'os' library.  
 
# Start the Server
We so this using the manage.py command tool by entering this command in the terminal:

pycharm:

    python manage.py runserver
    
If you're doing this on another platform, then you might need to use this instead (change the port number from 8000 as required):

codio:

    python3 manage.py runserver 0.0.0.0:8000 
    
 First, we ask Django to generate the migration file with the command:
 
    python manage.py makemigrations shopping
    
This will read the models.py file and generate a migration file based on changes found there.

Second, we run the generated migration with the command:
 
    python manage.py migrate shopping   
