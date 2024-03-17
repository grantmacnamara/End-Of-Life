# Application Version Management System

This application is designed to manage and display version information for various applications. It provides two main pages:

## Index Page

The index page displays a table of applications along with their latest version, release date, and end of life date. It allows users to search for specific applications and view detailed information about each application by clicking on its name.

**Features of the Index Page:**
- **Table Display**: Shows a list of applications with their key information.
- **Search Functionality**: Users can search for specific applications using a search box.
- **Detailed Information**: Clicking on an application name opens a modal popup displaying all versions and additional details.

## Report Page

The report page generates a table of applications that will go out of date within six months of the current date. It helps users identify applications that require attention due to upcoming end of life dates.

**Features of the Report Page:**
- **Upcoming End of Life Applications**: Displays a list of applications that will go out of date within the next six months.
- **Navigation**: Includes a "Home" button to return to the index page for further exploration.

## Usage

1. **Index Page**: Visit the index page to view a comprehensive list of applications and their versions.
2. **Search**: Utilize the search box to quickly find specific applications.
3. **Detailed Information**: Click on an application name to view detailed information about its versions.
4. **Report Page**: Navigate to the report page to identify applications with upcoming end of life dates.

## Technologies Used

- Python Flask: Backend framework for handling server requests and rendering HTML templates.
- Jinja2: Templating engine for generating dynamic HTML content.
- Bootstrap: Frontend framework for designing responsive and visually appealing web pages.
- JavaScript: Used for client-side interactivity and AJAX requests.

## Installation

1. Clone the repository to your local machine.
2. Install Python and required dependencies using `pip install -r requirements.txt`.
3. Run the Flask application using `python app.py`.
4. Access the application in your web browser at `http://localhost:5000`.


