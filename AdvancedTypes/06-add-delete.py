pets = [
    "Pelusa",
    "Chucho",
    "Solo vino",
    "Chucho"]

# inset element
pets.insert(-1, "Bobby")
# to add element on the last
pets.append("Bobby")
# Type name to delete
pets.remove("Pelusa")
# Remove the last element
pets.pop()
# Remove specific element
pets.pop(1)
# remove element
del pets[0], pets[0]
# Clear list
pets.clear()
print(pets)
