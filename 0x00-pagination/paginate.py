# In the Python function, `paginate`, takes a list of items,
# a page size, and a page number as input and returns the subset 
# of items corresponding to the specified page.

# In the example usage, a list of numbers from 1 to 100 is created,
# and the function is used to retrieve and print the items for the first page
# (page number 1) with a page size of 10 and result displays the content of 
# the first page, showcasing the simplicity of the pagination functionality.

def paginate(items, page_size, page_number):
    start_index = (page_number - 1) * page_size
    end_index = start_index + page_size
    return items[start_index:end_index]

# Example usage
# Example: a list of numbers from 1 to 100 is created
numbers = range(1, 101)

# Retrieve and display the items for the first page (page number 1) with a page size of 10
first_page = paginate(numbers, 10, 1)
print("Items on the first page:")
for item in first_page:
    print(item)
