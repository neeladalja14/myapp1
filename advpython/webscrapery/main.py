from bs4 import BeautifulSoup
import requests

"""
search = input("Enter search term: ")
params = {"q": search}
r = requests.get("https://www.bing.com/search", params = params)

soup = BeautifulSoup(r.text, "html.parser")
print(soup.prettify())

"""

# this piece of code is used to gt some parsing from the search engine.
search = input("search for: ")  # input of th search is taken from the user
params = {"q": search}
r = requests.get("https://www.bing.com/search", params=params)  # the request is sent to BING search engine for user entered keyword.

soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol", {"id": "b_results"})      # the result for the links is posted found.("b_results" is found from thinspect elememts)
links = results.findAll("li", {"class", "b_algo"})      # this is the list item from the searched page.

for item in links:      # item is looped through the list of searches.
    item_text = item.find("a").text     # related text is printed.
    item_href = item.find("a").attrs["href"]    # related attributes is printed.

    if item_text and item_href:     # if item and attributes are found, they will be printed.
        print(item_text)
        print(item_href)
        #print("parent:", item.find("a").parent)      """this line has parent of the item printed."""
        #print("Summary:", item.find("a").parent.parent.find("p").text)      """this prints summary of each elements"""

        children = item.children
        """for child in children:   #this prints out the child of the parents.
            print("Child:", child)"""
        print("Next siblings of the h2: ", children.next_sibling)       # this prints out the next siblings of the child. for searching previous one, we need to write previuos instead of next.

