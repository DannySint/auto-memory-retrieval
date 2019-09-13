import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

databases = myclient.list_database_names()
database = myclient["database"]
collections = database.list_collection_names()


def insert_single(subreddit, redditLink, url, title, transcription):
    transcriptions = database[subreddit]
    if not alreadyExists:
        dict = {"_id": redditLink, "imageUrl": url, "title": title, "transcription": transcription}
        transcriptions.insert_one(dict)

def insert_multi(subreddit, dicts):
    multiDict = []
    transcriptions = database[subreddit]
    for i in range(len(dicts)):
        multiDict.append(dicts[i])
    transcriptions.insert_many(multiDict)

def alreadyExists(subreddit, redditLink):
    transcriptions = database[subreddit]
    for i in range(len(transcriptions)):
        if redditLink in transcriptions[i]._id:
            return True
    return False

def search(subreddit, transcription):
    transcriptions = database[subreddit]
    hits = []
    for i in range(len(transcriptions)):
        if transcription in transcriptions.transcription:
            hits.append(transcriptions[i].transcription)
    return hits