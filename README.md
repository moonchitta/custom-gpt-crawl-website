### **README.md**

# WebTech Analysis API

## **Overview**
The **WebTech Analysis API** is a RESTful service that analyzes a given website URL to detect its underlying technologies. It identifies various technologies used in the website's infrastructure, including front-end frameworks, back-end technologies, CMS platforms, analytics tools, and server configurations. This tool leverages the WebTech library for its analysis.

---

## **Features**
- Analyze websites to detect:
  - Front-end frameworks (e.g., React, Vue.js).
  - Back-end technologies (e.g., Node.js, PHP).
  - Content Management Systems (e.g., WordPress, Drupal).
  - Infrastructure (e.g., HTTP/3, HSTS, Nginx).
  - Analytics tools (e.g., Google Analytics).
- Identify and interpret custom headers for insights into the server setup.
- Provide structured JSON responses for integration with other tools.
- A user-friendly `/` endpoint with an HTML-based guide for API usage.

---

## **Endpoints**

### **1. GET /** 
Returns a simple HTML page explaining the purpose of the API and how to use it.

- **Response**:
  - Status Code: `200`
  - Content Type: `text/html`

### **2. POST /analyze**
Analyzes the given URL and detects its underlying technologies.

- **Request**:
  - Method: `POST`
  - Content-Type: `application/json`
  - Body Example:
    ```json
    {
      "url": "https://example.com"
    }
    ```

- **Response**:
  - Status Code: `200` (Success)
  - Example JSON Response:
    ```json
    {
      "url": "https://example.com",
      "technologies": {
        "CMS": ["WordPress"],
        "Frontend": ["React"],
        "Backend": ["PHP"],
        "Infrastructure": ["HTTP/3", "HSTS"],
        "Analytics": ["Google Analytics"]
      }
    }
    ```

  - Status Code: `400` (Invalid Request)
    - Example:
      ```json
      {
        "error": "Please provide a valid URL in the request body"
      }
      ```

  - Status Code: `500` (Internal Server Error)
    - Example:
      ```json
      {
        "error": "An unexpected error occurred: <details>"
      }
      ```

---

## **Installation**

### Prerequisites
- Python 3.8 or later
- Pip package manager

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/webtech-analysis-api.git
   cd webtech-analysis-api
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the server:
   ```bash
   python app.py
   ```

---

## **Usage**

1. **Start the API**:
   - Run the server using `python app.py`. The API will be available at `http://127.0.0.1:5000`.

2. **Analyze a Website**:
   - Use tools like Postman or `curl` to send a `POST` request to the `/analyze` endpoint.
   - Example `curl` command:
     ```bash
     curl -X POST http://127.0.0.1:5000/analyze \
     -H "Content-Type: application/json" \
     -d '{"url": "https://example.com"}'
     ```

3. **Access the Home Page**:
   - Navigate to `http://127.0.0.1:5000/` in your browser to see the documentation page.

---

## **Examples**

### Example 1: Analyze `https://web.whatsapp.com`
Request:
```json
{
  "url": "https://web.whatsapp.com"
}
```

Response:
```json
{
  "url": "https://web.whatsapp.com",
  "technologies": {
    "Frontend": ["React"],
    "Infrastructure": ["HTTP/3", "HSTS"],
    "Analytics": ["Google Analytics"]
  }
}
```

---

## **Limitations**
- May not detect technologies hidden or obfuscated by the server.
- Requires the WebTech library; compatibility issues may arise with certain versions.

---

## **Contributing**
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push:
   ```bash
   git push origin feature-name
   ```
4. Create a Pull Request.

---

## **License**
This project is licensed under the [MIT License](LICENSE).

---

## **Contact**
For support or questions, please contact:
- **Email**: hammad@thexsol.com
- **Website**: [hammad.bala-kot.com](http://hammad.thexsol.com/)

