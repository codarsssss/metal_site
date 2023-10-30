import asyncio
from typing import Any
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.views import View
from django.views.generic.edit import FormView


from .bot_telegram import send_telegram_message
from .forms import FeedbackForm
from .models import Category, Product

# Create your views here.


# def send_feedback(request):
#     feedback = FeedbackForm(request.POST)
#     if feedback.is_valid():
#         feedback.save()
#         return True
#     return False


# def home_main(request):
#     categories = Category.objects.all()
#     context = {
#         "title": "Продукция",
#         "categories": categories,
#     }
#     return render(request, "home_app/index.html", context=context)


class Home(ListView):
    model = Category
    template_name = "home_app/index.html"
    context_object_name = "categories"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Продукция"
        return context


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products_list = category.products.all()
    paginator = Paginator(products_list, 15)
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


class Detail(ListView):
    template_name = "home_app/detail.html"
    # allow_empty = False
    context_object_name = "category"
    paginate_by = 2

    def get_context_data(self, object_list=None, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.filter(category__slug=self.kwargs["slug"])
        context["title"] = "Варианты поставки"
        return context

    def get_queryset(self) -> QuerySet[Any]:
        return Category.objects.filter(slug=self.kwargs["slug"])


def about(request):
    return render(request, "home_app/about.html", {"title": "О компании"})


# def contacts(request):
#     if request.method == "POST":
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             asyncio.run(
#                 send_telegram_message(
#                     f"{form.cleaned_data['name']} ({form.cleaned_data['contact_number']})\
#              - {form.cleaned_data['comment']}"
#                 )
#             )
#             form.save()
#             messages.success(
#                 request, f"В ближайшее время мы обязательно свяжемся с Вами!"
#             )
#             return redirect("home_app:contacts")
#         else:
#             context = {"title": "Контакты", "form": form}
#             return render(request, "home_app/contacts.html", context=context)
#     else:
#         form = FeedbackForm()
#         context = {"title": "Контакты", "form": form}
#         return render(request, "home_app/contacts.html", context=context)


class ContactsForm(FormView):
    form_class = FeedbackForm
    template_name = "home_app/contacts.html"
    success_url = reverse_lazy("home_app:contacts")
    extra_context = {"title": "Контакты"}

    def form_valid(self, form):
        form.save()
        asyncio.run(
            send_telegram_message(
                f"{form.cleaned_data['name']} ({form.cleaned_data['contact_number']})\
             - {form.cleaned_data['comment']}"
            )
        )
        messages.success(
            self.request, f"В ближайшее время мы обязательно свяжемся с Вами!"
        )
        return super().form_valid(form)
