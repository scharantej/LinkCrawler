## Flask App Design: Google Document Link Crawler

### HTML Files
1. **index.html**:
   - This is the main HTML file that will serve as the user interface for the application.
   - It will include the necessary form elements for the user to specify the Google document link to be crawled.
   - It will also contain a section to display the results of the crawl, such as the list of links extracted from the document.


### Routes

1. **index**:
   - This route will handle the rendering of the `index.html` file.
   - It will display the user interface for the application.


2. **crawl_document**:
   - This route will handle the submission of the Google document link entered by the user.
   - It will use a suitable Python library, such as `gspread`, to access the specified Google document.
   - It will parse the document's content to extract all the links present in it.
   - The extracted links will be stored in a data structure (e.g., a list or dictionary) to be displayed on the `index.html` page.