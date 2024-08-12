# TODO
## Accessing the Data
- add in custom session ID to the cookie header (each one expires in 10 days I think?)
    - is the cookie header going to be a problem, and is there a way to bypass it? Maybe see if an incognito browser can send a request without the cookie/session ID?
    - is logging in actually necessary, or can you make the request anonymously and increase the limit parameter and get the same result?

## UX
- build functionality for selecting industries
- Scrape data from the analysis page for each ad (API endpoint response includes total number of ads found from the given search query)

## Headers
- does timestamp header need to be correct for the request to work? Will this get me banned?
- user sign header changes with each request. Will this cause a problem?
- some requests include the cache-control header