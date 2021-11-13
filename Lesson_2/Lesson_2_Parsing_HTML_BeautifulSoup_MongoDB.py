import requests
from pprint import pprint
import re
from bs4 import BeautifulSoup

main_link = 'https://hh.ru/search/vacancy'
vacancy_hh = 'Python'
search_str = 10
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (XHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'
}

n_page = 0
vacancies = []
while n_page <= search_str - 1:
    params = {
        'L_is_auto_search': 'false',
        'area': '2',
        'clusters': 'true',
        'enable_snippets': 'true',
        'text': vacancy_hh,
        'page': n_page

    }
    response = requests.get(main_link, params=params, headers=headers)

    if response.status_code == 200:
        dom = BeautifulSoup(response.text, 'html.parser')
        vacancy_list = dom.find_all('div', {'class': 'vacancy-serp-item__row vacancy-serp-item__row_header'})

        for vacancy in vacancy_list:
            vacancy_data = {}
            vacancy_name = vacancy.find('a').text
            vacancy_link = vacancy.find('a')['href']
            vacancy_salary = vacancy.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'})

            if not vacancy_salary:
                salary_min = None
                salary_max = None
                salary_currency = None
            else:
                vacancy_salary = vacancy_salary.getText().replace(u'\xa0', u'')
                vacancy_salary = re.split(r'\s|-', vacancy_salary)
                if vacancy_salary[0] == 'до':
                    salary_min = None
                    salary_max = float(vacancy_salary[1])
                    salary_currency = vacancy_salary[2]
                elif vacancy_salary[0] == 'от':
                    salary_max = None
                    salary_min = float(vacancy_salary[1])
                    salary_currency = vacancy_salary[2]
                else:
                    salary_max = float(vacancy_salary[1])
                    salary_min = float(vacancy_salary[0])
                    salary_currency = vacancy_salary[2]

            vacancy_data['name'] = vacancy_name
            vacancy_data['vacancy_link'] = vacancy_link
            vacancy_data['salary_min'] = salary_min
            vacancy_data['salary_max'] = salary_max
            vacancy_data['currency'] = salary_currency
            vacancies.append(vacancy_data)

    n_page += 1
pprint(vacancies)
