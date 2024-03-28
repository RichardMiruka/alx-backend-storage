# sample dataset

dataset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Define page size for pagination
page_size = 3

# calculate total number of items
total_items = len(dataset)

# calculate total number of pages
total_pages = (total_items + page_size -1) // page_size

# print the result

print("Total pages: ", total_pages)

# In this example, we have a sample dataset with 20 items.
# We define the page_size as 3, and then calculate the total_items using the len() function.
# Next, we calculate the total_pages using the formula described earlier. 
# The formula takes into account the total number of items and the desired page size. 
# By adding (+ page_size — 1) to the total number of items and then performing integer division (// page_size), 
# we get the correct number of pages, accounting for any remaining items that may not fill a complete page.

# Finally, we print the total_pages to see the result.