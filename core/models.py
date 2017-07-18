from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CartItemManager(models.Manager):

    def add_item(self, cart_key, product):
        pass



class CartItem(models.Model):

    cart_key = models.CharField(
        'Chave do Carrinho', max_length=40, db_index=True
        )
    product = models.ForeignKey('catalog.Product', verbose_name='Produto')
    quantity = models.PositiveIntegerField('Quantidade', default=1)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    objects = CartItemManager()

    class Meta:
        verbose_name = 'Item do Carrinho'
        verbose_name_plural = 'Itens do Carrinho'
        # para tornar um produto único por cada carrinho
        unique_together = (('cart_key', 'product'))

        def __str__(self):
            return '{} [{}]'.format(self.product, self.quantity)
