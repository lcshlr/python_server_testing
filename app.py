from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def calc():
    try:
        numbers = request.args.get("numbers").split(',')
        intNumbers = [int(i) for i in numbers]
        meanResult = sum(intNumbers) / len(intNumbers)
        return f'La moyenne de {"+".join(numbers)} est {meanResult}'
    except:
        return "Vous devez spécifier une liste de nombre dans l'attribut numbers"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')