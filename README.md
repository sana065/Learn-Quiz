# 🧠 LearnQuiz — Auto Quiz Generator

LearnQuiz is a web application built with Python and Django that automatically generates quiz questions from your uploaded study notes. Simply upload a file, choose your difficulty level, and start learning!

---

## 🚀 Features

- 📄 **Multi-format File Support** — Upload TXT, PDF, or DOCX files
- 🤖 **Auto Question Generation** — Questions generated directly from your content
- 🎯 **Difficulty Levels** — Easy, Medium, and Hard modes
- 🔢 **Custom Question Count** — Choose how many questions you want
- 📊 **Score Tracking** — See your results with percentage and grade
- 🏆 **Leaderboard** — Compete with other players
- 🎨 **Modern UI** — Clean and responsive interface with Poppins font

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.13 | Core programming language |
| Django 6.0 | Web framework |
| PyPDF2 | PDF file reading |
| python-docx | Word document reading |
| SQLite | Database |
| HTML/CSS | Frontend interface |
| Google Fonts | Poppins typography |

---

## 📚 Python Concepts Covered

| Concept | Where Used |
|---|---|
| **Virtual Environment** | Project setup and isolation |
| **OOP — Classes** | Player, Question, Result models |
| **Functions** | views.py, utils.py |
| **String Methods** | Text extraction and processing |
| **Lists & List Comprehension** | Question generation, word filtering |
| **Dictionaries** | Question data structure |
| **For Loops** | Sentence and word iteration |
| **If/Elif/Else** | Difficulty logic, grade calculation |
| **While Loop** | Options padding |
| **File I/O** | Reading uploaded files |
| **Modules** | random, PyPDF2, docx |
| **Django Framework** | URL routing, views, templates |

**##Project Structure**

learnquiz/
│
├── learnquiz/                  # Main Django project folder
│   ├── settings.py             # Project settings
│   ├── urls.py                 # Main URL configuration
│   └── wsgi.py                 # WSGI configuration
│
├── quiz/                       # Quiz application
│   ├── migrations/             # Database migrations
│   ├── templates/
│   │   └── quiz/
│   │       ├── home.html       # Landing page
│   │       ├── upload.html     # File upload page
│   │       ├── quiz.html       # Quiz page
│   │       ├── results.html    # Results page
│   │       └── leaderboard.html # Leaderboard page
│   ├── models.py               # Database models
│   ├── views.py                # Application logic
│   ├── urls.py                 # Quiz URL patterns
│   └── utils.py                # File reading & question generation
│
├── manage.py                   # Django management script
├── .gitignore                  # Git ignore file
└── README.md                   # Project documentation

---

## ⚙️ Installation & Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/sana065/Learn-Quiz.git
cd Learn-Quiz
```

### Step 2: Create Virtual Environment
```bash
python -m venv myenv
```

### Step 3: Activate Virtual Environment
```bash
# Windows
myenv\Scripts\activate

# Mac/Linux
source myenv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install django PyPDF2 python-docx
```

### Step 5: Run Migrations
```bash
python manage.py makemigrations
python manage.py makemigrations quiz
python manage.py migrate
```

### Step 6: Start the Server
```bash
python manage.py runserver
```

### Step 7: Open in Browser
http://127.0.0.1:8000/

## 🎮 How to Use

1. **Enter your name** on the home page
2. **Upload your notes** — TXT, PDF, or DOCX format
3. **Select difficulty** — Easy, Medium, or Hard
4. **Choose number of questions** — 5 to 30
5. **Answer the questions** — Fill in the blank style
6. **View your results** — Score, percentage, and grade
7. **Check leaderboard** — See how you rank

---

## 🧠 How Question Generation Works

File uploaded → Text extracted
Text split into sentences
Sentences shuffled randomly
Each sentence:

Common/stop words removed
Important word selected based on difficulty
Word replaced with "_____"
3 wrong options added from same sentence
Options shuffled randomly


Questions returned to quiz
---

## 📊 Grading System

| Percentage | Grade |
|---|---|
| 80% and above | 🏆 Excellent! |
| 60% - 79% | 👍 Good Job! |
| 40% - 59% | 📚 Keep Practicing! |
| Below 40% | 💪 Don't Give Up! |

---

## 🗄️ Database Models

### Player
```python
- name: CharField
- score: IntegerField  
- created_at: DateTimeField
```

### Result
```python
- player: ForeignKey(Player)
- topic: CharField
- correct: IntegerField
- total: IntegerField
```

### Question
```python
- topic: CharField
- question_text: TextField
- option1-4: CharField
- correct_option: IntegerField
```

---

## 🔮 Future Improvements

- [ ] User authentication and login system
- [ ] Topic-wise progress tracking
- [ ] Timer for each question
- [ ] True/False question type
- [ ] Detailed analytics dashboard
- [ ] Export results as PDF
- [ ] Mobile app version

---

## 👨‍💻 Developer

**Sana Ullah**
- 📧 sanaullah672005@gmail.com
- 💼 [LinkedIn](https://www.linkedin.com/in/sana-ullah-8a58b3280/)
- 🐙 [GitHub](https://github.com/sana065)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

*Built with ❤️ using Python & Django*

