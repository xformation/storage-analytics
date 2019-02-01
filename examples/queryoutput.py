from __future__ import print_function
import xml.etree.cElementTree as ET
import pandas as pd
from collections import OrderedDict
import re
from sqlalchemy.types import VARCHAR
from sqlalchemy import create_engine
import sqlite3

connection = sqlite3.connect('mysql')
crsr = connection.cursor()

crsr.execute("select distinct stor_grpname from vmax_sg;")
