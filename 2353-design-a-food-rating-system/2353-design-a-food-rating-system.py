#brute force

# class FoodRatings:

#     def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        
#         self.food_rating = { f:r for f,r in zip(foods,ratings)}

#         self.cuisines_food = defaultdict(list)
#         for c,f in zip(cuisines,foods):
#             self.cuisines_food[c].append(f)

#     def changeRating(self, food: str, newRating: int) -> None:
        
#         self.food_rating[food] =  newRating
        
#     def highestRated(self, cuisine: str) -> str:
        
#         ans =  []
#         max_rating = -1
#         for food in self.cuisines_food[cuisine] :
            
#             curr_rating = self.food_rating[food]

#             if curr_rating > max_rating :
#                 ans = [ food ]
#                 max_rating = curr_rating 
#                 continue

#             if  curr_rating == max_rating:
#                 ans.append(food)

#         ans.sort()
#         return ans[0]    

#Time Limit Exceeded
#-------------------------------------------------------------------



from sortedcontainers import SortedSet

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        
        self.cuisines_food = defaultdict(SortedSet) #(rating,food)
        self.food_cuisines = {} #(cuisine,rating)
        for c,f,r in zip(cuisines,foods,ratings):
            self.cuisines_food[c].add((-r,f))
            self.food_cuisines[f] = (c,r)

    def changeRating(self, food: str, newRating: int) -> None:
        
        cuisine = self.food_cuisines[food][0]
        rating = self.food_cuisines[food][1]

        self.cuisines_food[cuisine].remove( (-rating,food)  )

        self.cuisines_food[cuisine].add((-newRating,food) )

        self.food_cuisines[food] = (cuisine ,newRating)


    def highestRated(self, cuisine: str) -> str:

        return self.cuisines_food[cuisine][0][1]
  

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)