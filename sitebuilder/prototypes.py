import sys,os
from django.conf import settings

SECRET_KEY = os.environ.get('SECRET_KEY', '$fpso%q8rr&a1*_9a3cs=%_!+-*8+hohdjc7o8q6qjvtt=)6$2')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')
BASE_DIR = os.path.dirname(__file__)

settings.configure(
	DEBUG=True,
	SECRET_KEY=SECRET_KEY,
	ALLOWED_HOSTS=ALLOWED_HOSTS,
	ROOT_URLCONF='sitebuilder.urls',
	# MIDDLEWARE_CLASSES=(
	# 	'django.middleware.common.CommonMiddleware',
	# 	'django.middleware.csrf.CsrfViewMiddleware',
	# 	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	# 	),
	INSTALLED_APPS = (
		'django.contrib.staticfiles',
		'django.contrib.webdesign',
		'sitebuilder',
		'compressor',
		),
	STATIC_URL='/static/',
	SITE_PAGES_DIRECTORY=os.path.join(BASE_DIR, 'pages'),
	SITE_OUTPUT_DIRECTORY=os.path.join(BASE_DIR, '_build'),
	STATIC_ROOT=os.path.join(BASE_DIR, '_build', 'static'),
	# STATICFILES_STORAGE='django.contrib.staticfiles.storage.CachedStaticFilesStorage',
	STATICFILES_FINDERS=(
            'django.contrib.staticfiles.finders.FileSystemFinder',
            'django.contrib.staticfiles.finders.AppDirectoriesFinder',
            'compressor.finders.CompressorFinder',),
	)

if __name__ == "__main__":
	from django.core.management import execute_from_command_line
	execute_from_command_line(sys.argv)