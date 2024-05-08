import csv
import os
import webbrowser
import time

# Load links from CSV file
def load_links_from_csv(csv_file):
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        links = [row[0] for row in reader]
    return links

# Write remaining links to CSV file
def write_links_to_csv(csv_file, links):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Link"])
        for link in links:
            writer.writerow([link])

# Function to filter links
def filter_links(links):
    filtered_links = [link.strip() for link in links if "/status/" in link]
    return filtered_links

# Specify the path to your CSV file
csv_file = 'deck.csv'

# Load links from CSV
links = load_links_from_csv(csv_file)

# Filter the links
filtered_links = filter_links(links)

# Open each filtered link with a one-minute interval
for link in filtered_links:
    webbrowser.open(link)
    time.sleep(60)  # Wait for one minute before closing the current link
    os.system("taskkill /im msedge.exe /f") # Replace msedge.exe with the browser's process name
    time.sleep(120) # Wait for three minutes before opening the next link
    filtered_links.remove(link) # Remove the opened link from the list
    write_links_to_csv(csv_file, filtered_links) # Write the remaining links to the CSV file

