BOT_NAME = "python_vacancies"

SPIDER_MODULES = ["python_vacancies.spiders"]
NEWSPIDER_MODULE = "python_vacancies.spiders"

ROBOTSTXT_OBEY = False

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
