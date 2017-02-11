from django.shortcuts import render_to_response
from shortcut.models import Shortcut
from django.contrib.auth.models import User
from django.http import HttpResponse


def get_user(uid):
    user = None
    try:
        user = User.objects.get(id=uid)
        return user
    except Exception as e:
        print e
        return None


def shortcut_list(request):
    name = request.session.get('username')
    shortcut_lists = Shortcut.objects.filter(user__username=name)
    return render_to_response('shortcut/shortcut_list.html', locals())


def shortcut_add_edit(request):
    uid = request.GET.get('uid')
    name = request.GET.get('name')
    website = request.GET.get('website')
    show = request.GET.get('show')
    comment = request.GET.get('comment')

    if get_user(uid):
        # update
        shortcut = Shortcut.objects.get(user=uid)
        shortcut.user = uid
        shortcut.name = name
        shortcut.website = website
        shortcut.show = show
        shortcut.comment = comment
        shortcut.save()

        # return HttpResponse(util.make_msg('suc'))
    else:
        pass


def shortcut_del(request):
    pass
