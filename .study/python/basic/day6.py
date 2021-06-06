# import day6_module
#
# day6_module.price(3)            # 일반 3명 가격
# day6_module.price_morning(4)    # 조조 4명 가격
# day6_module.price_soldier(5)    # 군인 5명 가격
#
# import day6_module as dm        # 별명 dm
# dm.price(3)
# dm.price_morning(4)
# dm.price_soldier(5)
#
# from day6_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from day6_module import price, price_morning
# price(3)
# price_morning(4)
# # price_soldier(5)

from day6_module import price_soldier as price
price(5)