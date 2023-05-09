from django.test import TestCase
class NewsFilter(FilterSet):

    news_title = CharFilter(
        field_name='title',
        lookup_expr='icontias',
        label='Заголовок',)

    news_date=DateTimeFilter(
        field_name='dateCreation',
        lookup_expr ='lt',
        label='позже указываемой даты',
        widget=DateInput(format='%dT%H:%M-%m-%Y',
        attrs={'type': 'datetime-local'},),

    )
    news_text = CharFilter(
        field_name='text',
        lookup_expr='icontias',
        label='Текст',
    )

    class Meta:
        model = Post
        fields = ['categoryType']
        label = 'Текст'

# Create your tests here.
