from django.contrib.auth.models import User
from django_unicorn.components import UnicornView,QuerySetType
from .models import BoughtItem


class ShopmacramesView(UnicornView):
    user_products: QuerySetType[BoughtItem] = None
    user_pk: int

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs) # required
        self.user_pk = kwargs.get('user')
        self.user_products = BoughtItem.objects.filter(user=self.user_pk)