#Download image from given url
import random
import urllib.request

def download_web_image(url):
    num = random.randrange(1,1000)
    full_name = str(num) + ".jpg"
    urllib.request.urlretrieve(url,full_name)

download_web_image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Felis_silvestris_silvestris_small_gradual_decrease_of_quality.png/240px-Felis_silvestris_silvestris_small_gradual_decrease_of_quality.png")
download_web_image("http://i.dailymail.co.uk/i/pix/tm/2007/07/lionking1807_468x325._to_468x312jpeg")
