from .base import *


SECRET_KEY = env('DJANGO_SECRET_KEY', default='#&e7bs(7ey537&tosnyh\
1&%v9q&q8f**1l7b#4()$orx9w1inx')

DEBUG = env.bool('DJANGO_DEBUG', default=True)
