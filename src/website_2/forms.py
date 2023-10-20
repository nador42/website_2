from django import forms
from django.http import HttpResponse
from blog.models import BlogPost
JOBS = (
    ("python", "devellopeur python"),
    ("javascript", "devellopeur javascript"),
    ("csharp", "devellopeur csharp"),
)


class SignUpForm(forms.Form):
    pseudo = forms.CharField(max_length=8, required=False)
    email = forms.EmailField()
    password = forms.CharField(min_length=6, widget=forms.PasswordInput())
    job = forms.ChoiceField(choices=JOBS, widget=forms.RadioSelect())
    cgu_accept = forms.BooleanField(initial=True)

    def clean_pseudo(self):
        pseudo = self.cleaned_data.get("pseudo")
        if '$' in pseudo:
            # print("probleme avec symbole dollard")
            raise forms.ValidationError("symbole incompatible")
        return pseudo
class BlogPostForm(forms.ModelForm):
    class Meta:
        model=BlogPost
        fields=[
            "title",
            "date",
            "author",
            "category",
            "description",
        ]

        widgets={"date":forms.SelectDateWidget(years=range(1998,2025))}
