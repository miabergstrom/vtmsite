from flask import Flask
from flask import render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle='VTM Home Page')

@app.route('/about')
def about():
    return render_template('about.html', pageTitle='About VTM')

@app.route('/estimate',methods = ['POST','GET'])
def estimate():
    if request.method == 'POST':
        
        form = request.form
        if form.get('submit') == 'Submit':
            radius = form['radius']
            height = form['height']
            top_area = 3.14 * radius**2
            side_area = 2*(3.14*(radius*height))
            total_area = top_area + side_area
            total_sf = total_area/144
            total_material = total_sf * 25
            total_labor = total_sf * 15
            total_cost_estimate = total_material + total_labor
            print(radius)
            print(height)
            print(total_cost_estimate)
            return render_template('estimate.html',variable = total_cost_estimate)
        else:
            pass
    elif request.method == 'GET':
        return render_template('estimate.html', pageTitle='VTM Estimator')

if __name__ == '__main__':
    app.run(debug=True)