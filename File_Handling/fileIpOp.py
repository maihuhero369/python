with open("demo.txt", "r") as f:
    data = f.read()
    newData = data.replace("python", "java")
    print(newData)
    with open("demo.txt", "w") as f:
        f.write(newData)