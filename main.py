from flask import Flask, render_template, request
from forms import SugForm
from createroute import create_map


app = Flask(__name__)


@app.route('/')
@app.route("/home")
def index():
    return render_template("index.html")


@app.route('/intrestpoints')
def interes_poins():
    return render_template('interestpoints.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/suggestedroutes')
def suggestedroutes():
    return render_template('suggestedroutes.html')


@app.route('/suggestedroute1')
def suggestedroute1():
    return render_template('suggestedroute1.html')


@app.route('/suggestedroute2')
def suggestedroute2():
    return render_template('suggestedroute2.html')


@app.route('/suggestedroute3')
def suggestedroute3():
    return render_template('suggestedroute3.html')


@app.route('/suggestedroute4')
def suggestedroute4():
    return render_template('suggestedroute4.html')


@app.route('/createroute', methods=["GET", "POST"])
def creareroute():
    form = SugForm
    if request.method == "POST":

        startpoint = d[request.form["startpoint"]]
        point1 = d[request.form["point1"]]
        point2 = d[request.form["point2"]]
        # point11=get_key(d,startpoint+"\n")
        # point12=get_key(d,point1+"\n")
        # point13=get_key(d,point2+"\n")
        # print(point11,point12,point13)
        coordinates = [startpoint, point1, point2]
        
        return coordinates
    else:
        return render_template("createroute.html", form=form)


if __name__ == "__main__":

    create_map('route_description/01.txt', center='37.635426,55.829703')
    create_map('route_description/02.txt', center='37.635426,55.829703')
    create_map('route_description/03.txt', center='37.635426,55.829703')
    create_map('route_description/04.txt', center='37.635426,55.829703')

    d = {}

    with open('datumnn.csv', "r") as csvfile:
        for i in range(100):
            try:
                f = csvfile.readline().split(',')
                f[1] = f[1].replace(";", ',')

                d[f[0]] = f[1]

            except:
                break

    app.run(host='0.0.0.0', port=81)
