# Mindbowser Manager Employee Management Application - BACKEND

# Python, Django, Mysql
The Manager and Employee assignment with JWT implementation,swagger and pagination for list details.

Backend
# How To Run

## Requirements for backend
- Python
- IDE(pycharm or any other)
- pip(if not installed along with python)
- MySQL & MySql workbench
- Git

## Installation
First Install the base programs to run the application
- [Python](https://www.python.org/downloads/)
- [PyCharm](https://www.jetbrains.com/pycharm/download/)
- [MySQL](https://www.mysql.com/downloads/)
- [GIT](https://git-scm.com/downloads)

After all this is Installed
#
Create an empty folder
**Step 1:**

Right click -> gitbash
A terminal window will open, In that window run the following command
```
git clone https://github.com/pr4shantS0naw4n3/mindbowser_managerEmployeeApp_Back.git
```
This will clone the repository on your local environment
#
**STEP 2:**

Inside the cloned folder open command prompt(cmd) and run
```
pip install -r requirements.txt
```
This will install all the dependencies of the project on your local machine
#
**STEP 3:**

**Next Thing is Setting up Database**
If your Mysql and Mysql Workbench is Installed
1. Open MySql workbench and setup the host,port,username and password
2. Open a Connection to it and Create a new Schema(this will be your db name for django database settings)
#
**STEP 4:**

Open IDE and load your project inside it
Now goto ```settings.py``` and search for ```DATABASES```
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "your schema name",
        'USER': 'your Username',
        'PASSWORD': 'your password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
After all this configuration is done
#
**STEP 5:**

goto the terminal(project terminal) and run the following command

```
python manage.py migrate
```
this command will apply initial migrations and models so that all your models is reflected in the database
#
**STEP 6:**

Final command
```
python manage.py runserver
```
With this command your backend server will be up and running


**AFTER SETTING UP THE BACKEND NEXT WE WILL SETUP THE FRONT END**

**CLICK ON THE BELOW LINK TO GOTO THE FRONTEND SETUP README**

[FRONTEND SETUP](https://github.com/pr4shantS0naw4n3/mindbowser_managerEmployeeApp_Front)
