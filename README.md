
# Back End of Jiskefet

  

This part contain the **backend** of Jiskefet project.

## Summary

- **Server installation**

	1. Install Python

	2. Install Django

	3. Launch Django

	4. Install httpd

	5. Install PostgreSQL

- **Setup your environment**
- **Use Swagger**

  

# Server installation


> There is the **installation process from scratch** of the RedHad
> server we use.

First, you need to update repo : 

    sudo yum install epel-release centos-release-scl
    sudo yum update

## Install Python

We will need **python3** to use Django, run those command to install it
  
    sudo yum install python36-devel python36 python36-pip rh-python36--mod_wsgi
    sudo python3 -m pip install --upgrade pip
    sudo python3 -m pip install virtualenv

  

## Create Django application

> Django is a python framework used to create and manage REST API, more
> information [here](https://www.djangoproject.com/start/overview/)

Run those command to install it :

**If your use the project on this git repo**

    cd ~/
    git clone git@github.com:SoftwareForScience/summerschool2019-jiskefet-backend.git \ jiskefet-backend
    cd jiskefet-backend
    sudo python3 -m pip install django
    python3 -m venv djangoenv
    source djangoenv/bin/activate
    python3 -m pip install -r requirements.txt
    source djangoenv/bin/deactivate
    sudo cp ~/jiskefet-backend /var/www
    sudo chown -R <username>:apache /var/www/jiskefet-backend
    cd /var/www/jiskefet-backend 
    source djangoenv/bin/activate
    python3 manage.py migrate
    python3 manage.py collectstatic

Next you need to create **jiskefet/settings.py**
as it's a sensible file, it is not in git but you need to update it using the file called **settings.py.template** in the jiskefet folder

**If your start a project from scratch :** 
  

    cd ~/
    python3 -m venv djangoenv
    source ~/djangoenv/bin/activate
    sudo python3 -m pip install django
    sudo python3 -m pip install djangorestframework
    sudo python3 -m pip install django-rest-swagger
    sudo python3 -m pip install psycopg2
    django-admin startproject jiskefet-backend
    source djangoenv/bin/deactivate
    mv djangoenv jiskefet-backend
    sudo cp ~/jiskefet-backend /var/www
    sudo chown -R <username>:apache /var/www/jiskefet-backend
    cd /var/www/jiskefet-backend 
    source djangoenv/bin/activate
    python3 manage.py migrate
    python3 manage.py collectstatic
    python3 manage.py createsuperuser

    
## Launch Django

  

To run Django, you need to run this command :

  

    python3 manage.py runserver 0.0.0.0:8000

  

**Django use the port 8000**, if it's not open on your server, you'll need to do this :

  

    sudo firewall-cmd --zone=public --permanent --add-port=8000/tcp
    sudo firewall-cmd --reload

  

Now you're able to **acces to your Django interface** at [http://(host):8000](http://host:8000).

  ![Django interface](https://www.javatpoint.com/django/images/django-admin-interface.png)

## Install httpd

> httpd is used to install needed components for a **apache2
> webserver**,  certbot is used for https

    sudo yum install httpd httpd-devel
    sudo yum install certbot python2-certbot-apache
    sudo certbot certonly --apache
    echo "0 0,12 * * * root python -c 'import random; import time; time.sleep(random.random() * 3600)' && certbot renew" | sudo tee -a /etc/crontab > /dev/null
    sudo service httpd start

**httpd use the port 80 and 443**, if it's not open on your server, you'll need to do this :
  

    sudo firewall-cmd --zone=public --add-port=80/tcp --permanent
    sudo firewall-cmd --zone=public --add-port=443/tcp --permanent
    sudo firewall-cmd --reload

You can now acces to your web server at [http://host](http://host)

![Apache2 default page](https://connectwww.com/wp-content/uploads/2011/02/Apache2-Ubuntu-Default-Page-It-works-.jpg)

## Install PostgreSQL

> We use a **PostgreSQL database** to store and manage easily file's
> data and metadata because we can't predict data model

Run thoses commands tho install PostgreSQL on your server

    sudo yum install postgresql-server postgresql-contrib postgresql-devel
    sudo postgresql-setup initdb
    sudo systemctl start postgresql
    sudo systemctl enable postgresql

After PostgreSQL installation, connect you as postgres user :

    sudo su postgres
    [postgres] $ psql
    psql> CREATE USER jiskefet WITH LOGIN;
    psql> CREATE DATABASE jiskefet WITH OWNER jiskefet ENCODING 'UTF8';
    psql> \q
    [postgres] $ exit
Then, edit */var/lib/psgql/data/pg_hba.conf* in the line **IPv4** : change *peer* to *trust*

# Setup your environment

**For setup your local environment, You will need :**

 1. [Git client](https://git-scm.com/downloads)
 2. Create a local apache2 web server [XAMPP](https://www.apachefriends.org/fr/download.html) 
 3. Install [PostgreSQL](https://www.postgresql.org/download/)
 4. Install [python3](https://www.python.org/downloads/) and [Django](https://www.djangoproject.com/download/)

Then, create a new folder, open your **git client** and clone the project :

    git clone git@github.com:SoftwareForScience/summerschool2019-jiskefet-backend.git
 
After that, open a prompt and run this python command :

    pip install -r requirements.txt

If it's well done, you'll be able to launch your server and **acces to your Django interface** at [http://localhost:8000](http://localhost:8000).

As your local environment is used to develop, you may need to switch to develop branch :

    git checkout develop 

# Use Swagger

If you've correctely install and create the project, you are able to acces to your Django interface. Also, you have install [Swagger](https://swagger.io/).

> Swagger is an open-source software framework that helps to
> design and build REST API

This is a [exemple](https://petstore.swagger.io/) of what Swagger is able to do.

To configure swagger you need to do this :

> We use User API as a exemple

In *settings.py*


    INSTALLED_APPS = [ 
    	#[django core apps] 
    	... 
    	'rest_framework', 
    	'rest_framework_swagger', 
    ] 

    ... 
    
    REST_FRAMEWORK = {
	    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny',),
	    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework.authentication.SessionAuthentication',),
	}

In *urls.py*

    from django.conf.urls import url, include 
    from django.contrib.auth.models import User
    from rest_framework import routers, serializers, viewsets 
    class 
    from rest_framework.schemas import get_schema_view
    from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

    UserSerializer(serializers.HyperlinkedModelSerializer):  
	    class Meta: 
		    model = User 
			fields = ('url', 'username', 'email', 'is_staff') 
			
	class UserViewSet(viewsets.ModelViewSet):
		queryset = User.objects.all()
		serializer_class = UserSerializer 
	
	router = routers.DefaultRouter()
	router.register(r'users', UserViewSet)
	
	schema_view = get_schema_view(title='Users API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])
	 
	urlpatterns = [
		url('swagger/', schema_view, name="docs"),, 
		url('users/', include(router.urls)), 
	]
Now if you acces to [http://localhost:8000/swagger](http://localhost:8000/swagger) to will be able to display the swagger interface with the User API exemple

![Swagger default Users API](https://hirelofty-prod.s3.amazonaws.com/media/images/users_api.width-1920.png)