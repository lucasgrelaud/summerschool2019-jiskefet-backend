# Back End of Jiskefet

This part contain the backend of Jiskefet project.

**Server installation**
 1. Install Python
 2. Install Django
 3. Launch Django
 4. Install httpd
 5. Install PostgreSQL


# Server installation

There is the installation process of the RedHad server we use.

## Install Python
Install python and component in that

    sudo yum install epel-release
    sudo yum update
    sudo yum install python-devel
    python-setuptools python3 python36-pip
    sudo python3 -m pip install --upgrade pip
    sudo python3 -m pip install virtualenv

## Install Django

    virtualenv djangoenv
    source ~/djangoenv/bin/activate
    python3 -m pip install django sudo python3 -m pipinstall djangorestframework 
    sudo python3 -m pipinstall django-rest-swagger 
    django-admin startproject jiskefet
    python3 manage.py migrate
    python3 manage.py createsuperuser

## Launch Django

To run Django server, you need to run this command :

    python3 manage.py runserver 0.0.0.0:8000

Django use the port 8000, if it's not open on your server, you'll need to do this :

    sudo firewall-cmd --zone=public --permanent --add-port=8000/tcp
    sudo firewall-cmd --reload

Now you're able to acces to your Django interface at [http://(host):8000](http://host:8000).

## Install httpd

    sudo yum install httpd
    sudo service httpd start
  
  httpd use the port 80, if it's not open on your server, you'll need to do this :

    sudo firewall-cmd --zone=public --add-port=80/tcp --permanent
    sudo firewall-cmd --reload

## Install PostgreSQL

    sudo yum install postgresql-server postgresql-contrib
    sudo postgresql-setup initdb
    sudo systemctl start postgresql
    sudo systemctl enable postgresql

