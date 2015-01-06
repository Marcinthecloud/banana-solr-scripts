#Imports
import datetime
import time
import sys
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
import random
############Cassandra Constants######################

cluster = Cluster() #blank for localhost
session = cluster.connect('bananas')

############Variables################################

banana_types = ['Apple', 'Cavendish', 'Lady Finger', 'Pisang Raja', 'Williams', 'Cooking', 'Plantanes']

############Prepared Statement######################

statement=session.prepare(
    """INSERT INTO bananas_by_time(tree_id, time, banana_type, yield)\
    values(?,?,?,?)""")

##################END OF CONSTANTS###########

#To do: add args for parameter
for i in range(1000000):
    timestamp = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#general metrics/CSAT
    session.execute("""INSERT INTO bananas_by_time(tree_id, time, banana_type, yield) values(%s,%s,%s,%s)""",
                    (random.randint(1,1000), timestamp, random.choice(banana_types), random.randint(1,100)))

    time.sleep(1)

cluster.shutdown()
