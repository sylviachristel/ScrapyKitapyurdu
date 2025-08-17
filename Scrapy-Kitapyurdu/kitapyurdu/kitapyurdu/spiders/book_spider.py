import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    page_count = 1
    book_count = 1 # Counter for the queue of the books
    
    start_urls = [
        "https://www.kitapyurdu.com/cok-satan-kitaplar/haftalik/1.html",
        
    ]

    def parse(self, response):
        book_names = response.css("div.name.ellipsis a span::text").extract()
        book_authors = response.css("div.author span a span::text").extract()
        book_publishers = response.css("div.publisher span a span::text").extract()

        i = 0 # 20 books in the page
        while (i< len(book_names)): 
            # To write in the json file
            yield {
                "name": book_names[i], #Current index value
                "author": book_authors[i],
                "publisher": book_publishers[i],
            }
           
            self.book_count += 1 # Counter for the book

            i += 1
        next_url = response.css("a.next::attr(href)").extract_first()
        self.page_count += 1

        if next_url is not None and self.page_count != 5: # Get first 5 page
            yield scrapy.Request(url = next_url,callback = self.parse) # Firt url request and then parsing
        
