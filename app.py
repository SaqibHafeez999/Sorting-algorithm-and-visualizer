
# Import necessary libraries
import matplotlib.pyplot as plt   # for creating the plots
import matplotlib.animation as animation   # for animating the sorting
import random  # for generating random numbers
import time   # for measuring the execution time of algorithms

# Sorting Algorithms

# Quick Sort Algorithm
def quick_sort(arr, low, high, draw_callback):
    if low < high:
        pi = partition(arr, low, high, draw_callback)  # Partition the array and get the pivot index
        quick_sort(arr, low, pi - 1, draw_callback)    # Recursively sort the left part
        quick_sort(arr, pi + 1, high, draw_callback)   # Recursively sort the right part


# Partition function used by Quick Sort
def partition(arr, low, high, draw_callback):
    pivot = arr[high]  # Select the last element as pivot
    i = low - 1   # Pointer to track the smaller element
    for j in range(low, high):  # Traverse through the array
        if arr[j] < pivot:  # If current element is smaller than pivot
            i += 1   # Move the smaller element to the left
            arr[i], arr[j] = arr[j], arr[i] # Swap the elements
            draw_callback(arr,"Purple")  # color for swap
    arr[i + 1], arr[high] = arr[high], arr[i + 1]   # Swap pivot to its correct position
    draw_callback(arr,"Green")  # Mark the pivot position with a green color
    return i + 1    # Return the pivot index

# Merge Sort Algorithm
def merge_sort(arr, draw_callback):
    if len(arr) > 1:   # Base case: the array must have more than one element
        mid = len(arr) // 2  # Find the middle index of the array
        L = arr[:mid]  # Left half
        R = arr[mid:]  # Right half

        merge_sort(L, draw_callback)  # Recursively sort the left half
        merge_sort(R, draw_callback)  # Recursively sort the right half

        i = j = k = 0  # Pointers for merging
        while i < len(L) and j < len(R): # Merge the left and right halves
            if L[i] < R[j]:  # If element in left half is smaller
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            draw_callback(arr,"brown")  # Update the plot for merging step

 # If any element is left in the left half
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            draw_callback(arr,"orange")  # Color for adding elements from the left half

  # If any element is left in the right half
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            draw_callback(arr, "blue")  # Color for adding elements from the right half

# Bubble Sort Algorithm
def bubble_sort(arr, draw_callback):
    n = len(arr)
    for i in range(n):  # Outer loop for number of passes
        for j in range(0, n - i - 1):  # Inner loop for comparisons
            if arr[j] > arr[j + 1]:  # If current element is greater than next
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap the elements
                draw_callback(arr, "pink")  # color during swap

# Visualization function to initialize the plot
def visualize_sorting(algorithm):
    arr = [random.randint(1, 100) for _ in range(20)]  # Generate a random array of 20 elements

    fig, ax = plt.subplots()# Create a figure and axis for plotting
    bar_rects = ax.bar(range(len(arr)), arr, align="edge")  # Create bars for each element in the array

    ax.set_xlim(0, len(arr))  # Set x-axis range
    ax.set_ylim(0, int(max(arr) * 1.1))  # Set y-axis range
    ax.set_title(f"{algorithm.__name__.replace('_', ' ').title()} Visualization")  # Set the title dynamically
    ax.set_xlabel("Index")  # Set x-axis label
    ax.set_ylabel("Value")  # Set y-axis label


    # Callback function to update the plot during sorting
    def draw_callback(data,color):
        for rect, val in zip(bar_rects, data): # Update bar heights
            rect.set_height(val)
        for rect in bar_rects:  # Change bar colors
            rect.set_color(color)
        plt.pause(0.001)  # Pause to make the changes visible (animation delay)
    return arr, draw_callback  # Return the array and callback function

    
# Function to run a sorting algorithm and measure execution time
def run_algorithm(algorithm, arr, draw_callback):
    start_time = time.time()  # Start the timer
    # Run the appropriate algorithm (Quick Sort has low, high arguments, others do not)
    algorithm(arr, 0, len(arr) - 1, draw_callback) if algorithm == quick_sort else algorithm(arr, draw_callback)
    end_time = time.time()  # Stop the timer
    return end_time - start_time # Return the execution time

# Main function to drive the program
if __name__ == "__main__":
   while True: # Infinite loop to keep the program running
    print("Choose an algorithm (or type 'exit' to quit):")
    print("1. Quick Sort")
    print("2. Merge Sort")
    print("3. Bubble Sort")
    choice = (input("Enter your choice (1,2,3) or 'exit' to quit): ")).strip()
     # Check if the user wants to exit
    if choice.lower() == "exit":
            print("Exiting the program.")
            break # Exit the loop and end the program

        # Input validation: check if input is a valid option
    if choice not in ["1", "2", "3"]:
            print("Invalid choice! Please choose a valid option.")
            continue # Skip the rest of the loop and prompt again

# Convert choice to an integer
    choice = int(choice)

# Execute Quick Sort
    if choice == 1:
        arr, draw_callback = visualize_sorting(quick_sort)  # Prepare the plot and array for Quick Sort
        exec_time = run_algorithm(quick_sort, arr, draw_callback)   # Run Quick Sort and measure time
        print(f"Quick Sort completed in {exec_time:.4f} seconds.")  # Display execution time
        print("Time Complexity: O(n log n)")

# Execute Merge Sort
    elif choice == 2:
        arr, draw_callback = visualize_sorting(merge_sort)
        exec_time = run_algorithm(merge_sort, arr, draw_callback)
        print(f"Merge Sort completed in {exec_time:.4f} seconds.")
        print("Time Complexity: O(n log n)")

# Execute Bubble Sort
    elif choice == 3:
            arr, draw_callback = visualize_sorting(bubble_sort)
            exec_time = run_algorithm(bubble_sort, arr, draw_callback)
            print(f"Bubble Sort completed in {exec_time:.4f} seconds.")
            print("Time Complexity: O(n^2)")
    # Optional: Pause after the sorting to show the result
    time.sleep(2)  # pause for 2 seconds before the next iteration
    