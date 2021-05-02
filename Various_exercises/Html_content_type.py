import requests

def get_content_type(url):
    r = requests.get(url)
    print(r.headers['Content-Type'])

get_content_type('https://index.hu')
