from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse, include
from django.template.loader import render_to_string

months_dict = {
    "january": "This is January!",
    "february": "This is February!",
    "march": "This is March!",
    "april": "This is April!",
    "may": "This is May!",
    "june": "This is June!",
    "july": "This is July!",
    "august": "This is August!",
    "september": "This is September!",
    "october": "This is October!",
    "november": "This is November!",
    "december": "This is December!"
}
# Create your views here.


def index(request):
    list_monthitems = ""
    months = list(months_dict.keys())

    for item in months:
        capitialized_month = item.capitalize()
        month_path = reverse("month_challenge", args=[item])
        list_monthitems += f"<h1><li><a href=\"{month_path}\">{capitialized_month}</a></li></h1>"

    response_data = f"<ul>{list_monthitems}</ul>"
    return HttpResponse(response_data)


def dynamic_month_by_number(request, displaymonth):  # pathconverters
    months = list(months_dict.keys())

    if displaymonth > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[displaymonth-1]
    # which is equivalent to "/challenge/january"
    redirect_path = reverse("month_challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def dynamic_month(request, displaymonth):
    month = displaymonth.lower()  # Convert to lowercase to match dictionary keys
    try:
        challenge_text = months_dict[month]
        # Pass challenge_text to the template context
        return render(request, "challenges/challenge.html", {"challenge_text": challenge_text})
    except KeyError:
        # Handle the case where the month is not in the dictionary
        return HttpResponseNotFound("<h2>This month is not supported!</h2>")



# def dynamic_month(request, displaymonth):
#     try:
#         challenge_text = months_dict[displaymonth]
#     # response_data = f"<h1>{challenge_text}</h1>"
#         response_data = render_to_string("challenges\challenge.html")
#         return HttpResponse(response_data)

#     except:
#         return HttpResponseNotFound("<h2> This month is not supported! </h2>")
