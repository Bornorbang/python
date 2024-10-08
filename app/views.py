from django.shortcuts import render, redirect
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from app.models import GeneralInfo, Service, Testimony, Faq, ContactFormLog, Blog, Author

# Create your views here.

def index(request):
    general_info = GeneralInfo.objects.first()
    services = Service.objects.all()
    testimony = Testimony.objects.all()
    faq = Faq.objects.all()
    recent_blog = Blog.objects.all().order_by("-created_at")[:3]
    author = Author.objects.all()

    context = {
        'company_name': general_info.company_name,
        'location': general_info.location,
        'email': general_info.email,
        'phone': general_info.phone,
        'open_hours': general_info.open_hours,
        'video_url': general_info.video_url,
        'twitter_url': general_info.twitter_url,
        'instagram_url': general_info.instagram_url,
        'facebook_url': general_info.facebook_url,
        'linkedin_url': general_info.linkedin_url,

        'services': services,

        'testimony': testimony,

        'faq': faq,

        'recent_blog': recent_blog,

        'author': author,
    }
    
    
    return render(request, "index.html", context)

# def aboutus(request):
#     services = ["Web Development", "App Development", "SEO", "Graphic Design"]
#     products = [
#     {'names': 'Laptop', 'price': 999.99},
#     {'names': 'Smartphones', 'price': 499.99},
#     {'names': 'Headphones', 'price': 99.99},
#     {'names': 'Camera', 'price': 799.99}
#     ]
#     context = {
#         'course_title': "Django Project",
#         'current_date': datetime.now(),
#         'is_prof' : False,
#         'user' : {
#             'name': "Michael Forbes",
#             'email': "mike@gmail.com",
#             'age': 37
#         },
#         'random_text': "You are welcome to our Web App, you!",
#         'product_price': 199.9999,
#         'services': services,
#         'products': products,
#         'price_threshold': 500
#     }
#     return render(request, "aboutus.html", context)

def blog_detail (request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    general_info = GeneralInfo.objects.first()
    recent_blog = Blog.objects.all().exclude(id=blog_id).order_by("-created_at")[:2]

    context = {
        'blog': blog,
        'recent_blog': recent_blog,

        'company_name': general_info.company_name,
        'location': general_info.location,
        'email': general_info.email,
        'phone': general_info.phone,
        'open_hours': general_info.open_hours,
        'video_url': general_info.video_url,
        'twitter_url': general_info.twitter_url,
        'instagram_url': general_info.instagram_url,
        'facebook_url': general_info.facebook_url,
        'linkedin_url': general_info.linkedin_url,
    }
    return render(request, "blog-details.html", context)

def blog(request):
    general_info = GeneralInfo.objects.first()
    all_blog = Blog.objects.all().order_by("-created_at")
    author = Author.objects.all()
    paginator = Paginator(all_blog, 2)

    page = request.GET.get('page')

    try:
        article = paginator.page(page)
    except PageNotAnInteger:
        article = paginator.page(1)
    except EmptyPage:
        article = paginator.page(1)


    context = {
        'company_name': general_info.company_name,
        'location': general_info.location,
        'email': general_info.email,
        'phone': general_info.phone,
        'open_hours': general_info.open_hours,
        'video_url': general_info.video_url,
        'twitter_url': general_info.twitter_url,
        'instagram_url': general_info.instagram_url,
        'facebook_url': general_info.facebook_url,
        'linkedin_url': general_info.linkedin_url,

        'all_blog': article,
        'author': author,
    }

    return render(request, "blog.html", context)


def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message =  request.POST.get("message")

        context = {
            "name": name,
            "email": email,
            "subject": subject,
            "message": message
        }

        html_content = render_to_string('email.html', context)

        is_success = False
        is_error = False 
        error_message = ""

        try:
            send_mail(
                subject=subject,
                message=None,
                html_message = html_content,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
        except Exception as e:
            is_error = True
            error_message = str(e)
            messages.error(request, "Could not send your Email. Please try again later!")
        else:
            is_success = True
            error_message = "Null"
            messages.success(request, "The Email Has Been Sent Successfully")

        
        ContactFormLog.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
            action_time = timezone.now(),
            is_success = is_success,
            is_error = is_error,
            error_message = error_message,
        )


    return redirect('home')