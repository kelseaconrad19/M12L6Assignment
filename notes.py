def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n):
    if n <= 1: # 6
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(factorial(5))
print(fibonacci(6))

# Exercise 1
def find_file(file_system, file_name):
    for item in file_system:
        if item == file_name:
            return f"Found {file_name}"
        elif isinstance(item, list):
            result = find_file(item, file_name)
            if result:
                return result
    return f"File {file_name} not found."

file_system = ["folder 1", ["subfolder", "report.pdf"], "folder"]
print(find_file(file_system, "report.pdf"))
print(find_file(file_system, "presentation.pptx"))

# Exercise 2
def calculate_total_file_size(file_system):
    total_size = 0

    for item in file_system:
        if isinstance(item, int):
            total_size += item
        elif isinstance(item, list):
            total_size += calculate_total_file_size(item)
    return total_size

file_system2 = [[10, 20, 30], [15, [25, 35]], 40, [45, [55, 65]], 70]
print(calculate_total_file_size(file_system2))