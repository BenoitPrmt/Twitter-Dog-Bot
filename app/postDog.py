def postDog(apiKey:str):
    '''Fonction qui poste la photo de chien'''

    apiKey.update_status_with_media(filename='assets/doggy.jpg', status='🐕 Dog of the day :')
    print('Dog picture posted !')