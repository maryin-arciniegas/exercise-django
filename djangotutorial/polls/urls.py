from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    path("add", views.create_question, name="add"),
    path("update/<int:question_id>", views.update_question, name="update"),
    path("delete/<int:question_id>", views.delete_question, name="delete"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]