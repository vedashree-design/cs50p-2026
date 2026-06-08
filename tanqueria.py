def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total = 0
    while True:
        try:
            item = input("Item: ").title()
            total += menu[item] #Add price to the total
            print(f"Total: ${total:.2f}") #Print formatted total
            # 1. Look up item in menu
            # 2. Add price to total
            # 3. Print total formatted as $0.00
        except EOFError:
            # 4. Ctrl+D was pressed, print newline and break
            print()
            break
        except KeyError:
            # 5. Item not in menu, ignore and re-prompt
            pass

main()

    except KeyError:
         if item.lower() == "done":
            print()
            break
    pass
