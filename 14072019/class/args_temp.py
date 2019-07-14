def test(*args, **kwargs):
    print("Args", args)
    print("Kwargs",kwargs)


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    b = {"MH": "A", "WE": "B"}
    test(*a, **b)