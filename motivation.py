import random

motivaciones = [
    "Every small step forward still counts as progress.",
    "You don't have to be perfect, you just have to start.",
    "Mistakes are proof that you're actually trying.",
    "Consistency beats intensity in the long run.",
    "Your future self will thank you for the effort you put in today.",
    "Progress is progress, no matter how slow.",
    "The hardest part is usually just starting.",
    "You are capable of more than you think.",
    "Focus on being better than you were yesterday.",
    "Discipline is choosing what you want most over what you want now.",
    "Every expert was once a beginner.",
    "Small habits, repeated daily, create big results."
]

def random_motivation():
    return random.choice(motivaciones)

sentence = random_motivation()
print(sentence)