# django-scrapy
Django-Scrapy Integration

This project integrates the Django and Scrapy frameworks.
For example, a scrapping of blog posts http://blog.wattpanel.com.br/ is done, creating in django a Blog model with title, posted_at date and short_text.

## How to run (testing)
1. Install requirements
    ```
    $ pip install -r requirements.txt
    ```
2. Migrate DB
    ```
    $ make django-migrate
    ```
3. Copy staticfiles
    ```
    $ make django-static
    ```
4. Scrapping blog data
    ```
    $ make scrapy-wattpanel
    ```
5. Run project
    ```
    $ make django-run
    ```
    You access the project on browser by localhost url.

## TO DO
* Tests
* Improve front-end
* Improve spider to scrapping more data
