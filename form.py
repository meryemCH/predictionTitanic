from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    results = {}
    if request.method == "POST":
     if request.form['action'] == 'Submit':
        # get url that the user has entered
        try:
            PassengerId = str(request.form['PassengerId'])
            print(PassengerId)
            print(type(PassengerId))

            json = [
                {"PassengerId": PassengerId},
                {"class": Pclass},
                {sex}
                
            ]
            r = requests.post("http://0.0.0.0:5000/predict", json=json)
            print(r.text)

            data = r.json()
            print(data)
            pred = data['prediction']

            
            survive = int(pred[1])
            print(survive)
            if survive == 0:
                results = "You would have died!"
            elif survive == 1:
                results = "Congrats, you have survived!"
            print(results)
        except:
            errors.append(
                "Unable to reach API. Please make sure it's running and try again."
               )

    return render_template('index.html', errors=errors, results=results)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
