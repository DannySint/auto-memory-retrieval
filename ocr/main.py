import retriever
import transcriber
#import file

subreddit = 'memes'
posts = 5

images = retriever.get_image_submissions(subreddit, posts)

for image in images:
    #x = transcriber.transcribe_image_from_path('data/cucumber.png')
    x = transcriber.transcribe_image_from_url(image.url)
    append = "https://reddit.com/r/memes/comments/" + str(image)
    print(append, image.title, image.url, x)