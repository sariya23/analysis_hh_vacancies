import requests
from datetime import datetime, time, date


def get_vacancies(keyword: str, programming_language: str="Python") -> None:
    url = "https://api.hh.ru/vacancies"
    params = {
        "text": keyword,
        "area": 113,
        "per_page": 100, 
        "experience": "noExperience",
        "currency": "RUR",
        "date_from": "2024-03-01",
    }
    headers = {
        "User-Agent": "Your User Agent",
    }

    response = requests.get(url, params=params, headers=headers)
    result = []
    if response.status_code == 200:
        data = response.json()
        vacancies = data.get("items", [])
        print(type(vacancies))
        for vacancy in vacancies:
            vacancy: dict = vacancy
            vacancy_id = vacancy.get("id")
            vacancy_title = vacancy.get("name")
            vacancy_url = vacancy.get("alternate_url")
            company_name = vacancy.get("employer", {}).get("name")
            salary = vacancy["salary"]
            # print(vacancy["salary"])
            # print(salary)
            print(vacancy)
            break
            result.append(
                [vacancy_id, vacancy_title, vacancy_url, company_name, salary, programming_language]
            )
            print(f"ID: {vacancy_id}\nTitle: {vacancy_title}\nCompany: {company_name}\nURL: {vacancy_url}\nSalary: {salary}\n\n")
        return result
    else:
        print(f"Request failed with status code: {response.status_code}")


# Example usage
a = '2024-03-06T16:55:57+0300'
print(datetime.fromisoformat(a).date())