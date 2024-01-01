import requests
import multiprocessing

def downloadfile(URL, name):
    request = requests.get(URL)
    open(f"files/file{name}.jpg", "wb").write(request.content)
    print("Finished Download")

URL = "https://picsum.photos/2000/3000"

if __name__ == "__main__":
    for i in range(10):
        print("Starting Download")
        # downloadfile(URL, i)
        p = multiprocessing.Process(target=downloadfile, args=[URL, i])
        p.start()
