from hashlib import new

from django import forms
from django_filters import FilterSet, DateTimeFilter, ModelChoiceFilter, CharFilter
from django.forms import DateTimeInput
from django.core.exceptions import ValidationError
from .models import Post, Category


class PostForm(forms.ModelForm):
    text = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = [
            'author',
            'postCategory',
            'title',
            'text',
            'categoryType',
        ]

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        text = cleaned_data.get("text")

        if title == text:
            raise ValidationError(
                "Заголовок не должен быть идентичным тексту."
            )

        return cleaned_data


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
    category = ModelChoiceFilter(
        field_name='postCategory',
        queryset=Category.objects.all(),
        label='Категория публикации',
        empty_label='Любая')

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
                   'author': forms.Select(),

                   }
