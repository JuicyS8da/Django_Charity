from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from home.models import Information

import stripe

def donate_view(request):
    context = {
        'info': Information.objects.first(),
    }
    if request.method == 'POST':
        stripe.api_key = settings.STRIPE_PRIVATE_KEY
        # amount should be in cents. Stripe use amount in the smallest currency.
        try:
            amount = int(request.POST.get('amount')) * 100
        except:
            amount = int(request.POST.get('flexRadioDefault')) * 100
        mode = request.POST.get('DonationFrequency')

        checkout = stripe.checkout.Session.create(
            line_items = [{
                'quantity': 1,
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Donation',
                    },
                    'unit_amount': amount
                }
            }],
            mode = mode,
            success_url = request.build_absolute_uri(reverse('success')),
            cancel_url 	= request.build_absolute_uri(reverse('cancel'))
        )
        return redirect(checkout.url, code=303)

    return render(request, 'donate.html', context=context)


def success_view(request):
    context = {
        'info': Information.objects.first(),
        'status': 'Thank you for your donation!'
    }
    return render(request, 'donate.html', context=context)

def cancel_view(request):
    context = {
        'info': Information.objects.first(),
        'status': 'Sorry, your payment has been cancelled.'
    }
    return render(request, 'donate.html', context=context)