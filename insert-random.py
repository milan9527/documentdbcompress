import pymongo
import random
import string
import datetime


def generate_random_string(size):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(size))
    return random_string


random_string = generate_random_string(4 * 1024)
idn = 0
client = pymongo.MongoClient('mongodb://milan:wAr16dk7@ping5.cluster-c7b8fns5un9o.us-east-1.docdb.amazonaws.com:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
db = client.test
col = db.micro
for num in range(0, 100000):
    data = []
    for i in range(0, 100):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data.append({'_id': idn, 'txt': random_string, 'dt': now})
        idn += 1
    col.insert_many(data)
client.close()
