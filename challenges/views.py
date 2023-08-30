from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

mounthly_challenges = {
	"january" : "Works",
	"february" : "Hello i am february",
	"march" : "Hello i am march",
	"april" : "Hello i am april",
	"may" : "Hello i am may",
	"june" : "Hello i am june",
	"july" : "Hello i am july",
	"august" : "Hello i am august",
	"september" : "Hello i am september",
	"october" : "Hello i am october",
	"november" : "Hello i am november",
	"december" : None
}

# Create your views here.
def index(request):
	months = list(mounthly_challenges.keys())

	return render(request, "challenges/index.html", {
			"months": months
		})

def mounthly_challenge_by_number(request, month):
	months = list(mounthly_challenges.keys())

	if month > len(months):
		return HttpResponseNotFound("Invalid Month")

	redirect_month = months[month - 1]
	redirect_path = reverse("mounth-challenge", args=[redirect_month]) # /challenge/january
	return HttpResponseRedirect(redirect_path)

def mounthly_challenge(request, month):
	try:
		challenge_text = mounthly_challenges[month]
		return render(request, "challenges/challenge.html", {
			"text": challenge_text,
			"month_name": month
			})
	except:
		raise Http404()