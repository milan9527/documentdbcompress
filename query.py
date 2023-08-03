import threading
import pymongo

def perform_query(query):
    client = pymongo.MongoClient('mongodb://milan:password@ping5.cluster-c7b8fns5un9o.us-east-1.docdb.amazonaws.com:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client['compresstest']
    collection = db['microrepeat']
    results = collection.find(query)
    for result in results:
        print(result)
    client.close()


n = 0
while True:
    num_threads = 50
    threads = []
    for i in range(num_threads):
        query = {"name": "name"+str(n)}
        t = threading.Thread(target=perform_query, args=(query,))
        threads.append(t)
        t.start()
        n += 1
    for t in threads:
        t.join()
