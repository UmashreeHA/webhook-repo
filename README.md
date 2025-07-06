# webhook-repo

GitHub Webhook Receiver
This project receives GitHub Webhook events (Push and Pull Request) and displays them in a live UI. It was built as part of the TechStaX Developer Assessment.

 Tech Stack
Python 3
Flask – for the backend webhook server and UI rendering
MongoDB – to store GitHub webhook event data
HTML + JavaScript – to display events and auto-refresh every 15 seconds
ngrok – to expose local server for GitHub webhook delivery
GitHub Webhooks – to trigger data on Push and Pull Request events

 Project Structure
webhook-repo/ │ 
├── app.py # Flask app for receiving and displaying events 
├── requirements.txt # Python dependencies 
├── templates/ 
    └── index.html # UI displaying webhook events

 How to Run the App Locally
 
### 1. Clone the Repo
git clone https://github.com/UmashreeHA/webhook-repo.git
cd webhook-repo

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Start MongoDB
Make sure MongoDB is running locally on the default port 27017.
mongod
Or use MongoDB Compass if installed.

### 4. Start Flask Server
python app.py
The app will run on http://127.0.0.1:5000/.

### 5. Start ngrok
In a new terminal:
ngrok http 5000

 What You Should Do Next

1. Save this file as `README.md` in your `webhook-repo` folder.
2. Run:
   ```bash
   git add README.md
   git commit -m "Add README file"
   git push
