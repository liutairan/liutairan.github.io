import django
from django.conf import settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['/Users/liutairan/Documents/GitHub/liutairan.github.io/'],
    }
]
settings.configure(TEMPLATES=TEMPLATES)
django.setup()
from django.template.loader import get_template
from django.template import Context
template = get_template('index.html')
template.render(Context({'name': 'world'}))
