# CurrencyScraper
Get currecy data with Scrapy

> Usage

### If you want to fetch currecy data for TRY;

 * ``` scrapy crawl currency ``` 
 
 or write to json file

``` scrapy crawl currency -o scrapy.json ```


### If you want to getch bank sell-buy value

``` scrapy crawl <currecyTipe> -o scrapy.json ```  

> (currencyTipe = eur, usd, gld ext.)
  
  or
  
``` scrapy crawl <currencyTipe> ```   
