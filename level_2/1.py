s1 = "Python is easy to learn!"
s2 = "Python is object-oriented!"
s3 = "Python is platform-independent!"

def phrase(*text):
    i = 0
    while i < 4:
        print(text)
        i = i + 1

phrase(s1)
phrase(s2)
phrase(s3)
