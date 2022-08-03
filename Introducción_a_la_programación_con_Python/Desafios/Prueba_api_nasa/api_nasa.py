import requests
import json
from string import Template


def build_web_page(url_list):
    """
    It takes a list of urls and creates an html file with the images from those urls
    
    :param url_list: a list of urls to images
    """
    
    # Creating a template for the html code that will be used to display the images.
    img_template = Template('<li><img src="$url"></li>')
    # Creating a template for the html page.
    html_template = Template("""<html>
                                <head>
                                <title>Fotos de Curiosity</title>
                                </head>
                                <body>
                                <h1>Fotos de Curiosity</h1>
                                <ul>
                                $images
                                </ul>
                                </body>
                                </head>
                                </htm
                            """)
    
    texto_img = ''
    for i in url_list:
        texto_img += img_template.substitute(url = i) +'\n'

    html = html_template.substitute(images = texto_img)
    
    with open('output.html', 'w') as f:
        f.write(html)

def request(url):
    """
    It takes a url and returns the json response from the API
    
    :param url: the url of the API endpoint
    :return: A JSON object
    """
    payload = ""
    headers = headers = {"api_key" : "m3nkogOQEl1k9SR2gnHmlFF0LZjsgjJGfuWQCWgJ"}

    response = requests.request("GET",url, data = payload, headers = headers)
    return json.loads(response.text)

# Making a request to the NASA API and storing the results in a variable called results.
url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos?page=1&api_key=m3nkogOQEl1k9SR2gnHmlFF0LZjsgjJGfuWQCWgJ"
results = request(url)


# Creating an empty list.
url_list=[] 

# The above code is creating a list of the 25 most recent photos taken by the Mars Rover.
for i in range(25):
    x= results["latest_photos"][i]["img_src"]
    url_list.append(x)



request(url)
build_web_page(url_list)
