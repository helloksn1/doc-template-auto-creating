from .models import PlaceHolder, PHChaptor0, PHChaptor1, PHChaptor2
from django.forms import ModelForm


class PlaceHolderForm(ModelForm):
    class Meta:
        model = PlaceHolder
        # exclude = ('user',)
        fields = ('filename',)

class PH0Form(ModelForm):
    class Meta:
        model = PHChaptor0
        fields = ('__all__')

class PH1Form(ModelForm):
    class Meta:
        model = PHChaptor1
        fields = ('__all__')

class PH2Form(ModelForm):
    class Meta:
        model = PHChaptor2
        fields = ('__all__')
