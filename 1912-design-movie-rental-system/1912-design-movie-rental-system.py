# class MovieRentingSystem:

#     def __init__(self, n: int, entries: List[List[int]]):
#         #entries[i] = [shopi, moviei, pricei]
        
#         self.shops      = defaultdict(list)
#         self.movies     = defaultdict(list)
#         self.shop_movie = defaultdict(list)
#         self.rented     = []

#         for shopi, moviei, pricei in entries:
#             heappush(self.shops[shopi], (pricei,moviei))
#             heappush(self.movies[moviei], (pricei,shopi))
#             self.shop_movie[(shopi, moviei)] = pricei
    
#         #self.my_print("begin")

#     def my_print(self,text):
#         print(text)

#         for k,v in self.shops.items():
#             print(f"shop {k} have the movies {v}")
#         print()

#         for k,v in self.movies.items():
#             print(f"movie {k} is on shops {v}")
#         print()
        


#     def get5(self,heap):
#         ans = []
#         cnt = 5
#         while heap and cnt > 0:
#             cnt -= 1
#             ans.append(heappop(heap) )
#         for elem in ans:
#             heappush(heap,elem)
#         return ans



#     def search(self, movie: int) -> List[int]:
#         heap = self.movies[movie]
#         ans = [ shop for price,shop in self.get5(heap)]
        
#         #print(f"search cheapest 5 shops with movie {movie}:",ans)
#         #print()

#         return ans
        

#     def remove_from_heap(self,heap,element):
#         if element in heap:

#             index = heap.index(element)
            
#             heap[index] = heap[-1]
#             heap.pop()  
            
#             # Re-heapify the heap
#             if index < len(heap):
#                 heapq._siftup(heap, index)
#                 heapq._siftdown(heap, 0, index)

#             return heap
        


#     def rent(self, shop: int, movie: int) -> None:
#         price = self.shop_movie[(shop, movie)]

#         heappush(self.rented, (price,shop,movie))
    
#         self.movies[movie] = self.remove_from_heap(self.movies[movie],(price,shop))
#         self.shops[shop] = self.remove_from_heap(self.shops[shop],(price,movie))

#         #self.my_print(f" after rent in shop {shop} movie {movie}")
            

#     def drop(self, shop: int, movie: int) -> None:
        
#         price = self.shop_movie[(shop, movie)]

#         self.remove_from_heap(self.rented , (price,shop,movie))

#         heappush(self.shops[shop], (price,movie))
#         heappush(self.movies[movie], (price,shop))

#         #self.my_print(f" after drop in shop {shop} movie {movie}")
        

#     def report(self) -> List[List[int]]:
#         ans = [ (shop,movie) for  price,shop,movie in self.get5(self.rented) ]
#         #print(f"report cheapest 5 rented movies :",ans)
#         #print()
#         return ans

#Time Limit Exceeded
#--------------------------------------------------------------------------

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.available = {}  # (shop, movie) -> price
        self.movie_shops = {}  # movie -> list of (price, shop)
        self.rented = set()  # (shop, movie) that are currently rented

        for shop, movie, price in entries:
            self.available[(shop, movie)] = price
            if movie not in self.movie_shops:
                self.movie_shops[movie] = []
            self.movie_shops[movie].append((price, shop))

        # Sort shops by price for each movie initially
        for movie in self.movie_shops:
            self.movie_shops[movie].sort()

    def search(self, movie: int) -> List[int]:
        result = []
        for price, shop in self.movie_shops.get(movie, []):
            if (shop, movie) not in self.rented:
                result.append(shop)
            if len(result) == 5:
                break
        return result

    def rent(self, shop: int, movie: int) -> None:
        self.rented.add((shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        self.rented.discard((shop, movie))

    def report(self) -> List[List[int]]:
        rented_list = []
        for shop, movie in self.rented:
            price = self.available[(shop, movie)]
            rented_list.append((price, shop, movie))

        rented_list.sort()
        return [[shop, movie] for price, shop, movie in rented_list[:5]]





# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()