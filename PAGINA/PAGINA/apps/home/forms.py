from django import forms

class ContactForm(forms.Form):
	Texto	 = forms.CharField(widget=forms.Textarea()) 


class ContactForm2(forms.Form):
	FECHA1	 = forms.DateField(widget=forms.Textarea()) 
	FECHA2	 = forms.DateField(widget=forms.Textarea()) 