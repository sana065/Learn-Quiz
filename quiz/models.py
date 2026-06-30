from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Result(models.Model):
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name="results"
    )
    topic = models.CharField(max_length=100)
    correct = models.PositiveIntegerField(default=0)
    total = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.player.name} - {self.topic}"


class Question(models.Model):
    topic = models.CharField(max_length=100)
    question_text = models.TextField()

    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)

    correct_option = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.question_text[:50]