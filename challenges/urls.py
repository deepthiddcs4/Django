from django.urls import path

from . import views

# hard coding every month
# urlpatterns = [
#     path("january", views.january),  # URLconf
#     path("february", views.february)
# ]

# dynamically adding using place holders
urlpatterns = [
    # order of int,string matters
    path("", views.index), #for "/challenges/""
    path("<int:displaymonth>", views.dynamic_month_by_number),
    path("<str:displaymonth>", views.dynamic_month, name="month_challenge")

]
