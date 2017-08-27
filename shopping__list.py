shopping_list = []
def START():
    print "do you want to quit??"
    print "if yes then print DONE!!"

print "you can use commands like DONE, HELP, SHOW"
#DONE for exit from the cart
#SHOW for visit the cart
#HELP for helping the commands
def SHOW():
    for i in shopping_list:
        print i

def HELP():
    print "print SHOW for visiting your cart"
    print "print DONE for exit from the shopping"

while True:
    new_item = input("> ")

    if new_item == 'DONE':
        break
    if new_item == 'SHOW':
        SHOW()
        continue
    if new_item == 'HELP':
        HELP()
        continue
    shopping_list.append(new_item)

print "here is your list"

for i in shopping_list:
    print i



