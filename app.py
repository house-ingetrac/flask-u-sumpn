from flask import Flask
app = Flask(__name__) #create instance of class

#assign following fxn to run when root route requested
@app.route("/")
def hello_world():
    return "<i><b><small><small>No</small> hablo</small> queso!</i></b>"

#/bye
@app.route("/bye")
def goodbye():
    return "<i><b>Thanks for visiting!</i></b>"

#/inception
@app.route("/inception")
def inception():
    return "<code>@app.route(inception)<BR>def inception():<small><BR>    @app.route(inception)<BR    def inception():<BR><small>        @app.route(inception):<BR>        def inception():<BR>        <small>...</small></small></small></code>"

if __name__ == "__main__":
    app.debug = True
    app.run()
