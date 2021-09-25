from flask import Flask, render_template

app = Flask (__name__)

@app.route('/play', methods=['GET'])
def index():
    return render_template( "index.html", color='skyblue', times=3)

@app.route('/play/<int:num>', methods=['GET'])
def indexnum(num):
    return render_template( "index.html", color='skyblue', times=num)

@app.route('/play/<int:num>/<color>', methods=['GET'])
def indexnumcolor(num,color):
    return render_template( "index.html", color=color, times=num)

if __name__=="__main__":
    app.run(debug=True)