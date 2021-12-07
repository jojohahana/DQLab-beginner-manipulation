# Membaca hello.txt dengan fungsi read()
print(">>Membaca berkas file hello.txt dengan fungsi read()")
file =open("hello.txt", "r")
content=file.read()
file.close()
print(content)

# Membaca hello.txt dengan fungsi readlines()
print(">>Membaca berkas file hello.txt dengan fungsi readlines()")
file = open("hello.txt", "r")
first_line = file.readlines()
second_line = file.readlines()
file.close()
print("first_line")
print("second_line")

# Membaca hello.txt dengan menerapkan looping
print((">>Membaca berkas file hello.txct dengan menerapkan looping"))
file = open("hello.txt", "r")
for line in file:
    print(line)
file.close()
