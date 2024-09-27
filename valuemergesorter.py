# Function to read values from the input file
def read_values(filename):
    values = []
    with open(filename, 'r') as file:
        for line in file:
            value = line.strip()
            if value:
                values.append(value)
    return values

# Function to compare two values and return the preferred one
def compare_values(value_a, value_b):
    print(f"Do you rank '{value_a}' over '{value_b}'? (y/n): ", end="")
    response = input().strip().lower()
    return value_a if response == 'y' else value_b

# Merge two sorted lists using pairwise comparison
def merge(left, right):
    result = []
    while left and right:
        if compare_values(left[0], right[0]) == left[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    # Append any remaining values
    result.extend(left if left else right)
    return result

# Function to perform merge sort with pairwise comparisons
def merge_sort(values):
    if len(values) <= 1:
        return values
    
    mid = len(values) // 2
    left = merge_sort(values[:mid])
    right = merge_sort(values[mid:])
    
    return merge(left, right)

# Function to write the sorted values to the output file
def write_sorted_values(filename, sorted_values):
    with open(filename, 'w') as file:
        for value in sorted_values:
            file.write(value + '\n')

# Main function
def main(input_file, output_file):
    # Read the values from input file
    values = read_values(input_file)
    
    # Sort values using merge-sort inspired pairwise sorting
    sorted_values = merge_sort(values)
    
    # Write the sorted values to the output file
    write_sorted_values(output_file, sorted_values)
    print(f"Sorted values have been written to {output_file}.")

# Example usage
if __name__ == "__main__":
    input_file = 'values.txt'  # Input text file containing values
    output_file = 'sorted_values.txt'  # Output text file for sorted values
    main(input_file, output_file)
