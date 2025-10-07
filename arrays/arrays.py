"""
Author: Hetvi Patel
Date: 2025-10-06
Description: Demonstration of array operations in Python.
"""

def insert_element(arr, element, position):
    """Insert an element at a given position in the array."""
    return arr[:position] + [element] + arr[position:]

def delete_element(arr, position):
    """Delete element at position if valid."""
    if position < 0 or position >= len(arr):
        return "Invalid position"
    return arr[:position] + arr[position+1:]

def search_element(arr, element):
    """Return index of element or -1 if not found."""
    return arr.index(element) if element in arr else -1

def reverse_array(arr):
    """Return reversed array."""
    return arr[::-1]

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    print("Original:", data)
    print("Insert:", insert_element(data, 99, 2))
    print("Delete:", delete_element(data, 3))
    print("Search:", search_element(data, 4))
    print("Reversed:", reverse_array(data))
