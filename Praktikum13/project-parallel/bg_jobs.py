import requests # [cite: 13]
from bs4 import BeautifulSoup # [cite: 14]

def get_web_title(url): # [cite: 15]
    try: # [cite: 16]
        # Menambahkan timeout agar worker tidak nyangkut selamanya
        response = requests.get(url, timeout=10) # [cite: 17]
        response.raise_for_status() # [cite: 18]
        soup = BeautifulSoup(response.text, 'html.parser') # [cite: 19]
        title = soup.title.string.strip() if soup.title else "No Title Found" # [cite: 20]
        return f"SUCCESS | {url} | Title: {title}" # 
    except Exception as e: # [cite: 22]
        return f"FAILED | {url} | Error: {str(e)}" # [cite: 23]
