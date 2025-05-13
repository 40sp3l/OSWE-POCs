from flask import Flask, request, render_template_string
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("input", "")
        response = render_template_string(user_input)  # Vulnerable to SSTI
        return response
    return '''
    <form method="POST">
        <input type="text" name="input" placeholder="Enter input here">
        <input type="submit" value="Submit">
    </form>
    '''
if __name__ == "__main__":
    app.run(debug=True)
