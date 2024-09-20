from bs4 import BeautifulSoup
import requests

try:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
    url = 'https://www.imdb.com/chart/top/'
    response = requests.get(url, headers=headers)
    response.raise_for_status() 
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.prettify())  
    movies = soup.find('ul',class_="dHaCOW").find_all('li')
    # print(len(movies)) #25
    
    for movie in movies:
        name = movie.find('div',class_="ipc-title").a.text.split('.')[0]
        spans = movie.find_all('span', class_="sc-b189961a-8 hCbzGp cli-title-metadata-item")
        if spans:
            year = spans[0].text  
            duration = spans[1].text 
            rating = spans[2].text
        print(f"Name:{name} Year: {year}, Duration: {duration}, Rating: {rating}")
    else:
        print("Failed to retrieve movie details")
        
    
    
except Exception as e:
    print(e)
    
