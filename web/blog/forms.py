from django import forms


class ContactMeMessage(forms.Form):
    customer_name = forms.CharField(label='Name', max_length=100)
    customer_email_address = forms.CharField(label='email_address', max_length=200)
    customer_phone_number = forms.CharField(label='phone_number', max_length=20)
    customer_message = forms.CharField(label='message', max_length=5000)
    article_UUID_string = forms.CharField(max_length=200)

