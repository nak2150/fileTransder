from pandas import DataFrame
import numpy as np
import time
import math
import sqlite3
import datetime




conn = sqlite3.connect('cv4DatabaseSarMdac.db')
c = conn.cursor()
c.execute("ALTER TABLE cv4 RENAME COLUMN runNumber TO calibVersion")
conn.commit()
conn.close()
