# soloassisment

    pyenv local 3.7.0 # this sets the local version of python to 3.7.0
    python3 -m venv .venv # this creates the virtual environment for you
    source .venv/bin/activate # this activates the virtual environment
    pip install --upgrade pip [ this is optional]  # this installs pip, and upgrades it if required.
   
    python3 manage.py migrate
    
    python manage.py migrate
    
# Start the Server
We so this using the manage.py command tool by entering this command in the terminal:

    python manage.py runserver
If you're doing this on another platform, then you might need to use this instead (change the port number from 8000 as required):

    python3 manage.py runserver 0.0.0.0:8000 
