from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from contact.models import Contact
# from django.http import Http404


def create(request):
    # contacts = Contact.objects.filter(show=True).order_by('-id')

    # paginator = Paginator(contacts, 10)
    # page_number = request.GET.get("page")
    # page_obj = paginator.get_page(page_number)

    context = {
        # 'page_obj': page_obj,
        # 'site_title': 'Contatos - '
    }

    return render(
        request,
        'contact/create.html',
        context,
    )
