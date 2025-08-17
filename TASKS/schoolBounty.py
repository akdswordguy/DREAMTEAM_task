import math

def calculate_gpa(grades):
    """Calculates GPA from a list of grades (0–100).Returns GPA on a 4.0 scale."""
    if not grades:
        return 0  

    avg = sum(grades) / len(grades)

    if avg > 90:
        return 4.0
    elif avg > 80:
        return 3.5
    elif avg > 70:
        return 3.0
    elif avg > 60:
        return 2.5
    elif avg > 50:
        return 2.0
    else:
        return 1.0 


def assign_scholarship(gpa, extracurricular_score):
    """
    Awards scholarship if:
    - GPA >= 3.5
    - Extracurricular score >= 70
    """
    if gpa > 3.5 and extracurricular_score > 70:
        return True
    return False


def normalize_scores(scores):
    """Normalizes scores to 0–1 range."""
    max_score = max(scores)  
    return [s / max_score for s in scores]


def find_top_student(students):
    """Given a list of tuples (name, score), return the name of the top scorer."""
    students.sort(key=lambda x: x[1]) 
    return students[0][0]  


def safe_divide(a, b):
    """Divides a by b and rounds up."""
    return math.ceil(a / b) 
