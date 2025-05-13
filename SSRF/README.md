## SSRF Practice Challenge – Local Setup

### 🔧 Prerequisites

Make sure you have:

- Python 3 installed
- Flask (`pip install flask`)
- Ngrok (optional, for external callbacks)
- Burp Suite (optional for observing the requests)

---

## ⚙️ Architecture of the Challenge

A web app that has:

- A **user-supplied URL fetcher**
- A simulated **internal service** on `localhost:9000`
- Your goal is to extract a secret from the internal service via SSRF

---

### 📁 Folder Structure

```
ssrf-challenge/
├── app.py          ← vulnerable main app
├── internal.py     ← internal service with secrets
└── requirements.txt

```

---

### 📜 Step 1: Create `app.py` (SSRF vulnerable)

```python
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
    app.run(port=5000)

```

---

### 📜 Step 2: Create `internal.py` (internal service)

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "🏠 Internal Admin Service - Forbidden"

@app.route("/secret")
def secret():
    return "🔐 FLAG{ssrf_access_to_internal_network_success}"

if __name__ == "__main__":
    app.run(port=9000)

```

---

### 📜 Step 3: `requirements.txt`

```
Flask==2.3.2
requests==2.31.0

```

---

### 🚀 Step 4: Run the Services

In one terminal:

```bash
python internal.py

```

In another terminal:

```bash
python app.py

```

---

## 🎯 Challenge Goal

> Use the vulnerable app on port 5000 to access the internal-only service on port 9000, and extract the secret at http://127.0.0.1:9000/secret
> 

---

### ✅ Sample Exploitation

In the form, submit:

```
http://127.0.0.1:9000/secret

```

If successful, you’ll see:
