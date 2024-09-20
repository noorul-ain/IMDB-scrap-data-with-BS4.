
from bs4 import BeautifulSoup
import requests

try:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
    url = 'https://www.imdb.com/chart/top/'
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # This will raise an HTTPError for bad responses (4xx and 5xx)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the list of movies
    movies = soup.find('tbody', class_='lister-list').find_All('tr')

    for movie in movies:
        # Extract movie title
        title_column = movie.find('td', class_='titleColumn')
        name = title_column.a.text
        rank = title_column.get_text(strip=True).split('.')[0]
        
        # Extract year, duration, and rating
        spans = movie.find('span', class_='secondaryInfo')
        year = spans.text.strip('()')
        
        duration_span = movie.find('span', class_='runtime')
        duration = duration_span.text if duration_span else 'N/A'
        
        rating_span = movie.find('strong')
        rating = rating_span.text if rating_span else 'N/A'

        print(f"Rank: {rank} Name: {name} Year: {year} Duration: {duration} Rating: {rating}")

except Exception as e:
    print(e)
