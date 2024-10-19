# FoodFinder
## Overview
FATlanta Food Finder is a web application that allows users to search for and discover restaurants in Atlanta.
Users can view restaurant locations on a map, read reviews, and get directions.
- Website: http://localhost:8000/myappp/
- Trello: https://trello.com/invite/66d9fa0ac2da3572004b2e10/ATTI91248e3c5781bc7d631ebf36ab2ad6f3D4A54191
- Repository Link: https://github.com/meetonk/FoodFinder.git
- Team Website: https://aarnwang900.wixsite.com/fatlanta-food-finder

## Directions
How to run this page:
1. Clone this repository into your local machine
2. Use cd, cd.. ls to navigate to the directory that contains requirements.txt
3. In terminal, enter pip install -r requirements.txt
4. Make sure the Python Interpreter that you are running the app on has Django installed. If not, install in settings
5. Run the website and enjoy!

## Website Functions
### Main Page (no login):
The main page hosts much of the basic functionality of the web application, allowing the user to:
- **Search for restaurants** in the left window using a central location and cuisine type, with optional settings for maximum distance (radius from central location) and rating
  - Note that the search function may not pull up all results if the maximum radius is too large
- **View the Atlanta area** on an interactive map
  - To move around the map, the user can drag the cursor (holding click and moving)
  - To zoom in and out of the map, the user can scroll up and down or click the + and - buttons in the lower right corner of the page
  - If the user has performed a search, red markers will show on the map indicating search results (restaurants in the area)
    - Clicking a red marker will cause the corresponding restaurant's detailed information window to be displayed, containing information such as the restaurant's name, address, rating, cost (1-4 $ symbols), website link, and reviews

### Main Page (with login):
If the user has logged in, the following additional features will also be available on the main page:
- A "bookmark" button will appear at the top of the search window; clicking this will cause the favorite restaurants list to be displayed in the upper right corner of the page
  - Clicking the button again will cause the list to disappear
- Clicking the "Add to Favorites" button in any restaurant's detailed information window will add the restaurant to the account's favorites list
  - If the current account has restaurants in the favorites list, flag markers will always appear on the map, showing the locations of the favorite restaurants
  - To remove the restaurant from the favorites list, the user can open the favorites list and click the "X" button in the favorites list
- A "profile" button will appear next to the bookmark button at the top of the search window; clicking this will take the user to their account's profile page

## Login Page
The login page can be accessed by either:
1. Clicking on the "Login to Add to Favorites" button in any restaurant's detailed information window
2. Clicking on the "Sign In" button in the upper right corner of the main page

The login page has the following functions:
- To **login into an account**, the user can enter a valid account username and password
- To **register a new account**, the user can click the text "Register here." to go to the account registration page
- To **reset the password of an existing account**, the user can click the text "Forgot your password?" to go to the password reset page
- To **go back to the main page**, the user can click on the logo in the upper left corner

## Password Reset Process
To reset the password of an existing account, the user must have the email account corresponding to the account.
The user should then follow these steps:
1. Enter the email account and click the "Send Reset Link" button to send an email to the email account
   - If this step is successful, on the current page, the user will be taken to a new page with the title "Password Reset Link Sent" at the top of the window
2. Go to the email account and click the button in the email from the FATlanta Food Finder website
   - At this point, the previously open FATlanta Food Finder page (password reset link sent page) can be closed
3. Follow the instructions to create a new password
   - If this step is successful, on the current page, the user will be taken to a new page with the title "Password Reset Complete" at the top of the window. Congratulations!