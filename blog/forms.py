from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('date',)

class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label="Votre adresse e-mail")
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        sujet = cleaned_data.get('sujet')
        message = cleaned_data.get('message')

        if sujet and message:  # Est-ce que sujet et message sont valides ?
            if "pizza" in sujet and "pizza" in message:
                self.add_error("message", 
                    "Vous parlez déjà de pizzas dans le sujet, "
                    "n'en parlez plus dans le message !"
                )

        return cleaned_data  # N'oublions pas de renvoyer les données si tout est OK

    # def clean_message(self):
    #     message = self.cleaned_data['message']
    #     if "pizza" in message:
    #         raise forms.ValidationError("On ne veut pas entendre parler de pizza !")

    #     return message  # Ne pas oublier de renvoyer le contenu du champ traité

    