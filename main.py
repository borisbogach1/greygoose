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


@app.route('/suggested_route/<int:number>')
def suggested_route(number):
    pretty_number = str(number // 10) + str(number % 10)
    create_map('route_description/' + pretty_number + '.txt')
    values = {"number": number,
              "file_map": "../static/" + pretty_number + ".png"}
    return render_template('suggested_route.html', **values)


@app.route('/createroute', methods=["GET", "POST"])
def creareroute():
    form = SugForm
    if request.method == "POST":
        points = []
        for i in range(2, 11):
            pointx = 'point' + str(i)
            points.append(pointx)
        routepoint = []
        startpoint = d[request.form["startpoint"]]
        point1 = d[request.form["point1"]]
        routepoint.append(startpoint)
        routepoint.append(point1)

        for i in points:
            try:
                currentpoint = d[request.form[i]]
                routepoint.append(currentpoint)
            except:
                pass
        endpoint = d[request.form["endpoint"]]
        routepoint.append(endpoint)
        # point11=get_key(d,startpoint+"\n")
        # point12=get_key(d,point1+"\n")
        # point13=get_key(d,point2+"\n")
        # print(point11,point12,point13)


        file='route_description/11.txt'
        file=open(file,mode='w')
        for i in routepoint:
            file.write(i+'\t#'+'\n')
        create_map('route_description/11.txt',spn='0.01,0.01')
        values = {"number": '11',
                  "file_map": "../static/" + '11' + ".png"}
        return render_template("suggested_route.html", **values)

        return
    else:
        return render_template("createroute.html", form=form)


if __name__ == "__main__":

    create_map('route_description/01.txt', center='37.635426,55.829703')
    create_map('route_description/02.txt', center='37.635426,55.829703')
    create_map('route_description/03.txt', center='37.635426,55.829703')
    create_map('route_description/04.txt', center='37.635426,55.829703')

    d = {}

    with open('datumnn.csv', "r", encoding='utf-8') as csvfile:
        for i in range(100):
            try:
                f = csvfile.readline().split(',')
                f[1] = f[1].replace(";", ',')

                d[f[0]] = f[1]

            except:
                break

    app.run(host='0.0.0.0', port=81)
