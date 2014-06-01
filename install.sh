#!/bin/bash

#configuration
DB_ROOT_PASSWORD=admin
DB_NAME=iss_django
DB_LOGIN=admin
DB_PASSWORD=admin
WWW_PATH=/var/www
ALLOWED_HOSTS="[
	'localhost'
]"

# Make sure only root can run our script
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

cat << EOF | debconf-set-selections
mysql-server mysql-server/root_password password $DB_ROOT_PASSWORD
mysql-server mysql-server/root_password_again password $DB_ROOT_PASSWORD
mysql-server mysql-server/root_password seen true
mysql-server mysql-server/root_password_again seen true
phpmyadmin phpmyadmin/dbconfig-install boolean true
phpmyadmin phpmyadmin/app-password-confirm password $DB_ROOT_PASSWORD
phpmyadmin phpmyadmin/mysql/admin-pass password $DB_ROOT_PASSWORD
phpmyadmin phpmyadmin/mysql/app-pass password $DB_ROOT_PASSWORD
phpmyadmin phpmyadmin/reconfigure-webserver multiselect apache2
EOF

apt-get install --yes acl
apt-get install --yes git
apt-get install --yes apache2
apt-get install --yes libapache2-mod-php5
apt-get install --yes mysql-server
apt-get install --yes phpmyadmin
cp /etc/phpmyadmin/apache.conf /etc/apache2/conf.d
apt-get install --yes sqlite3
apt-get install --yes gzip
apt-get install --yes python-dev
apt-get install --yes python-imaging
apt-get install --yes python-pythonmagick
apt-get install --yes python-markdown
apt-get install --yes python-textile 
apt-get install --yes python-docutils
apt-get install --yes python-django
apt-get install --yes python-pip
apt-get install --yes libapache2-mod-wsgi
apt-get install --yes python-mysqldb
pip install --upgrade pip

/usr/share/debconf/fix_db.pl

git clone https://github.com/agnieszkapaszkowska/mega-ankieta

pip install -r mega-ankieta/venv/pip_freeze

cp -r mega-ankieta/django_app/iss $WWW_PATH
mkdir $WWW_PATH/iss/iss/surveys/attachment
chmod 777 $WWW_PATH/iss/iss/surveys/attachment
mkdir $WWW_PATH/static
chmod 777 $WWW_PATH/static

a2dissite default

echo "
<VirtualHost *:80>
    ServerName localhost
    WSGIScriptAlias / $WWW_PATH/iss/iss/iss.wsgi

    Alias /attachment/ $WWW_PATH/iss/iss/surveys/attachment/
    Alias /static/ $WWW_PATH/static/
    Alias /favicon.ico /$WWW_PATH/iss/iss/static/surveys/favicon.ico
</VirtualHost>
" >/etc/apache2/sites-available/iss
a2ensite iss

service apache2 reload

echo "
import os, sys
sys.path.append('$WWW_PATH/iss')
os.environ['DJANGO_SETTINGS_MODULE'] = 'iss.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
" >$WWW_PATH/iss/iss/iss.wsgi


echo "
'''
Django settings for iss project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
'''

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SETTINGS_DIR = os.path.abspath(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'us=tu@1zg%z^&7\$7g+%l=2fn0077\$k5\$ngp*(79xne^h=t!udf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = $ALLOWED_HOSTS


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'iss.surveys',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'iss.urls'

WSGI_APPLICATION = 'iss.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '$DB_NAME',
        'USER': '$DB_LOGIN',
        'PASSWORD': '$DB_PASSWORD',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', _('English')),
    ('pl', _('Polish')),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_CHARSET = 'utf-8'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = '$WWW_PATH/static'

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(SETTINGS_DIR, 'templates'),
)

STATICFILES_DIRS = (
    os.path.join(SETTINGS_DIR, 'static'),
)

LOCALE_PATHS = (
    os.path.join(SETTINGS_DIR, 'locale/'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

" >$WWW_PATH/iss/iss/settings.py


#creating database and user
echo "Enter database root password";
echo "drop database if exists $DB_NAME;
create database $DB_NAME collate utf8_unicode_ci;
grant usage on *.* to $DB_LOGIN@localhost identified by '$DB_PASSWORD';
grant all privileges on $DB_NAME.* to $DB_LOGIN@localhost;
" > tmpdb

mysql -u root -p < tmpdb
rm tmpdb
 
echo no | python $WWW_PATH/iss/manage.py syncdb
echo "from django.contrib.auth.models import User; User.objects.create_superuser('$DB_LOGIN', '', '$DB_PASSWORD')" | $WWW_PATH/iss/manage.py shell
echo yes | python $WWW_PATH/iss/manage.py collectstatic
cp -r $ADMIN_PATH/django/contrib/admin/static/admin $WWW_PATH/iss/iss/static/admin

setfacl -Rm u:www-data:rwX $WWW_PATH

/etc/init.d/apache2 restart

echo "Done";

