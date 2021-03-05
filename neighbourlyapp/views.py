from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User, Tool

###################################################
##Login/Registration##
# Create your views here.
#############Display Paths########


def displayhome(request):
    if 'UserID' in request.session:
        return redirect('/dashboard')
    return render(request, 'displayhome.html')


def displaydashboard(request):
    if 'UserID'not in request.session:
        return redirect('/')
    cu = User.objects.get(id=request.session['UserID'])
    # alljobs=Job.objects.all()

    context = {
        'cu': cu,
        'all_tools': Tool.objects.all(),
        'thisUser': User.objects.get(id=request.session['UserID']),
        # 'allusers': User.objects.all().values(),
    }
    return render(request, 'dashboard.html', context)

    #############Action Paths########


def register(request):
    errors = User.objects.registration_validator(request.POST)  # postData??
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    pw_hash = bcrypt.hashpw(
        request.POST['formpassword'].encode(), bcrypt.gensalt()).decode()
    newUser = User.objects.create(
        first_name=request.POST['formfname'],
        last_name=request.POST['formlname'],
        email=request.POST['formemail'],
        password=pw_hash
    )
    request.session['UserID'] = newUser.id
    return redirect('/dashboard')


def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    user = User.objects.filter(email=request.POST['formemail'])
    logged_user = user[0]
    if bcrypt.checkpw(request.POST['formpassword'].encode(), logged_user.password.encode()):
        request.session['UserID'] = logged_user.id
        return redirect('/dashboard')
    else:
        messages.error(request, 'Invalid logon')
        return redirect('/')


def logout(request):
    request.session.clear()
    return redirect('/')
#############################################################################


def newtool(request):
    # if 'UserID'not in request.session:
    #     return redirect('/')
    context = {
        'thisUser': User.objects.get(id=request.session['UserID'])
    }
    return render(request, 'newtool.html', context)


def submittool(request):
    errors = Tool.objects.tool_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/new')
    newTool = Tool.objects.create(item_name=request.POST['formitem_name'],
        description=request.POST['formtitle'],
        location=request.POST['formlocation'],
        start_date=request.POST['formstart_date'],
        end_date=request.POST['formend_date'],
        user=User.objects.get(id=request.session['UserID'])
        )
    return redirect('/dashboard')


def searchtools(request):
    if 'UserID'not in request.session:
        return redirect('/')
    lookForTool = Tool.objects.all(item_name=request.POST['formitem_name'],
    description=request.POST['formtitle'],
    location=request.POST['formlocation'],
    start_date=request.POST['formstart_date'],
    end_date=request.POST['formend_date'],
    user=User.objects.get(id=request.session['UserID'])
    )
    return redirect('/dashboard')


def displayedittool(request):
    if 'UserID'not in request.session:
        return redirect('/')
    context = {
        'thisUser': User.objects.get(id=request.session['UserID']),
        'thistool':Tool.objects.get(id=id)
    }
    return render(request, 'thistool.html', context)


def revisedtool(request):
    if 'UserID'not in request.session:
        return redirect('/')
    return redirect('/show')

# def searchtools(request):
#     if 'UserID'not in request.session:
#         return redirect('/')
#     return render(request, 'thistool.html')


def showalltools(request):
    if 'UserID'not in request.session:
        return redirect('/')
    context={
        'all_tools': Tool.objects.all(),
        'user':User.objects.get(id=request.session['userID']),
        'all_users': User.objects.all().values()
    }
    return render(request, 'alltools.html', context)


def thistool(request):
    # if 'UserID'not in request.session:
    #     return redirect('/')
    context = {
        'thistool': Tool.objects.get(id=id),
        'thisUser': User.objects.get(id=request.session['userID'])
    }
    return render(request, 'thistool.html', context)


def acceptedtools(request):
    if 'UserID'not in request.session:
        return redirect('/')
    return render(request, 'acceptedtool.html')


def deletethistool(request, tool_id):
    if 'UserID'not in request.session:
        return redirect('/')
    remove_tool = Tool.objects.get(id=tool_id)
    remove_tool.delete()
    return redirect('/show')