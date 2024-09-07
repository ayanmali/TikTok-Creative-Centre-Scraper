# TODO
## Accessing the Data
~~- add in custom session ID to the cookie header (each one expires in 10 days I think?)~~
    ~~- is the cookie header going to be a problem, and is there a way to bypass it? Maybe see if an incognito browser can send ~~~~a request without the cookie/session ID?~~
    ~~- is logging in actually necessary, or can you make the request anonymously and increase the limit parameter and get the ~~~~same result? Does this resolve the cookie thing above?~~
### Headers
~~- does timestamp header need to be correct for the request to work? Will this get me banned?~~
- user sign header changes with each request. Will this cause a problem? -> Find the JS code that generates this token by checking the Initiator tab and following the trace to find the code that generates it
- some requests include the cache-control header
- Hypothesis:
    For a given search, there are a series of requests needed to get all the data, with the page number being different. The limit parameter is 3 for the first request and 20 for all subsequent requests. 
    The first request has an additional header than subsequent requests. Can I simply omit this header after making the request?


## UX
- build functionality for selecting industries
- Scrape data from the analysis page for each ad (API endpoint response includes total number of ads found from the given search query)
- Clean the DataFrame obtained from JSON data