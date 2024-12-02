from flask import Flask, request, jsonify, render_template_string
import webtech

app = Flask(__name__)

# Initialize WebTech scanner
wt = webtech.WebTech()

# HTML template for the home route
HOME_PAGE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WebTech Analysis API</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            background-color: #f4f4f9;
        }
        h1 {
            color: #333;
        }
        p {
            margin: 10px 0;
        }
        code {
            display: block;
            background: #e8e8e8;
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
        }
        pre {
            background: #f8f8f8;
            padding: 15px;
            border-radius: 5px;
            overflow: auto;
        }
    </style>
</head>
<body>
    <h1>Welcome to WebTech Analysis API</h1>
    <p>This API analyzes a given website URL and returns its detected technology stack. It uses the <b>WebTech</b> library to gather insights about the site's frontend, backend, CMS, infrastructure, and analytics tools.</p>
    <h2>Endpoints</h2>
    <h3>1. <code>POST /analyze</code></h3>
    <p>Send a POST request with a JSON body containing the <code>url</code> field.</p>
    <p><b>Example Request:</b></p>
    <pre>
POST /analyze HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: application/json

{
    "url": "https://example.com"
}
    </pre>
    <p><b>Example Response:</b></p>
    <pre>
{
    "url": "https://example.com",
    "technologies": {
        "CMS": ["WordPress"],
        "Frontend": ["React"],
        "Backend": ["PHP"],
        "Infrastructure": ["Nginx", "HTTP/3"],
        "Analytics": ["Google Analytics"]
    }
}
    </pre>
    <h2>How to Use</h2>
    <ol>
        <li>Start the server using <code>python app.py</code>.</li>
        <li>Send a POST request to <code>/analyze</code> with the website URL.</li>
        <li>Get a detailed report of the website's technology stack in JSON format.</li>
    </ol>
    <p>For more information or questions, please contact the developer.</p>
</body>
</html>
"""

# Home route
@app.route('/')
def home():
    return render_template_string(HOME_PAGE_HTML)

@app.route('/analyze', methods=['POST'])
def analyze_website():
    try:
        # Get URL from the request
        data = request.json
        if not data or 'url' not in data:
            return jsonify({"error": "Please provide a valid URL in the request body"}), 400

        url = data['url']

        # Analyze the website
        try:
            result = wt.start_from_url(url, timeout=30)
            print(f"Result: {result}")
            return jsonify({
                "url": url,
                "technologies": result
            })
        except webtech.utils.ConnectionException:
            return jsonify({"error": "Unable to connect to the URL. Check if the URL is reachable."}), 400
        except Exception as e:
            return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

    except Exception as e:
        return jsonify({"error": f"Invalid request format: {str(e)}"}), 400


if __name__ == '__main__':
    app.run(debug=True)
