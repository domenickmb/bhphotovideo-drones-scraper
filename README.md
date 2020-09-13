# bhphotovideo-drones-scraper.py
A webscraper that extracts product details about drones on [B&H Photo Video](https://bhphotovideo.com) using the [Scrapy](https://scrapy.org) framework. **Note**: This program is for educational purposes only.

***

## Extracted Data
The web scraper will extract the following data:

  * Product Name
  * Product Price
  * Key Features
  * Availability
  * Image Link
  * Product Link
  
The output data will be exported as a csv format and will be save to 'drones.csv' on the same directory where you run the program.

***

## Prerequisite
The scraper is using the [Scrapy](https://scrapy.org) framework, so it needs to be installed first. Open a terminal and type:
```
$ pip install scrapy
```

***

## Downloading and running the program
Download and extract the zip file on this repo or clone it if you have git installed on your system.
```
$ git clone 'https://github.com/domenickmb/bhphotovideo-drones-scraper.git'
```

Then `cd` to 'bhphotovideo-drones-scraper' directory  
```
$ cd bhphotovideo-drones-scraper
```

Now run the program by typing:  
```
$ python bhphotovideo-drones-scraper.py
```

***

## Screenshot
Screenshot of running the program and opening the output file  
![screenshot](/images/screenshot.jpg)