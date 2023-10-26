chance_of_obtain = 0.016
rolls = 120

chance_of_not_obtain = 1 - chance_of_obtain

chance_of_never = chance_of_not_obtain ** rolls

print(chance_of_never)