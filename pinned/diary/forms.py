from django.forms import ModelForm
from .models import Entry


class Entryform(ModelForm):
    class Meta:
        model = Entry
        fields = {'text'}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['text'].widget.attrs.update({'style': 'width: 100%', 'textarea class': 'form-control',
                'cols' : '100', 'rows' : '100', 'placeholder' : 'Write down here...', 'id' : 'floatingTextarea'})
