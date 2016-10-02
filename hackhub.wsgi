activate_this = '/home/hackhub/.hackhub/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
import os

sys.path.insert(0, '/home/hackhub/hackhub')
os.environ["MPLCONFIGDIR"] = "/tmp/"
os.environ["GNUPGHOME"] = "/home/hackhub/.gnupg"
from hackhub import app as application
