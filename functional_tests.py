from selenium import webdriver

browser = webdriver.Firefox()

# User goes to the homepage
browser.get('http://localhost:8000')

# user reads the page title
assert 'To-Do' in browser.title

# user invited to enter a to-do item straight away

# user types "feed kitties" into a text box

# when the user presses enter, the page updates, and now the page lists "feed kitties" as an item
# in the to-do list

# there is still a text box inviting the user to add another item. they enter "clean litter box"

# the page updates again, and now shows both items on their list

# the user wonders if the site will remember their list. then they see that the site has generated
# a unique url for her (there is also some explanatory text to that efffect)

# the user visits that url and sees their to-do list is still there

# the user exits the page

browser.quit()