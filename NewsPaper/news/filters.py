from django_filters import FilterSet, DateTimeFilter
from django.forms import DateTimeInput
from .models import Post

# Создаем свой набор фильтров для модели Post.
# FilterSet, который мы наследуем,

class PostFilter(FilterSet):

    added_after = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

    class Meta:

       model = Post
       fields = {
           'title': ['icontains'],
           'categoryType': ['icontains'],
       }