from django.db import models
from django.conf import settings


class Counter(models.Model):
    class Meta:
        verbose_name = 'счетчик'
        verbose_name_plural = 'счетчики'

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             verbose_name='пользователь')
    count = models.IntegerField(null=False,
                                verbose_name='счетчик',
                                default=0)

    def increment(self):
        self.count += 1
        self.save()

    def decrement(self):
        self.count = self.count - 1 if self.count > 0 else 0
        self.save()



