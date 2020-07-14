import requests

def download(url):
    get_response=requests.get(url)
    #split("/")will split elements according to slashes
    #[-1] will return the splitted url's last part
    file_name=url.split("/")[-1]
    #wb-write binary files
    with open(file_name,"wb")as img:
        img.write(get_response.content)
#select the link with correct extension(jpg,png)
download("https://metro.co.uk/wp-content/uploads/2014/09/minions.png")