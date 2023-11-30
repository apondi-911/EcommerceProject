from django.http import HttpResponse

def handle_mpesa_callback(request):
    # Your callback logic here
    return HttpResponse("M-Pesa Callback received.")
