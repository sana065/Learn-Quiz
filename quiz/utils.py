import random

import PyPDF2
import docx


def extract_text(file):
    """Extract text from TXT, PDF, or DOCX files."""

    filename = file.name.lower()

    if filename.endswith(".txt"):
        return file.read().decode("utf-8", errors="ignore")

    if filename.endswith(".pdf"):
        pdf_reader = PyPDF2.PdfReader(file)
        extracted_text = []

        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                extracted_text.append(page_text)

        return "".join(extracted_text)

    if filename.endswith(".docx"):
        document = docx.Document(file)
        paragraphs = [paragraph.text for paragraph in document.paragraphs]
        return ". ".join(paragraphs)

    return ""


def generate_questions(text, difficulty="medium", num_questions=10):
    """Generate fill-in-the-blank MCQs from the given text."""

    stop_words = {
        "the", "a", "an", "is", "are", "was",
        "in", "on", "at", "to", "of", "and",
        "that", "this", "with", "for", "it",
        "as", "be", "by", "or", "but", "not"
    }

    difficulty_rules = {
        "easy": {"min_word": 3, "min_sentence": 5},
        "medium": {"min_word": 4, "min_sentence": 6},
        "hard": {"min_word": 6, "min_sentence": 8},
    }

    settings = difficulty_rules.get(difficulty, difficulty_rules["medium"])

    sentences = [sentence.strip() for sentence in text.split(".") if sentence.strip()]
    random.shuffle(sentences)

    questions = []

    for sentence in sentences:
        if len(questions) >= num_questions:
            break

        words = sentence.split()

        if len(words) < settings["min_sentence"]:
            continue

        candidate_words = [
            word for word in words
            if len(word) >= settings["min_word"]
            and word.lower() not in stop_words
        ]

        if not candidate_words:
            continue

        answer = random.choice(candidate_words)
        blank_sentence = sentence.replace(answer, "_____", 1)

        distractors = [word for word in candidate_words if word != answer]
        distractors = distractors[:3]

        while len(distractors) < 3:
            distractors.append("Unknown")

        options = [answer] + distractors
        random.shuffle(options)

        questions.append({
            "question_text": blank_sentence,
            "options": options,
            "correct_option": answer,
        })

    return questions