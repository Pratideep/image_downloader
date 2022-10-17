
# importing Flask and other modules
import os
import requests
from bs4 import BeautifulSoup
from flask import Flask, request, render_template

# Flask constructor
app = Flask(__name__)
google_image = "https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&"

user_agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}

@app.route('/', methods=["GET", "POST"])
def gfg():
    global img_name
    global img_num
    if request.method == "POST":
       # getting input with name = fname in HTML form
       image_name = request.form.get("iname")
       # getting input with name = lname in HTML form
       number = request.form.get("num")
       img_name = image_name
       img_num = int(number)
       main()
       return render_template("sucess.html")
      #  return "This is ->"+image_name +" "+ number

   #  print(img_name,img_num)
    return render_template("index.html")

# Third Section: Build the main function
saved_folder = 'images'
def main():
    if not os.path.exists(saved_folder):
        os.mkdir(saved_folder)
    download_images()


def download_images():
    data = img_name
    n_images = img_num

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



 
if __name__=='__main__':
   app.run()