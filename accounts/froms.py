from django  import forms
class ContectForm(forms.Form):
    choices=(('Q','Questionx'),('a','Answer'))
    name=forms.CharField()
    email= forms.EmailField()
    category=forms.TypedChoiceField(choices=choices, coerce=int, initial=2 )
    subject = forms.CharField(max_length = 150)
    body= forms.CharField(widget=forms.Textarea)
    
    
    
    
    
    
    

