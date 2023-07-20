from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.core.mail import send_mail 
from django.core.validators import EmailValidator 
from django.views import View
from .models import *
from .forms import *
from django.http import HttpResponse
from django.contrib import messages


class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    # override get context date method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # first, call super get context data
        context['about'] = About.objects.first()
        context['services'] = Service.objects.all()
        context['works'] = RecentWork.objects.all()
        #context['contact'] = Contact.objects.all()
        return context


class AboutCreateView(CreateView):
    model = About
    fields = ['short_description', 'description', 'image', 'cv']
    template_name = 'about_form.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def contact_view(request):
        
        if request.method == 'POST':
            form = ContactForm(request.POST)
            
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            
            # Perform any necessary actions with the form data
            # For example, you can save the data to the database or send an email
            send_mail(
                'Contact Form Submission from {}'.format(name),
                message,
                'form-response@example.com',
                ['landoulsi.emir@gmail.com'],
                fail_silently=False,
            )

            return HttpResponse('Votre message a été envoyé avec succès.')  # Render a success page or redirect as desired

        return render(request, 'home.html')  # Render the contact form template


# class ContactView(View):
#     def get(self, request):
#         form = ContactForm()
#         return render(request, 'home.html', {'form': form})

#     def post(self, request):
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']

#             # Envoi de l'e-mail
#             email_message = EmailMessage(
#                 'Contact Form Submission from {}'.format(name),
#                 message,
#                 'form-response@example.com', # Votre adresse e-mail
#                 ['landulsi.emir@gmail.com'], # Adresse e-mail de l'administrateur
#                 reply_to=[email]
#             )
#             email_message.send()

#             messages.success(request, 'Your message has been sent successfully.')
#             return redirect('contact')

#         return render(request, 'contact.html', {'form': form})