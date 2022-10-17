# First Section: Importing Libraries
import os
import requests
from bs4 import BeautifulSoup

# Second Section: Declare important variables
google_image = "https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&"

user_agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}

# Third Section: Build the main function
saved_folder = 'images'


def main():
    if not os.path.exists(saved_folder):
        os.mkdir(saved_folder)
    download_images()


# Fourth Section: Build the download function
def download_images():
    data = input('What are you looking for? ')
    n_images = int(input('How many images do you want? '))

    print('searching...')

    search_url = google_image + 'q=' + data

    response = requests.get(search_url, headers=user_agent)

    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    results = soup.findAll('img', {'class': 'rg_i Q4LuWd'})
    # print(results)
    count = 1  # For counter for counting N number of images
    links = []   # storing all images links in array
    for result in results:
        try:
            link = result['data-src']
            links.append(link)
            count += 1
            if(count > n_images):
                break

        except KeyError:
            continue

    print(f"Downloading {len(links)} images...")

    for i, link in enumerate(links):
        response = requests.get(link)

        # let data you given is dog then,
        # image_name = images/dog1.jpg
        image_name = saved_folder + '/' + data + str(i+1) + '.jpg'

        with open(image_name, 'wb') as fs:
            fs.write(response.content)
        
    print("Thanks for downloading 😊 ----> Made by pratideep")

# Fifth Section: Run your code
if __name__ == "__main__":
    main()




'''
WB IN OPEN 
The wb indicates that the file is opened for writing in binary mode.

When writing in binary mode, Python makes no changes to data as it is written to the file. In text mode (when the b is excluded as in just w or when you specify text mode with wt), however, Python will encode the text based on the default text encoding. Additionally, Python will convert line endings (/n) to whatever the platform-specific line ending is, which would corrupt a binary file like an exe or png file.

Text mode should therefore be used when writing text files (whether using plain text or a text-based format like CSV), while binary mode must be used when writing non-text files like images.

'''