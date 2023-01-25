from flask import Flask, render_template, request
import requests
#create an instance of flask app
app = Flask(__name__)

@app.route("/")
def homepage():
    

    return render_template("index.html", result=None)

@app.route("/word", methods=["GET", "POST"])
def getMeaning():
    if request.method == "POST":
        word = request.form["word"]

        if word:
            result = searchWord(word)

            return render_template("index.html", result=result)

def searchWord(word):
    #free dictionary API
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    # make a request
    response = requests.get(url)

    if response.status_code == 200:
        print ("Successful")

        data = response.json()

        result = {}
        result["word"] = data[0]["word"]
        result["phonetic"] = data[0]["phonetics"][1]["text"]
        result["pos"] = data[0]["meanings"][0]["partOfSpeech"]
        result["definition"] = data[0]["meanings"][0]["definitions"][0]["definition"]
        
        print(result)
        return result
    else:
        print("ERROR ENCOUNTERED")


#main
if __name__ == "__main__":
    app.run(debug=True, port=8080)

