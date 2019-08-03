import retriever
import transcriber


#return true if search terms are found in image
#

def search(input, subreddit):
    submissions = retriever.get_image_submissions('memes', 10)
    for submission in submissions:
        transcription = transcriber.transcribe_image_from_url(submission.url)
        if (input in transcription):
            print(submission.title, submission.url)


search('Plankton', 'memes')