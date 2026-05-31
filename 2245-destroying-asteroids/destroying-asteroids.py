class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:

        heap_mass = []
        for ast in asteroids:
            heapq.heappush(heap_mass,ast)
            while heap_mass and heap_mass[0] <= mass:
                mass += heapq.heappop(heap_mass)

        return len(heap_mass) == 0     
        