# Import necessary libraries
import os
import requests

# Configuration
api_url = "https://xyz-corp.com/api/employee-directory"
sync_file_path = "/home/platform/scripts/sync_data.txt"  # Esure both file paths are correct

def fetch_employee_data():
    try:
        # Attempt to fetch employee data from the API
        response = requests.get(api_url)
        response.raise_for_status()
        
        # Save the data to the local file
        with open(sync_file_path, 'w') as file:
            file.write(response.text) #Ensure script has correct permisiion
        
        print("Employee data successfully fetched and saved.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching employee data: {e}")

def main():
    # Fetch employee data
    fetch_employee_data()

if __name__ == "__main__":
    main()
