from datetime import date, timedelta
from hdfs import InsecureClient, config

# get yesterday
yesterday = day.today()  - timedelta(1)

# connect to hdfs
# client = InsecureClient('http://host:port', user='ann')
# client = Config().get_client('dev')   # use config file

# read csv file from hdfs
# with client.read('samples.csv', encoding='utf-8', delimiter='\n') as reader:
#   for line in reader:
#     pass

# calculate

# save to hdfs
