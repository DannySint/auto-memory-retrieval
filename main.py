import retriever

images = retriever.get_image_submissions('memes', 5)

for image in images:
    print(image.title, image.url)