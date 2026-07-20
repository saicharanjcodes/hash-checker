import hashlib

def hash_cal(option):

    if option == 1:

        cal_file_path_sha = input("Enter file path: ")

        with open(cal_file_path_sha, "rb") as cal_file:
            cal_hash_sha = hashlib.file_digest(cal_file, "sha256").hexdigest()

        print("")
        print("Your sha256 hash is:")
        print("")
        print(cal_hash_sha)
        print("")

    elif option == 2:
        cal_file_path_md = input("Enter file path: ")

        with open(cal_file_path_md, "rb") as cal_file_md:
            cal_hash_md = hashlib.file_digest(cal_file_md, "md5").hexdigest()

        print("")
        print("Your MD5 hash is:")
        print("")
        print(cal_hash_md)
        print("")

    else:
        print("Invalid option")
        return


def hash_verify(option2):

    if option2 == 1:

        cal_file_path_sha = input("Enter file path: ")

        with open(cal_file_path_sha, "rb") as cal_file:
            cal_hash_sha = hashlib.file_digest(cal_file, "sha256").hexdigest()

        print("")
        user_hash_sha = input("Enter hash: ")
        print("")
        print(f"calculated hash is: {cal_hash_sha}")
        print("")

        if user_hash_sha == cal_hash_sha:
            print("Hashes match")
            print("")
        else:
            print("hashes dont match")
            print("")

    elif option2 == 2:
        cal_file_path_md = input("Enter file path: ")

        with open(cal_file_path_md, "rb") as cal_file_md:
            cal_hash_md = hashlib.file_digest(cal_file_md, "md5").hexdigest()

        print("")
        user_hash_md = input("Enter hash: ")
        print("")
        print(f"calculated hash is: {cal_hash_md}")

        if user_hash_md == cal_hash_md:
            print("Hashes match")
            print("")
        else:
            print("hashes dont match")
            print("")

    else:
        print("Invalid option")
        return


print("Hash check and veryfiy")
print("------------------------------------------------------------------")
print("")

while True:
    print("1.Calculate hash")
    print("2.Verify hash")
    print("3.exit")

    choice = int(input("Enter your choice(1,2 or 3): "))

    if choice == 1:
        print("Choose algorithm")
        print("1.sha256")
        print("2.md5")
        print("")

        subchoice1 = int(input("Enter you choice(1 or 2):"))
        hash_cal(subchoice1)

    elif choice == 2:
        print("Choose algorithm")
        print("1.sha256")
        print("2.md5")
        print("")

        subchoice2 = int(input("Enter you choice(1 or 2):"))
        hash_verify(subchoice2)

    else:
        print("Invalid option")