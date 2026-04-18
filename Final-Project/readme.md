# NeuraLearn 

An AI-powered study assistant built with Flask and Groq API (LLaMA 3.3 70B). Helps students explain topics, generate MCQs, summarize notes, and take scored quizzes.

---

## Features

- **Topic Explainer** — enter any topic and get a simple explanation with examples
- **MCQ Generator** — generates practice questions for exam prep
- **Notes Summarizer** — paste your notes, get a bullet-point summary
- **Quiz Mode** — interactive scored quiz with instant right/wrong feedback

---

## Tech Stack

- Python / Flask
- Groq API (LLaMA 3.3 70B)
- HTML, CSS
- python-dotenv

---

## How to Run Locally

1. Clone the repo
   ```
   git clone https://github.com/yourusername/neuralearn.git
   cd neuralearn
   ```

2. Install dependencies
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file and add your Groq API key
   ```
   GROQ_API_KEY=your_key_here
   ```

4. Run the app
   ```
   python app.py
   ```

5. Open `http://127.0.0.1:5000` in your browser

---

## Project Structure

```
neuralearn/
├── app.py
├── requirements.txt
├── .env
├── static/
│   └── style.css
└── templates/
    ├── index.html
    ├── explain.html
    ├── mcq.html
    ├── summarizer.html
    └── quiz.html
```

---

## Getting a Free Groq API Key

1. Go to [console.groq.com](https://console.groq.com)
2. Sign up and go to API Keys
3. Create a new key and paste it in your `.env` file

---

