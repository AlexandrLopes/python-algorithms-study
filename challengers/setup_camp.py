import os

# The 10-day syllabus
themes = {
    1: "Basic Loops and Dictionaries (JSON extraction)",
    2: "Nested Loops and Complex JSON",
    3: "Exception Handling (KeyError, IndexError)",
    4: "List Comprehension",
    5: "Dictionary Comprehension",
    6: "String Manipulation (ARNs and Logs)",
    7: "Datetime Basics (Log retention)",
    8: "Functions and Modularity",
    9: "File I/O (Reading JSON, writing reports)",
    10: "Complex Aggregation (Billing and grouping)"
}

print("Starting the creation of the 10-Day Bootcamp...")

# Loop for the 10 days
for day in range(1, 11):
    folder_name = f"day-{day}"
    
    # Create the folder if it doesn't exist
    os.makedirs(folder_name, exist_ok=True)
    
    theme = themes[day]
    
    # Loop to create 300 files per day
    for ex in range(1, 301):
        file_path = os.path.join(folder_name, f"exercise-{ex:03d}.py")
        
        # Write the template inside each file
        with open(file_path, "w") as file:
            file.write(f'# Day {day} - Exercise {ex}\n')
            file.write(f'# Theme: {theme}\n\n')
            file.write('# Context: [Paste the challenge context here]\n\n')
            file.write('# TODO: Write your code below\n')
            
    print(f"Folder {folder_name} created with 300 exercises.")

print("\nBootcamp structure successfully generated! Let's get to work.")