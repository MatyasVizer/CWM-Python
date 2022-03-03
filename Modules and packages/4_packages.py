# subdirectory organization is important
# add __init__.py to directory

from ecommerce.sales import calc_shipping, calc_tax  # 1

from ecommerce import sales  # 2

import ecommerce.sales  # 3

ecommerce.sales.calc_shipping()

calc_tax()
calc_shipping()
