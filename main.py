import retriever
import transcriber

images = retriever.get_image_submissions('memes', 3)

for image in images:
    print(image.title, image.url)
    #x = transcriber.transcribe_image_from_path('data/cucumber.png')
    x = transcriber.transcribe_image_from_url(image.url)
    print(x)