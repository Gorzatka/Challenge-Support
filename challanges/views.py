from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Challenge, Story
from .forms import ChallengeForm


def main(request):
    #challenges = Challenge.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'challange_support_app/main.html', {'challenges': challenges})


def challenge_list(request):
    challenges = Challenge.objects.filter(challenge_status='In progress',published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'challange_support_app/challenge_list.html', {'challenges': challenges})


def challenge_detail(request, pk):
    challenge = get_object_or_404(Challenge, pk=pk)
    return render(request, 'challange_support_app/challenge_detail.html', {'challenge': challenge})


def new_challenge(request):
    if request.method == "POST":
        form = ChallengeForm(request.POST)
        if form.is_valid():
            challenge = form.save(commit=False)
            challenge.author = request.user
            challenge.published_date = timezone.now()
            challenge.save()
            return redirect('challenge_detail', pk=challenge.pk)
    else:
        form = ChallengeForm()
        return render(request, 'challange_support_app/edit_challenge.html', {'form':form})


def edit_challenge(request, pk):
    challenge = get_object_or_404(Challenge, pk=pk)
    if request.method == "POST":
        form = ChallengeForm(request.POST, instance=challenge)
        if form.is_valid():
            challenge = form.save(commit=False)
            challenge.author = request.user
            challenge.published_date = timezone.now()
            challenge.save()
            return redirect('challenge_detail', pk=challenge.pk)
    else:
        form = ChallengeForm(instance=challenge)
        return render(request, 'challange_support_app/edit_challenge.html', {'form':form})


def complete_challenge(request):
    challenges = Challenge.objects.filter(challenge_status='Complete',published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'challange_support_app/complete_challenges.html', {'challenges': challenges})


def story_list(request):
    story = Story.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'challange_support_app/story_list.html', {'story': story})

#def story_detail(request, pk):
 #   challenge = get_object_or_404(Challenge, pk=pk)
  #  return render(request, 'challange_support_app/story_detail.html', {'story': story})

