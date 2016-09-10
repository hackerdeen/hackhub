
import sys
import os

sys.path.insert(0, '/srv/vhosts/www/hackhub')
os.environ["MPLCONFIGDIR"] = "/tmp/"
os.environ["GNUPGHOME"] = "/home/www-data/.gnupg"
from hackhub import app as application

