def calculate_overtime():
    scrap_sold = float(input("\nQuota fulfilled: "))
    profit_quota = float(input("Profit quota: "))
    days_until_deadline = int(input("Days until deadline: "))

    overtime_score = (scrap_sold - profit_quota) / 5 + 15 * days_until_deadline
    print(f"\n🕒 Overtime score: {overtime_score:.2f}")


def target_planner():
    try:
        target = float(input("\nWhat is your target (credits)? "))
        already_collected = float(input("How much loot have you already collected? "))
        days_left = int(input("How many days left in overtime? "))
        players = int(input("How many players? "))

        remaining = target - already_collected
        per_day = remaining / days_left
        per_day_per_player = per_day / players

        print("\n🎯 Target Planner")
        print(f"Total target: {target:.2f} credits")
        print(f"Already collected: {already_collected:.2f} credits")
        print(f"Days left: {days_left}")
        print(f"Players: {players}")
        print(f"\n💰 Needed per day: {per_day:.2f} credits")
        print(f"👤 Per person per day: {per_day_per_player:.2f} credits")

    except ZeroDivisionError:
        print("⚠️ Error: Days left and players must be greater than 0.")
    except ValueError:
        print("⚠️ Error: Invalid input. Please enter numbers.")


def show_menu():
    while True:
        print("\n==== Lethal Company Overtime Calculator ====")
        print("1. Calculate Overtime")
        print("2. Use Target Planner")
        print("3. Do Both")
        print("4. Exit")

        choice = input("\nChoose an option (1-4): ")

        if choice == "1":
            calculate_overtime()
        elif choice == "2":
            target_planner()
        elif choice == "3":
            calculate_overtime()
            target_planner()
        elif choice == "4":
            print("Good luck out there, employee 👋")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, 3 or 4.")


# Run the menu
if __name__ == "__main__":
    show_menu()
