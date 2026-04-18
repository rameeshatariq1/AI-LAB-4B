# NeuraLearn 
### AI-Powered Study Assistant

A web app that helps students study smarter using AI. Built with Flask and powered by LLaMA 3.3 via Groq API.

---

## What it does

NeuraLearn has 4 main features:

**1. Topic Explainer**
Type any topic and choose your level (beginner, intermediate, or advanced). The AI gives you a clear explanation with a real-life example - no confusing jargon.

**2. MCQ Generator**
Enter a subject and get 3, 5, or 10 multiple choice questions instantly. Great for quick revision before exams.

**3. Notes Summarizer**
Paste your long lecture notes and get a short, clean bullet-point summary. Saves a lot of time.

**4. Quiz Mode** 
Pick a topic, choose how many questions you want, and take an interactive quiz. It shows you correct/wrong answers in real time and gives you a final score with percentage at the end.

---

## Tech Stack

- **Backend** — Python, Flask
- **AI Model** — LLaMA 3.3 70B (via Groq API)
- **Frontend** — HTML, CSS

---

## Project Structure

```
neuralearn/
│
├── app.py                  
├── requirements.txt        
├── .env                                  
│
├── templates/
│   ├── index.html         
│   ├── explain.html       
│   ├── mcq.html            
│   ├── summarizer.html    
│   └── quiz.html           
└── static/
    └── style.css           
```

---

## How to Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/rameeshatariq1/lab13-project.git
cd lab13-project
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Add your API key**

Create a `.env` file in the root folder:
```
GROQ_API_KEY=your_groq_api_key_here
```
Get a free API key at [console.groq.com](https://console.groq.com)

**4. Run the app**
```bash
python app.py
```

Open your browser and go to `http://127.0.0.1:5000`

---


## Why I built this

I'm a BS Artificial Intelligence student and I wanted to build something actually useful for studying. Instead of switching between different tools, I wanted everything in one place — explanations, MCQs, summaries, and a proper quiz with scoring. NeuraLearn is that tool.

---

## Future Ideas

- Add PDF upload support (summarize from file)
- Save quiz history
- Add more subjects/categories
- Mobile app version

---