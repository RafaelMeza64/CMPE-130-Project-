from flask import Flask, redirect, url_for, send_from_directory, render_template, request, session, flash, Markup
from DijkstraAlgo import Map

app = Flask(__name__)

g = Map([[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ], 9)

print(g.findShortestPath(0))

@app.route("/")
@app.route("/home")
def home():
    vertices = 9
    temp = g.findShortestPath(0)
    return render_template("home.html", print=temp, vertices=vertices)

if __name__ == "__main__":
    app.run(debug = True)