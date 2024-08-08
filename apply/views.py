from django.http import HttpResponse
from django.shortcuts import render

def apply (request):
    data = {}
    if request.method == 'POST':
        na = request.POST.get('name')
        fna = request.POST.get('fname')
        cnic = request.POST.get('cnic')
        dob = request.POST.get('dob')
        blood = request.POST.get('blood')
        gender = request.POST.get('gender')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        age = request.POST.get('age')
        taddress = request.POST.get('taddress')
        paddress = request.POST.get('paddress')
        iomarks = request.POST.get('iomarks')
        itmarks = request.POST.get('itmarks')
        iper = request.POST.get('iper')
        momarks = request.POST.get('momarks')
        mtmarks = request.POST.get('mtmarks')
        mper = request.POST.get('mper')
        data ={
            'name': na,
            'fname': fna,
            'cnic':cnic,
            'dob':dob,
            'blood' : blood,
            'gender' : gender,
            'contact' : contact,
            'email' : email,
            'age' : age,
            'taddress' : taddress,
            'paddress' : paddress,
            'iomarks' : iomarks,
            'itmarks' : itmarks,
            'iper' : iper,
            'momarks' : momarks,
            'mtmarks' : mtmarks,
            'mper' : mper,
        }
    if 'button' in request.POST:
        return render(request, 'application.html', data)
    return render(request, 'apply.html', data)
