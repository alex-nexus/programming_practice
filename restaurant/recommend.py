import csv
import argparse

class Restaurant:
	def __init__(self, restaurant_id):
		self.id = restaurant_id
		self.dishes = []
		self.deals = []
		
	def add_dish(self, dish):
		self.dishes.append(dish)

	def add_deal(self, deal):
		self.deals.append(deal)

	def get_all_dishes(self):
		return set(self.dishes + self.get_deal_dishes())
		
	def get_deal_dishes(self):
		return set(sum([deal.dishes for deal in self.deals], []))
		
	def has_dishes(self, dish_names):
		return len(set([d.dish_name for d in self.get_all_dishes()]) & set(dish_names)) == len(dish_names)
		
	def total_price(self, dish_names):
		deal_dish_names = set(self.get_deal_dishe_names(dish_names))
		non_deal_dish_names = set(dish_names) -deal_dish_names
		print 'deal_dish_names', deal_dish_names
		print 'non_deal_dish_names', non_deal_dish_names
		return self.total_deal_price(deal_dish_names) + self.total_non_deal_price(non_deal_dish_names)

	def get_deal_dishe_names(self, dish_names):
		return set([d.dish_name for d in self.get_deal_dishes()]) & set(dish_names)
		
	def total_deal_price(self, deal_dish_names):
		return sum([deal.price for deal in self.deals for dish_name in deal_dish_names if ])

	def total_non_deal_price(self, non_deal_dish_names):
		non_deal_dishe_names = set(dish_names) - set(self.deal_dishe_names)
		non_deal_dishe_names.intersection_update(set(dish_names))
		return sum([dish.price for dish in self.dishes if dish.dish_name in non_deal_dishe_names])
	
class Dish:
	def __init__(self, restaurant_id, price, dish_name):
		self.restaurant_id = restaurant_id
		self.price = float(price)
		self.dish_name = dish_name
	
class Deal:
	def __init__(self, restaurant_id, price):
		self.restaurant_id = restaurant_id
		self.price = float(price)
		self.dishes = []

	def add_dish(self, dish):
		self.dishes.append(dish)

	def dish_names(self):
		return [(dish.dish_name,dish.price) for dish in self.dishes]
	
def load_data(filename):
	f = open(filename, 'r')
	restaurant_dict = {}

	for row in csv.reader(f):
		restaurant_id = row[0]
		if restaurant_id not in restaurant_dict:
			restaurant_dict[restaurant_id] = Restaurant(restaurant_id)				
		price = row[1]
		
		#no deal
		if len(row)==3:
			restaurant_dict[restaurant_id].add_dish(Dish(restaurant_id, price, row[2]))
		else:
			deal = Deal(restaurant_id, price)			
			for dish_name in row[2:]:	
				dish = Dish(restaurant_id, price, dish_name)
				restaurant_dict[restaurant_id].add_dish(dish)				
				deal.add_dish(dish)
			restaurant_dict[restaurant_id].add_deal(deal)
	
	# for rid, r in restaurant_dict.items():
	# 	for d in r.dishes:
	# 		print rid, d.dish_name, d.price
	# 	for d in r.deals:
	# 		print rid, d.dish_names()

	return restaurant_dict

def recommend(filename, dish_names):
	if len(dish_names) ==0:
		return False

	restaurant_dict = load_data(filename)	
	candidates =  filter(lambda r: r.has_dishes(dish_names), restaurant_dict.values())
	if len(candidates) ==0:
		return False
	print 'candidates', candidates
	print len([(c.dishes, c.deals) for c in candidates])
	candidate_to_price = dict([(candidate.id, candidate.total_price(dish_names)) for candidate in candidates])
	print candidate_to_price
	return sorted(candidate_to_price.items(), key=lambda r: r[1])[0]
	
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("filename", help="the file name that contains the file")
	parser.add_argument("dishnames", help="the dish names")
	args = parser.parse_args()
	
	print recommend(args.filename, args.dishnames.split(' '))
	# print recommend(args.filename, ['burger', 'tofu_log'])
	# print recommend(args.filename, ['salad', 'wine'])
	# print recommend(args.filename, ['water', 'fajita'])
	# print recommend(args.filename, ['fajita','popper', 'salsa', 'water'])
	#print recommend(args.filename, ['applepie'])
	#Expected: 4, 23.00
