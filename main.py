from flask import Flask
import json
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/primenumber/<int:num>")
def prime_number(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                print(num, "is not a prime number")
                result = {
                    "Number": num,
                    "Primenumber":False
                }
                break
        else:
            print(num, "is a prime number")
            result = {
                    "Number": num,
                    "Primenumber":True
                }
                
    else:
        print(num, "is not a prime number")
        result = {
                    "Number": num,
                    "Primenumber":False
                }
    return json.dumps(result)           

if __name__ == "__main__":
    app.run(debug=True)