import scrapy
from scrapy.http import Response

from python_vacancies.config import PARSE_URL, DOMAIN, TECHNOLOGIES


class DjinniVacanciesSpider(scrapy.Spider):
    name = "vacancies"
    allowed_domains = [DOMAIN]
    start_urls = [PARSE_URL]

    def parse(self, response: Response, **kwargs):
        for vacancy in response.css(".job-list-item"):
            vacancy_detail_url = (
                vacancy.css(".job-list-item__link::attr(href)").get()
            )

            yield response.follow(
                vacancy_detail_url, callback=self._parse_single_vacancy
            )

        next_page = response.css(
            "li.page-item:last-child a.page-link::attr(href)"
        ).get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def _parse_single_vacancy(self, response: Response):
        english_level_text = response.xpath(
            '//div[contains(text(), "Англійська:")]/text()'
        ).get()

        english_level = (
            english_level_text.replace("Англійська:", "").strip() \
            if english_level_text else ""
        )

        yield {
            "Title": response.css("h1::text").get().strip(),
            "Technologies": self._find_technologies(response),
            "English level": english_level,
            "Url": response.url,
        }

    def _find_technologies(self, response: Response) -> list:
        current_vacancy_stack = []

        for tech in TECHNOLOGIES:
            if tech.lower() in response.css(".mb-4").get().lower():
                current_vacancy_stack.append(tech)

        return current_vacancy_stack
