def hello(name, last_name=" Happy"):
    print("Hello world")
    print(f"Welcome {name}  {last_name}")


hello("Cruz", "Ibarra")
hello("Cruz")

# Named arguments
hello(last_name="Ibarra", name="Cruz")
