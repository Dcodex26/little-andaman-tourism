from django.shortcuts import render, redirect

from .forms import EnquiryForm


def home(request):
    return render(request, 'andamanweb/home.html')


def butler_bay(request):
    return render(request, 'andamanweb/butler_bay.html')


def kalapathar(request):
    return render(request, 'andamanweb/kalapathar.html')


def dalda_plantation(request):
    return render(request, 'andamanweb/dalda_plantation.html')


def white_surf(request):
    return render(request, 'andamanweb/white_surf.html')


def enquiry(request):

    if request.method == 'POST':
        form = EnquiryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('enquiry_success')

    else:
        form = EnquiryForm()

    return render(
        request,
        'andamanweb/enquiry.html',
        {'form': form}
    )


def enquiry_success(request):
    return render(
        request,
        'andamanweb/enquiry_success.html'
    )