unique_visitors = {"Alice","Shawn","Kavindu","Thasangan"}
unique_visitors_2= {"Kavitha","Perera","Kavindu","Thasangan"}


unique_visitors.add("Shane")
unique_visitors.remove("Alice")

unique_visitors.add("Shawn")

intersection = unique_visitors & unique_visitors_2


union = unique_visitors | unique_visitors_2
print(union)

