numbers = [10, 20, 30, 40]
def generate_numbers():
    print("Starting!")

    yield 10

    print("Resuming")

    yield 20

    print("Finished")

generator = generate_numbers()
print(next(generator))
print(next(generator))

# return - ends function, returns a result, cant resume the function
# yield - pauses function, produces generator value, can resume the function