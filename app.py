from flask import Flask
from flask import render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle='VTM Home Page')

@app.route('/about')
def about():
    return render_template('about.html', pageTitle='About VTM')

def estimateCalculation(radius,height):
    top_area = 3.14 * float(radius)**2
    side_area = 2*(3.14*(float(radius)*float(height)))
    total_area = top_area + side_area
    total_sf = total_area/144
    total_mat = total_sf*25
    total_lab = total_sf * 15
    total_cost_estimate = total_mat + total_lab
    return total_cost_estimate

@app.route('/estimate',methods = ['GET','POST'])
def estimate():
    if request.method == 'POST':
        form = request.form
        if 'submitt' in request.form:
          

            #if form.get('submit') == 'Submit':
            radius = form['radius']
            height = form['height']
            total_cost = estimateCalculation(float(radius), float(height))
            return render_template('estimate.html',pageTitle = 'The Estimation',variable = total_cost)
    return render_template('estimate.html',pageTitle='The Estimation')
        
    #elif request.method == 'GET':
     #   return render_template('estimate.html', pageTitle='VTM Estimator')

if __name__ == '__main__':
    app.run(debug=True)