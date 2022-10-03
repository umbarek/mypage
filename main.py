from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/mypage/contact', methods=['GET', 'POST'])
def message():
   if request.method == 'GET':
       print("We received GET")
       return render_template("contact.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")

@app.route('/mypage/me', methods=['GET'])
def greeting():
    return render_template("me.html")


if __name__ == '__main__':
    app.run(debug=True)