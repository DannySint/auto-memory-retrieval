import retriever
import transcriber
import file

subreddit = 'memes'
posts = 4

images = retriever.get_image_submissions(subreddit, posts)

for image in images:
    #x = transcriber.transcribe_image_from_path('data/cucumber.png')
    x = transcriber.transcribe_image_from_url(image.url)
    redditLink = "https://reddit.com/r/memes/comments/" + str(image)
    #print(redditLink, image.url, image.title, x)
    file.insert_single(subreddit, redditLink, image.url, image.title, x)