import os

def file_validations(pathname):

    # get the file extension to check if it is .csv
    name, extension = os.path.splitext(pathname)

    # Initialize a variable to set the file as invalid if there is any error
    invalid_file = False
    row_count = 0
    
    # set variable to log errors
    error_log = set()

    # dictionary to print responses
    response = {}

    # condition to check if filepath exists and if the file is .csv: if invalid return, no further checks needed
    if extension.lower() == ".csv" and os.path.exists(pathname) and os.path.isfile(pathname) and os.path.getsize(pathname) != 0:
        pass
    else:
        invalid_file = True
        print("Invalid filename or filepath")
        response = {
            "status": "error", 
            "message": "Invalid filename or filepath"
        }
        return response

    # open csv file in read mode
    with open(pathname, 'r') as csv_file:
        for row in csv_file.readlines():
            col_data = row.strip().split(',')
            row_count += 1
    
            # check if file has 3 columns 
            if len(col_data) < 3:
                invalid_file = True
                error_log.add("file has less than 3 columns")
                
            # check if file has data in all cells
            if not all(col_data):
                invalid_file = True
                error_log.add("cell data is not complete")

        # check if file has 10 rows
        if row_count < 10:
            invalid_file = True
            error_log.add("file has less than 10 rows")

    # check if file passed validations and return response
    if not invalid_file:
        response = {
            "status": "success", 
            "message": "Valid CSV file"
        }
        return response
    else:
        response = {
            "status": "error", 
            "message": ", ".join(error_log)
        }
        return response
    
        

response = file_validations("/Users/rlavanya/Desktop/sample6.CSV")
print(response)