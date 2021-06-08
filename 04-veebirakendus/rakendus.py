from flask import Flask, request, render_template
import random

app = Flask(__name__)

@app.route("/")
def index():
    miinimum = request.args.get("miinimum", default=1, type=int)
    maksimum = request.args.get("maksimum", default=100, type=int)
   
    juhuslik_arv = random.randint(miinimum,maksimum)
    return render_template(
        "index.html",
        arv=juhuslik_arv,
        miinimum=miinimum,
        maksimum=maksimum
        )

if __name__ == "__main__":
    app.run(debug=False)