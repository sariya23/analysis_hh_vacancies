import requests
from bs4 import BeautifulSoup


def get_count_viwers(vacancy_id: int) -> int:
    headers = {
        "User-Agent": "Your User Agent",
    }
    url = f"https://hh.ru/vacancy/93341729"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")
        v = soup.findAll('div', class_="noprint")[0]
        return v
    else:
        raise ValueError


print(get_count_viwers(93341729))