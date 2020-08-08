from django import forms

class EmailSendForm(forms.Form):
    name=forms.CharField(
        label='Name',widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Name'
            }
        )
    )
    email=forms.EmailField(
        label='Email', widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }
        )
    )
    to=forms.EmailField(
        label='To', widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'To'
            }
        )
    )
    comments=forms.CharField(required=False,
                             label='Comments',widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Comments Here'
            }
        )
    )




from .models import Comments
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=('name','email','body')