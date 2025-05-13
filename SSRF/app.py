from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        try:
            res = requests.get(url, timeout=3)
            output = res.text
        except Exception as e:
            output = str(e)
        return render_template_string("""
            <h3>Result</h3>
            <pre>{{output}}</pre>
            <a href="/">Try again</a>
        """, output=output)
    return '''
        <h2>URL Fetcher</h2>
        <form method="post">
            <input type="text" name="url" placeholder="http://example.com" size="50"/>
            <button type="submit">Fetch</button>
        </form>
    '''

if __name__ == "__main__":
    app.run(port=5001)
