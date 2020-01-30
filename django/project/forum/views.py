import poplib

from email.parser import Parser

from django.shortcuts import render
from .models import Group
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def groups(request):
    context = {
        'groups': Group.objects.all()
    }
    return render(request, 'forum/groups.html', context)


class GroupListView(ListView):
    model = Group
    template_name = 'forum/groups.html'
    context_object_name = 'groups'


class GroupDeleteView(LoginRequiredMixin, DeleteView):
    model = Group
    success_url = '/groups'


class GroupDetailView(DetailView):
    model = Group

    def get_context_data(self, **kwargs):
        context = super(GroupDetailView, self).get_context_data(**kwargs)
        SERVER = 'pop3.poczta.onet.pl'
        username = 'email'
        password = 'Haslo'

        pop3server = poplib.POP3(SERVER)
        # print(pop3server.getwelcome())
        pop3server.user(username)
        pop3server.pass_(password)

        messages = [pop3server.retr(i) for i in range(1, len(pop3server.list()[1]) + 1)]

        messages = [b"\n".join(m[1]) for m in messages]

        messages = [Parser().parsestr(m.decode()) for m in messages]

        froms = []
        subjects = []
        contents = []

        for message in messages:
            email_from = message.get('From')
            email_subject = message.get('Subject')

            # print('From ' + email_from)
            # print('To ' + email_to)
            # print('Subject ' + email_subject)

            for part in message.walk():
                if part.get_content_type() == 'text/plain':
                    body = part.get_payload(decode=True)
                    print('tresc: ')
                    print(str(body))
                    contents.append(body)

            froms.append(email_from)
            subjects.append(email_subject)

        mylist = zip(froms, subjects, contents)
        context['myList'] = mylist
        # context['From'] = froms
        # context['Subject'] = subjects
        # context['Messages'] = contents
        return context


class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    fields = ['group_name', 'group_code']


def home(request):
    return render(request, 'forum/home.html', {'title': 'Home'})
