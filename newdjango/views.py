from django.shortcuts import redirect, render
from .models import Member
from django.db.models import Q  # Import Q for complex queries


def index(request):
    query = request.GET.get('q', '')  # Get the search query from the URL parameter 'q'

    if query:
        mem = Member.objects.filter(
            Q(email__icontains=query) |  # Case-insensitive search for email
            Q(firstname__icontains=query) |  # Case-insensitive search for first name
            Q(lastname__icontains=query) |  # Case-insensitive search for last name
            Q(id__icontains=query) | # Case-insensitive search for id
            Q(age__icontains=query) | # Case-insensitive search for age
            Q(function__icontains=query)  # Case-insensitive search for function

        )
    else:
        mem = Member.objects.all()

    return render(request, 'index.html', {'mem': mem, 'query': query})

def add(request):
    return render(request,'add.html')

def home(request):
    return render(request, 'index.html')

def addrec(request):
    # Lấy thông tin từ dữ liệu POST gửi từ biểu mẫu thêm thành viên
    x=request.POST['first']
    y=request.POST['last']
    e=request.POST['email']
    a=request.POST['age']
    f=request.POST['function']
    # Tạo đối tượng `Member` mới với thông tin này và lưu vào cơ sở dữ liệu
    mem=Member(firstname=x,lastname=y,email=e,age=a,function=f)
    mem.save()
    return redirect("/")

def delete(request,id):
    mem=Member.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(request,id):
    mem=Member.objects.get(id=id)
    return render(request,'update.html',{'mem':mem})

def uprec(request,id):
    x=request.POST['first']
    y=request.POST['last']
    e = request.POST['email']
    a = request.POST['age']
    f = request.POST['function']
    mem=Member.objects.get(id=id)
    mem.firstname=x
    mem.lastname=y
    mem.email=e
    mem.age=a
    mem.function=f
    mem.save()
    return redirect("/")