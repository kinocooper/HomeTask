import requests

def main():
    response = requests.get("https://api.github.com")
    print(response.status_code)

    def sample_func(x, y):
        return x + y
    print(sample_func(10, 20))

if __name__ == "__main__":
    main()

