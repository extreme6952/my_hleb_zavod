from django import forms 
from .models import *


class UpdateProductInformationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_category','name',
                  'image','text',
                  'price','protein',
                  'fats','carbohydrates']
        
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['product_category'].widget.attrs.update(
            {
                'placeholder':'Выберите категорию вашего продукта',
            }
        )
        self.fields['product_category'].label = 'Категории'

        self.fields['name'].widget.attrs.update(
            {
                'placeholder':'Введите название вашего товара!',
            }
        )

        self.fields['name'].label = 'Имя товара'

        self.fields['image'].widget.attrs.update(
            {
                'placeholder':'Прикрепите фото к товару!',
            }
        )

        self.fields['image'].label = 'Фото товара'

        self.fields['text'].widget.attrs.update(
            {
                'placeholder':'Добавьте описание товара\n(данное поле не является обязательным.)',
            
            }
        )

        self.fields['text'].label = 'Описание товара'

        self.fields['price'].widget.attrs.update(
            {
                'placeholder':'Введите цену товара'
            }
        )
        self.fields['price'].label = 'Цена'

        self.fields['protein'].widget.attrs.update(
            {
                'placeholder':'Введите количество белков в граммах',
          }
        )

        self.fields['protein'].label = 'Белки'

        self.fields['fats'].widget.attrs.update(
            {
                'placeholder':'Введите количество жиров в продукте'
            }
        )

        self.fields['fats'].label = 'Жиры'
  
        self.fields['carbohydrates'].widget.attrs.update(
            {
                'placeholder':'Введите количество углеводов',
            }
        )

        self.fields['carbohydrates'].label = 'Углеводы'


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_category','name',
                  'image','text','price',
                  'protein','carbohydrates','fats']