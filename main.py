
# Import necessary libraries
from flask import Flask, request, render_template
import gspread

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# Define the route for crawling the Google document
@app.route('/crawl_document', methods=['POST'])
def crawl_document():
    # Get the Google document link from the form
    document_link = request.form['document_link']

    # Initialize the gspread client
    gc = gspread.service_account(filename='client_secret.json')

    # Open the Google document using its ID
    document_id = document_link.split('/d/')[1].split('/')[0]
    document = gc.open_by_key(document_id)

    # Get all worksheets in the document
    worksheets = document.worksheets()

    # Initialize a list to store the extracted links
    links = []

    # Iterate through each worksheet
    for worksheet in worksheets:
        # Get all cells in the worksheet
        cells = worksheet.get_all_values()

        # Iterate through each cell and extract links
        for cell in cells:
            for item in cell:
                if 'http' in item:
                    links.append(item)

    # Return the list of extracted links
    return render_template('index.html', links=links)

# Run the Flask application
if __name__ == '__main__':
    app.run()


*Notes:*

1. You will need to create a service account and generate the `client_secret.json` file to use the gspread library for accessing Google documents.
2. Adjust the HTML template (`index.html`) according to your specific requirements for displaying the results.
3. This code assumes you have a form element with the name `document_link` in your `index.html` file to capture the Google document link from the user.