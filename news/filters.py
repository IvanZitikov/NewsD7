from django import forms
from django_filters import FilterSet, DateTimeFilter, ModelChoiceFilter, CharFilter
from django.forms import DateTimeInput
from .models import Post, Category


class NewsFilter(FilterSet):
    title = CharFilter(
        lookup_expr='icontains',
        field_name='title',
        label='Заголовок',
    )

    date = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        label='Найти после указанной даты',
        widget=DateTimeInput(
            attrs={'type': 'date'},
        ),
    )

    class Meta:
        model = Post
        fields = ['categoryType']


class NewsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title',
                  'text',
                  'categoryType',
                  'author',
                  ]
        widgets = {'title': forms.TextInput(),
                   'text': forms.Textarea(),
                   'postCategory': forms.Select(),
                   'author': forms.Select()
                   }
