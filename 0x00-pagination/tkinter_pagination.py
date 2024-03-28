# This Python script tilizes the Tkinter library to create 
# a simple pagination application with themed styling.
# The app displays a Treeview widget and allows navigation between pages
# using “Previous” and “Next” buttons. 
# It includes a dynamic number of pagination buttons, 
# and each button corresponds to a page of items. 
# The script defines a PaginationApp class, showcasing the implementation of page navigation, 
# and updating the Treeview accordingly. 
# The example usage at the end demonstrates creating an instance of the app with a list of numbers and a specified page size.

# Pagination in Python:

# The pagination method used in this code involves dividing a list of items into smaller pages based on a specified page size.
# The update_treeview method calculates the start and end indices for the current page, retrieves the corresponding items, and updates the Treeview.
# The “Previous” and “Next” buttons adjust the current page, ensuring it stays within the valid range, and trigger the Treeview update.
# In essence, this method provides a clear and user-friendly way to navigate through a dataset or list of items, displaying a manageable subset at a time

import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

class PaginationApp:
    def __init__(self, master, items, page_size):
        self.master = master
        self.master.title("Pagination Example")

        self.items = items
        self.page_size = page_size
        self.current_page = 1

        style = ThemedStyle(self.master)
        style.set_theme("plastik")  # You can choose other available themes

        self.label = ttk.Label(master, text="Pagination Example", font=('Helvetica', 16, 'bold'))
        self.label.pack(pady=10)

        self.treeview = ttk.Treeview(master, columns=("Number",),
                                     show="headings", style="Treeview")
        self.treeview.heading("Number", text="Number")
        self.treeview.pack()

        self.page_buttons = []
        self.update_treeview()
        self.create_pagination_buttons()

        self.prev_button = ttk.Button(master, text="Previous", command=self.prev_page)
        self.prev_button.pack(side=tk.LEFT, padx=10)

        self.next_button = ttk.Button(master, text="Next", command=self.next_page)
        self.next_button.pack(side=tk.RIGHT, padx=10)

    def update_treeview(self):
        # Clear existing items
        self.treeview.delete(*self.treeview.get_children())

        # Get items for the current page
        start_index = (self.current_page - 1) * self.page_size
        end_index = start_index + self.page_size
        current_page_items = self.items[start_index:end_index]

        # Insert items into the treeview
        for number in current_page_items:
            self.treeview.insert("", "end", values=(number,))

    def create_pagination_buttons(self):
        max_pages = -(-len(self.items) // self.page_size)  # Ceiling division

        for page_number in range(1, max_pages + 1):
            button = ttk.Button(self.master, text=str(page_number),
                                command=lambda num=page_number: self.goto_page(num))
            button.pack(side=tk.LEFT, padx=5)
            self.page_buttons.append(button)

        self.highlight_current_page()

    def goto_page(self, page_number):
        self.current_page = page_number
        self.update_treeview()
        self.highlight_current_page()

    def highlight_current_page(self):
        for button in self.page_buttons:
            button.state(['!pressed'])
        self.page_buttons[self.current_page - 1].state(['pressed'])

    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.update_treeview()
            self.highlight_current_page()

    def next_page(self):
        max_pages = -(-len(self.items) // self.page_size)  # Ceiling division
        if self.current_page < max_pages:
            self.current_page += 1
            self.update_treeview()
            self.highlight_current_page()

# Example usage
root = tk.Tk()

# Create a list of numbers from 1 to 100
all_numbers = list(range(1, 101))

# Set the number of items per page
page_size = 10
app = PaginationApp(root, all_numbers, page_size)

root.mainloop()

