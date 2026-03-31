from django.shortcuts import render, get_object_or_404
<<<<<<< HEAD
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Course, Enrollment, Submission


# ✅ Course list (HOME PAGE)
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'onlinecourse/course_list_bootstrap.html', {'courses': courses})


# ✅ Course detail (LESSONS + EXAM PAGE)
def course_detail(request, course_id):
    course = Course.objects.get(pk=course_id)
    return render(request, 'onlinecourse/bootstrap.html', {'course': course})


# ✅ Submit exam
def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    user = request.user

    enrollment, created = Enrollment.objects.get_or_create(
        user=user,
        course=course
    )

    submission = Submission.objects.create(enrollment=enrollment)

    choices = extract_answers(request)
    submission.choices.set(choices)

    return HttpResponseRedirect(
        reverse('onlinecourse:exam_result', args=(course.id, submission.id,))
    )


# ✅ Extract answers
def extract_answers(request):
    submitted_answers = []

    for key in request.POST:
        if key.startswith('choice'):
            value = request.POST[key]
            choice_id = int(value)
            submitted_answers.append(choice_id)

    return submitted_answers


# ✅ Show result
def show_exam_result(request, course_id, submission_id):
    context = {}

    course = get_object_or_404(Course, pk=course_id)
    submission = Submission.objects.get(id=submission_id)

    choices = submission.choices.all()

    total_score = 0

    for choice in choices:
        if choice.is_correct:
            total_score += choice.question.grade

    context['course'] = course
    context['grade'] = total_score
    context['choices'] = choices

    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)
=======
from .models import Question, Choice, Submission


def submit(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.method == "POST":
        selected_choice_id = request.POST.get("choice")
        selected_choice = get_object_or_404(Choice, pk=selected_choice_id)

        # Save submission
        Submission.objects.create(
            question=question,
            selected_choice=selected_choice
        )

        return show_exam_result(request, question.id)

    return render(request, "onlinecourse/course_details_bootstrap.html", {"question": question})


def show_exam_result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all()

    correct_choices = choices.filter(is_correct=True)
    selected_choice_id = request.POST.get("choice")

    score = 0
    if selected_choice_id:
        selected_choice = get_object_or_404(Choice, pk=selected_choice_id)
        if selected_choice in correct_choices:
            score = 100

    context = {
        "question": question,
        "choices": choices,
        "score": score,
    }

    return render(request, "onlinecourse/course_details_bootstrap.html", context)
>>>>>>> d05fa7e23c773d15ac1cbf4f8652cfff7e3b2a4b
