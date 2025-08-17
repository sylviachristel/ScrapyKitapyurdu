# 🕷️ Kitapyurdu Scraper

A Scrapy project that crawls books from Kitapyurdu website.

## 🚀 Features

- Extract book titles, authors, prices
- Store data in JSON format

## ⚙️ Technologies Used

- Python
- Scrapy

## 📦 How to Run

1. **Install the scrapy to run the project**

    ```bash
    pip install scrapy
    ```

2. **Navigate to the project folder**

    To run Scrapy from the terminal, make sure you are in the folder where `scrapy.cfg` is located. The JSON file is not included in the project folder and will be created using the terminal command.

    ```bash
    cd Scrapy-Kitapyurdu\kitapyurdu 
    ```
    
3. **Run**

    ```bash
    scrapy crawl kitapyurdu -o books.json
    ```

4. **Check the output**

    - The scraped data will be saved in `books.json`.
    - You can open it with a text editor or view it in your terminal.

## 🖼️ Screenshots

![Scrapy Output](screenshots/output.png)


