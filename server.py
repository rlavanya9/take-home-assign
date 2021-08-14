from flask import Flask, render_template, request, flash, session, redirect
from jinja2 import * # StrictUndefined
import os
import click



app = Flask(__name__)
app.secret_key = "poij;lkrjaf;"
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True
app.config['UPLOAD_EXTENSIONS'] = ['.csv']


@app.route('/')
def homepage():
    """View homepage."""

    return render_template('/homepage.html')

@app.route('/validate_file', methods=['POST'])
def upload_file():
    
    uploaded_file = request.files['file']

    # save the uploaded file
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
    

    # get the file name and extension to check if it is .csv
    file_name = uploaded_file.filename
    name, extension = os.path.splitext(file_name)

    # Initialize a variable to set the file as invalid if there is any error
    invalid_file = False
    row_count = 0
    
    # set variable to log errors
    error_log = set()

    # dictionary to print responses
    response = {}

    # condition to check if file format is .csv and fiile is not empty, if so no further checks needed
    # if extension.lower() == ".csv" and os.path.exists(pathname) and os.path.isfile(pathname) and os.path.getsize(pathname) != 0:
    if extension.lower() in app.config['UPLOAD_EXTENSIONS']:
        pass
    else:
        invalid_file = True
        response = {
            "status": "error", 
            "message": "Invalid file format"
        }
        flash(response)
        return redirect('/')

    # open csv file in read mode
    with open(file_name, 'r', encoding="utf-8") as csv_file:
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
        flash(response)
        return redirect('/')
    else:
        response = {
            "status": "error", 
            "message": ", ".join(error_log)
        }
        flash(response)
        return redirect('/')

@click.command()
@click.option("--host", default="0.0.0.0", help="hostname for flask webapp")
@click.option("--port", default=5000, help="port for flask webapp")
def main(host, port):
    app.run(debug=True, host=host, port=port)

if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0')
    main()