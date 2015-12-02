import os
from stat import *

os.chmod('aaa.txt', S_IWUSR | S_IRUSR | S_IRGRP | S_IWOTH | S_IROTH)
