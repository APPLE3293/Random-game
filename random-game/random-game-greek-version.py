import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Καλώς ήλθατε στο παιχνίδι μαντείας αριθμών！")
    print("Σκέφτητε έναν αριθμό μεταξύ 1 και 100.")

    while True:
        try:
            guess = int(input("Παρακαλώ εισάγετε την εικασία σας: "))
            attempts += 1

            if guess < number_to_guess:
                print("Πολύ χαμηλή, δοκιμάστε ξανά.")
            elif guess > number_to_guess:
                print("Πολύ ψηλά, δοκιμάστε ξανά.")
            else:
                print(f"Συγχαρητήρια! Μαντέψατε σωστά τον αριθμό σε {attempts} προσπάθειες.")
                break
        except ValueError:
            print("Εισαγάγετε έναν έγκυρο ακέραιο αριθμό.")

if __name__ == "__main__":
    guess_the_number()
