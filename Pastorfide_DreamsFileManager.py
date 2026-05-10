import time
import os

Dreamsfile = "dreams.txt"

# Create file kung wala pa
if not os.path.exists(Dreamsfile):
    with open(Dreamsfile, "w") as file:
        file.write("Dream Big: I want to become a skilled programmer who builds systems that help people.\
                    \nStay Curious: I will keep learning even when things get difficult.\
                    \nEmbrace Failure: Every error is a step closer to success.\
                    \nCreate Impact: I want my code to solve real-world problems.\
                    \nBe Consistent: Small progress every day leads to big results.\
                    \nBelieve in Yourself: I am capable of learning and growing. Someday we will be free.\n\n ")

# Inspiring Messages
def InspiringMessage():
    print("\n\t𝑰𝑵𝑺𝑷𝑰𝑹𝑰𝑵𝑮 𝑴𝑬𝑺𝑺𝑨𝑮𝑬")
    print("\t﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌\n")

    with open(Dreamsfile, "r") as file:
        content = file.read()

        if content.strip() == "":
            print("No inspiring messages found.")
        else:
            print(content)

while True:
    time.sleep(0.1)
    print("\n\t\t=== 𝑫𝑹𝑬𝑨𝑴𝑺 𝑭𝑰𝑳𝑬 𝑴𝑨𝑵𝑨𝑮𝑬𝑹 ===")
    print("1 - Read inspiring messages")
    print("2 - Add a new inspiring message")
    print("3 - Rewrite the entire file")
    print("4 - Exit")

    option = input("\nEnter your choice ---> ")

    # OPTION 1
    if option == '1':
        os.system('cls')
        InspiringMessage()

    # OPTION 2
    elif option == '2':
        os.system('cls')

        add = input("Enter your new inspiring line:\n")

        with open(Dreamsfile, "a") as file:
            file.write(add + "\n")

        print("\nYour inspiration has been added!")

    # OPTION 3
    elif option == '3':
        os.system('cls')

        print("Warning: This will overwrite the file.")
        write = input("Type YES to continue: ").lower()

        if write == 'yes':

            rew = input("\nWrite your new inspiring messages:\n")

            with open(Dreamsfile, "w") as file:
                file.write(rew + "\n")

            print("File has been overwritten.")

        else:
            print("Please Try Again.")

    # OPTION 4 
    elif option == '4':
        os.system('cls')
        print("See yah, Good bye!")
        break

    # INVALID OPTION
    else:
        os.system('cls')
        print("𝑰𝑵𝑽𝑨𝑳𝑰𝑫 𝑶𝑷𝑻𝑰𝑶𝑵, 𝑷𝑳𝑬𝑨𝑺𝑬 𝑻𝑹𝒀 𝑨𝑮𝑨𝑰𝑵!")