from django.forms import *
from back.models import City, Hotel

# Form for City Model
class CityForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['code'].widget.attrs['autofocus'] = True

    class Meta:
        model = City
        fields = '__all__'  # Add all fields
        widgets = {
            'code': TextInput(
                attrs={
                    'placeholder': 'Enter City Code'
                }
            ),
            'name': TextInput(
                attrs={
                    'placeholder': 'Enter City Name',
                    'row': 3,
                    'cols': 3
                }
            )
        }

# Form for Hotel Model
class HotelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['hotel_name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Hotel
        fields = '__all__'  # Add all fields
        widgets = {
            'code': Select(   # TODO: Add Select lib
                attrs={
                    'class': 'select2',
                    'style': 'width:100%'
                }
            ),
            'hotel_code':  TextInput(
                attrs={
                    'placeholder': 'Enter a Hotel Code'
                }
            ),
            'name': TextInput(
                attrs={
                    'placeholder': 'Enter a Hotel'
                }
            )
        }
