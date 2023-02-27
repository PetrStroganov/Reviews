from django.shortcuts import redirect, render
from .models import Review
from .forms import CreatReviewForm


def reviews_page(request):
    if request.method == "POST":
        form = CreatReviewForm(request.POST)
        if form.is_valid():
            form.save()
            # name = form.cleaned_data.get("name")
            # email = form.cleaned_data.get("email")
            # rating = form.cleaned_data.get("rating")
            # comment = form.cleaned_data.get("comment")
            # review = {
            #     "name": name,
            #     "email": email,
            #     "rating": rating,
            #     "comment": comment
            # }
            # review_object = Review.objects.create(**review)
            # review_object.save() 
            # with open("db.txt", "a", encoding="utf-8") as file:
            #     file.write(f"{name}|{email}|{rating}|{comment}\n")
            return redirect("Home")
        else:
            stx = {"reviews": Review.objects.all(), "form": form}
            return render(request, "main.html", stx)
    else:
        # with open("db.txt", encoding="utf-8") as file:
        #     data = file.readlines()
        #     reviews = []
        #     for reviewtext in data:
        #         reviewdata = reviewtext.split("|")
        #         review = {
        #             "name": reviewdata[0],
        #             "email": reviewdata[1],
        #             "rating": reviewdata[2],
        #             "comment": reviewdata[3]
        #         }
        #         reviews.append(review)
        form = CreatReviewForm()
        stx = {"reviews": Review.objects.all(), "form": form}
    return render(request, "main.html", stx)
    # Улучшить список дел, сделать его с фоном, моделью
