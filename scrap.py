
import csv
from bs4 import BeautifulSoup
import requests

try:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
    url = 'https://www.imdb.com/chart/top/'  
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Check if the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')
    
    #---------------Open a CSV file to write data
    with open('imdb_top_movies.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Year', 'Duration', 'Rating'])  # Write CSV headers
        
        #------------------ Extract movies information
        movies = soup.find('ul', class_="dHaCOW").find_all('li')
        
        for movie in movies:
            name = movie.find('div', class_="ipc-title").a.text.split('.')[0]
            spans = movie.find_all('span', class_="sc-b189961a-8 hCbzGp cli-title-metadata-item")
            
            if spans and len(spans) >= 3:
                year = spans[0].text
                duration = spans[1].text
                rating = spans[2].text
                
                #---------------Write each movie's data to the CSV file
                writer.writerow([name, year, duration, rating])
        
        print("Data successfully written to imdb_top_movies.csv")

except Exception as e:
    print(f"An error occurred: {e}")
