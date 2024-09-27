import itertools

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

# Function to perform pairwise comparison and sort the values
def sort_values(values):
    sorted_values = values.copy()
    
    for i, j in itertools.combinations(range(len(values)), 2):
        preferred = compare_values(sorted_values[i], sorted_values[j])
        if preferred == sorted_values[j]:
            # Swap the values if the current pair is out of order
            sorted_values[i], sorted_values[j] = sorted_values[j], sorted_values[i]
    
    return sorted_values

# Function to write the sorted values to the output file
def write_sorted_values(filename, sorted_values):
    with open(filename, 'w') as file:
        for value in sorted_values:
            file.write(value + '\n')

# Main function
def main(input_file, output_file):
    values = read_values(input_file)
    sorted_values = sort_values(values)
    write_sorted_values(output_file, sorted_values)
    print(f"Sorted values have been written to {output_file}.")

# Example usage
if __name__ == "__main__":
    input_file = 'values.txt'  # Input text file containing values
    output_file = 'sorted_values.txt'  # Output text file for sorted values
    main(input_file, output_file)
