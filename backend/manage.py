import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'my_imdb'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_imdb.settings')

from django.core.management import execute_from_command_line

if __name__ == '__main__':
    execute_from_command_line(sys.argv)
