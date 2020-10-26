# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    assert inc(4) == 5


if __name__ == "__main__":
    print("The Lannisters send their regards")
    print("And Starks didn't like their regards, so there will be a rebellion :)")
