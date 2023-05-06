from flask import Flask, request, render_template, jsonify
# from flask imported Flask,request,render_template,jsonify
#
app = Flask(__name__)


@app.route('/')  # this is homepage
def home_page():
    # render_template will return whatever is there in index.html
    return render_template('index.html')


@app.route('/math', methods=['POST'])
# request.method=='POST' this is not visible in url
# request.method is post or get and request.form is of id of html
def math_ops():
    if (request.method == 'POST'):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if ops == 'add':
            r = num1+num2
            result = "The sum of " + \
                str(num1) + 'and ' + str(num2) + " is " + str(r)
        if ops == 'subtract':
            r = num1-num2
            result = "The subtract of " + \
                str(num1) + ' and ' + str(num2) + " is " + str(r)
        if ops == 'multiply':
            r = num1*num2
            result = "The multiply of " + \
                str(num1) + ' and ' + str(num2) + " is " + str(r)
        if ops == 'divide':
            r = num1/num2
            result = "The divide of " + \
                str(num1) + '  and ' + str(num2) + " is " + str(r)

        # this is given to the result of results.html
        return render_template('results.html', result=result)

# this sends to postman_action route


@app.route('/postman_action', methods=['POST'])
def math_ops1():
    if (request.method == 'POST'):
        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if ops == 'add':
            r = num1+num2
            result = "The sum of " + \
                str(num1) + 'and ' + str(num2) + "is " + str(r)
        if ops == 'subtract':
            r = num1-num2
            result = "The subtract of " + \
                str(num1) + 'and ' + str(num2) + "is " + str(r)
        if ops == 'multiply':
            r = num1*num2
            result = "The multiply of " + \
                str(num1) + 'and ' + str(num2) + "is " + str(r)
        if ops == 'divide':
            r = num1/num2
            result = "The divide of " + \
                str(num1) + 'and ' + str(num2) + "is " + str(r)

        return jsonify(result)
# this sends to postman
# postman is api testing


if __name__ == "__main__":
    app.run(host="0.0.0.0")  # this runs the app
# get is public and post is more secured
