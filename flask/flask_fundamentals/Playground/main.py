from flask import Flask,render_template
app = Flask(__name__)    
@app.route('/play')         
def play():
    return render_template('index.html',num=3,color="aqua")

@app.route('/play/<num>')    
def index(num):
    # num=int(num)
    return render_template("index.html",num=int(num),color="aqua")
@app.route('/play/<num>/<color>')   

def color(color,num):
    return render_template("index.html",num=int(num),color=color)
if __name__=="__main__":    
    app.run(debug=True)   
