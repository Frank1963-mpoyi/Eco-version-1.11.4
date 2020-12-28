from django import forms


class ContactForm(forms.Form):
    # search customize widget instances, will give the good layout in the front end
    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder": " Full name"
                }
            )
        )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder": " Your Email"
                }
            )
    )
    
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class":"form-control",
                "placeholder": "Your Content"
            }
            )
        )
    
    #field validation
    def clean_email(self): #email, content or any field above
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")
        return email
    
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)# to hide password
        