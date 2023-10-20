from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import FeedbackForm
from .models import Category, Product

# Create your views here.


# def send_feedback(request):
#     feedback = FeedbackForm(request.POST)
#     if feedback.is_valid():
#         feedback.save()
#         return True
#     return False


def home_main(request):
    categories = Category.objects.all()
    context = {
        "title": "Продукция",
        "categories": categories,
    }
    return render(request, "home_app/index.html", context=context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products_list = category.products.all()
    paginator = Paginator(products_list, 32)
    page_num = request.GET.get("page")
    try:
        products = paginator.page(page_num)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(
        request,
        "home_app/detail.html",
        {
            "category": category,
            "products": products,
        },
    )


def about(request):
    return render(request, "home_app/about.html", {"title": "О компании"})


def contacts(request):
    # if request.method == "POST":
    #     if send_feedback(request):
    #         return redirect("home_app:contacts")
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home_app:contacts")
        else:
            context = {"title": "Контакты", "form": form}
            return render(request, "home_app/contacts.html", context=context)
    else:
        form = FeedbackForm()
        context = {"title": "Контакты", "form": form}
        return render(request, "home_app/contacts.html", context=context)
