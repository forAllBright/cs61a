from utils import *

square = lambda x: x * x
is_odd = lambda x: x % 2 == 1
re = map_and_filter([1, 2, 3, 4, 5], square, is_odd)
print(re)
rs = map_and_filter(['hi', 'hello', 'hey', 'world'],lambda x: x[4], lambda x: len(x) > 4)
print(rs)
rs2 = key_of_min_value({1: 6, 2: 5, 3: 4})
print(rs2)



from abstractions import *
import abstractions
soda_reviews = [make_review('Soda', 4.5),
                make_review('Soda', 4)]
soda = make_restaurant('Soda', [127.0, 0.1],
                       ['Restaurants', 'Breakfast & Brunch'],
                       1, soda_reviews)

print(restaurant_ratings(soda))


