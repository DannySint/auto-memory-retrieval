import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

databases = myclient.list_database_names()
#print("databases:",databases)
database = myclient["database"]
#print("database",database)
collections = database.list_collection_names()
#print("collections:",collections)
debug = False


def insert_single(subreddit, redditLink, url, title, transcription):
    transcriptions = database[subreddit]
    if debug: print("alreadyExists:",bool(alreadyExists(subreddit, redditLink)))
    if not bool(alreadyExists(subreddit, redditLink)):
        if debug: print("Inserting...")
        dict = {"_id": redditLink, "imageUrl": url, "title": title, "transcription": transcription}
        transcriptions.insert_one(dict)

def insert_multi(subreddit, dicts):
    multiDict = []
    transcriptions = database[subreddit]
    for i in range(dicts.Sized):
        multiDict.append(dicts[i])
    transcriptions.insert_many(multiDict)

def alreadyExists(subreddit, redditLink):
    transcriptions = database[subreddit]
    if debug: print("'Already Exists' function activation. Searching: ",transcriptions.name, "for ",redditLink)
    #for i in range(transcriptions.count()):
    result = transcriptions.find_one({ "_id": redditLink})
    if (not (result == None)):
        return True
    return False

def search(subreddit, transcription):
    transcriptions = database[subreddit]
    hits = []
    for i in range(len(transcriptions)):
        if transcription in transcriptions.transcription:
            hits.append(transcriptions[i].transcription)
    return hits