from django.shortcuts import render, render_to_response
from addressbook.models import Company, Persons


def company_list(requests):
    company_lists = Company.objects.all()
    return render_to_response('addressbook/company_list.html', locals())


def person_list(requests):
    person_lists = Persons.objects.all()
    return render_to_response('addressbook/person_list.html', locals())
