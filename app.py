from flask import Flask, render_template, jsonify
import data

app = Flask(__name__, 
            static_folder='static',
            template_folder='templates')
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/property', methods=['GET'])
def database_data():
    propertydata = data.get_db_data()
    response = jsonify(propertydata)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


if __name__ == '__main__':
    app.run(debug=True)