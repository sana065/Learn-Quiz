from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import Player, Result
from .utils import extract_text, generate_questions

def home(request):
    if request.method == 'POST':
        player_name = request.POST.get('player_name')
        player, created = Player.objects.get_or_create(name=player_name)
        request.session['player_id'] = player.id
        return redirect('upload')
    return render(request, 'quiz/home.html')

def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        difficulty = request.POST.get('difficulty', 'medium')
        num_questions = int(request.POST.get('num_questions', 10))
        
        # Text extract karo
        text = extract_text(uploaded_file)
        
        if not text.strip():
            return render(request, 'quiz/upload.html', 
                         {'error': 'File empty hai ya read nahi ho saka!'})
        
        # Questions generate karo
        questions = generate_questions(text, difficulty, num_questions)
        
        if not questions:
            return render(request, 'quiz/upload.html',
                         {'error': 'Questions generate nahi ho sake! Bara file upload karo.'})
        
        request.session['questions'] = questions
        request.session['current_question'] = 0
        request.session['score'] = 0
        request.session['difficulty'] = difficulty
        
        return redirect('quiz')
    return render(request, 'quiz/upload.html')

def quiz_page(request):
    questions = request.session.get('questions', [])
    current = request.session.get('current_question', 0)
    
    if not questions or current >= len(questions):
        return redirect('results')
    
    if request.method == 'POST':
        selected = request.POST.get('answer')
        correct = questions[current]['correct_option']
        
        if selected == correct:
            request.session['score'] = request.session.get('score', 0) + 1
        
        request.session['current_question'] = current + 1
        return redirect('quiz')
    
    question = questions[current]
    context = {
        'question': question,
        'question_number': current + 1,
        'total_questions': len(questions),
        'progress': int(((current) / len(questions)) * 100),
        'difficulty': request.session.get('difficulty', 'medium')
    }
    return render(request, 'quiz/quiz.html', context)

def results(request):
    player_id = request.session.get('player_id')
    
    try:
        player = Player.objects.get(id=player_id)
    except:
        return redirect('home')
    
    score = request.session.get('score', 0)
    questions = request.session.get('questions', [])
    total = len(questions)
    
    player.score += score
    player.save()
    
    Result.objects.create(
        player=player,
        topic=request.session.get('difficulty', 'General'),
        correct=score,
        total=total
    )
    
    percentage = int((score / total) * 100) if total > 0 else 0
    
    if percentage >= 80:
        grade = '🏆 Excellent!'
        color = '#00b894'
    elif percentage >= 60:
        grade = '👍 Good Job!'
        color = '#0984e3'
    elif percentage >= 40:
        grade = '📚 Keep Practicing!'
        color = '#fdcb6e'
    else:
        grade = '💪 Don\'t Give Up!'
        color = '#e17055'
    
    context = {
        'player': player,
        'score': score,
        'total': total,
        'percentage': percentage,
        'grade': grade,
        'grade_color': color
    }
    return render(request, 'quiz/results.html', context)

def leaderboard(request):
    players = Player.objects.all().order_by('-score')[:10]
    context = {'players': players}
    return render(request, 'quiz/leaderboard.html', context)