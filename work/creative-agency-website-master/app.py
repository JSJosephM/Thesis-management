from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')  # Change to your desired default page

@app.route('/indexforinv')
def indexforinv():
    return render_template('indexforinv.html')

@app.route('/indexforpro')
def indexforpro():
    return render_template('indexforpro.html')

# Add routes for other pages as needed

if __name__ == '__main__':
    app.run(debug=True)
