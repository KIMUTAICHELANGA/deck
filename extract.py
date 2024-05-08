import requests
from bs4 import BeautifulSoup
import csv

def extract_links_from_webpage(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all anchor tags with href attribute
    links = soup.find_all('a', href=True)

    # Extract the href attribute of each link
    extracted_links = [link['href'] for link in links]

    return extracted_links

def save_links_to_csv(links, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Links'])
        for link in links:
            writer.writerow([link])

def main():
    # URL of the webpage to extract links from
    url = input("Enter the URL of the webpage: ")

    # Extract links from the webpage
    extracted_links = extract_links_from_webpage(url)

    # Save the extracted links to a CSV file
    filename = 'extracted_links.csv'
    save_links_to_csv(extracted_links, filename)

    print(f"Links extracted from {url} have been saved to {filename}")

if __name__ == "__main__":
    main()
