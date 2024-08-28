# DigitalBusinessCard System
## Description
This is a simple system to create and manage digital business cards for your copmany or personal use.

## Installation
1. Clone the repository
2. Install Requirements (`pip install -r requirements.txt`)
3. Run Program (`python app.py`)
4. Change Password and supersecret key in app.py

## Routes
- `/` - Home Page → See all business cards
- `/card/<int:id>` - View a business card with the selected View
- `/links/<int:id>` - View the links of a business card
- `/create` - Create a new business card
- `/edit/<int:id>` - Edit a business card
- `/logs>` - View the access logs and filter by date and card 

## Preview
Main Page <br>
<img src="pictures/mainpage.png"> <br>

Create Card <br>
<img src="pictures/create_card.png"> <br>

Edit Card <br>
<img src="pictures/edit_card.png"> <br>

View Card (Template 1)<br>
<img src="pictures/temp_1.png"> <br>

View Card (Template 2)<br>
<img src="pictures/temp_2.png"> <br>

View Card (Template 3)<br>
<img src="pictures/temp_3.png"> <br>

Show Links<br>
<img src="pictures/Links.png"> <br>

Logs<br>
<img src="pictures/template_view_log.png"> <br>
I make a picture of the template html for private reasons <br>