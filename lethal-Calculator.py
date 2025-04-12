from datetime import datetime, timedelta


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
        days_left = int(input("How many days left til deadline? "))
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


def quota_helper():
    try:
        quota = float(input("\n📦 Quota: "))
        days_left = int(input("📅 Days left: "))
        players = int(input("👥 Players (optional, 1 if solo): ") or "1")

        if days_left <= 0 or players <= 0:
            print("⚠️ Error: Days and players must be greater than 0.")
            return

        per_day = quota / days_left
        per_day_per_player = per_day / players

        print("\n📊 Quota Breakdown")
        print(f"Total quota: {quota:.2f}")
        print(f"Days left: {days_left}")
        print(f"Players: {players}")
        print(f"\n💰 Required per day: {per_day:.2f} credits")
        print(f"👤 Per player per day: {per_day_per_player:.2f} credits")

    except ValueError:
        print("⚠️ Error: Invalid input. Please enter numbers.")


def overtime_with_target():
    try:
        scrap_sold = float(input("\n📦 Quota fulfilled: "))
        profit_quota = float(input("🎯 Profit quota: "))
        days_until_deadline = int(input("📅 Days until deadline: "))

        overtime_score = (scrap_sold - profit_quota) / 5 + 15 * days_until_deadline
        overtime_score = max(overtime_score, 0)  # Geen negatieve scores

        bonus_multiplier = 1 + (overtime_score / 100)  # Bv. 10% score = 1.1x
        new_target = profit_quota * bonus_multiplier

        print(f"\n🕒 Overtime score: {overtime_score:.2f}")
        print(f"💹 Bonus multiplier: {bonus_multiplier:.2f}x")
        print(f"🎯 New target (incl. overtime bonus): {new_target:.2f} credits")

    except ValueError:
        print("⚠️ Error: Invalid input. Please enter numbers.")


# 1. Team Efficiency Tracker
def team_efficiency_tracker():
    try:
        total_scrap = float(input("\n🛠️ Total scrap produced: "))
        time_spent = float(input("⏱️ Time spent (in hours): "))

        efficiency = total_scrap / time_spent
        print(f"\n💡 Team efficiency: {efficiency:.2f} scrap per hour")

        if efficiency > 10:
            print("🚀 Excellent efficiency!")
        elif efficiency > 5:
            print("⚙️ Average efficiency")
        else:
            print("🛑 Low efficiency")
    except ValueError:
        print("⚠️ Invalid input. Please enter numbers.")


# 2. Time vs Profit Analysis
def time_vs_profit():
    try:
        profit = float(input("\n💰 Total profit made: "))
        time_spent = float(input("⏱️ Time spent (in hours): "))

        profit_per_hour = profit / time_spent
        print(f"\n💡 Profit per hour: {profit_per_hour:.2f} credits")

        if profit_per_hour > 100:
            print("🚀 High profit generation!")
        elif profit_per_hour > 50:
            print("⚙️ Average profit generation")
        else:
            print("🛑 Low profit generation")
    except ValueError:
        print("⚠️ Invalid input. Please enter numbers.")


# 3. Personal Goal Tracker
def personal_goal_tracker():
    try:
        goal = float(input("\n🎯 What is your personal goal (credits)? "))
        progress = float(input("📊 How much progress have you made so far (credits)? "))

        remaining = goal - progress
        print(f"\n💡 Remaining to reach goal: {remaining:.2f} credits")

        if remaining <= 0:
            print("🎉 Goal achieved!")
        else:
            print(f"Keep going, you're {remaining:.2f} credits away from your goal!")
    except ValueError:
        print("⚠️ Invalid input. Please enter numbers.")


# 4. Performance Comparison
def performance_comparison():
    try:
        personal_scrap = float(input("\n🛠️ How much scrap did you produce? "))
        team_scrap = float(input("👥 How much scrap did the team produce? "))

        performance_score = (personal_scrap / team_scrap) * 100
        print(f"\n💡 Your performance: {performance_score:.2f}% of team average")

        if performance_score > 100:
            print("🚀 You're outperforming the team!")
        elif performance_score > 75:
            print("⚙️ You're doing great!")
        else:
            print("🛑 Time to push harder!")
    except ValueError:
        print("⚠️ Invalid input. Please enter numbers.")


# 5. Daily Target Reminder
def daily_target_reminder():
    try:
        target = float(input("\n🎯 What's your daily target (credits)? "))
        progress = float(input("📊 How much progress have you made so far today? "))

        remaining = target - progress
        print(f"\n💡 You need {remaining:.2f} credits to reach your daily target.")

        if remaining <= 0:
            print("🎉 Daily target achieved!")
        else:
            print(f"Keep pushing! You are {remaining:.2f} credits away.")
    except ValueError:
        print("⚠️ Invalid input. Please enter numbers.")


def show_menu():
    while True:
        print("\n==== Lethal Company Overtime Calculator ====")
        print("1. Calculate Overtime")
        print("2. Use Target Planner")
        print("3. Quota Helper")
        print("4. Team Efficiency Tracker")
        print("5. Time vs Profit Analysis")
        print("6. Personal Goal Tracker")
        print("7. Performance Comparison")
        print("8. Daily Target Reminder")
        print("9. Exit")

        choice = input("\nChoose an option (1-9): ").strip()

        if choice == "1":
            overtime_with_target()
        elif choice == "2":
            target_planner()
        elif choice == "3":
            quota_helper()
        elif choice == "4":
            team_efficiency_tracker()
        elif choice == "5":
            time_vs_profit()
        elif choice == "6":
            personal_goal_tracker()
        elif choice == "7":
            performance_comparison()
        elif choice == "8":
            daily_target_reminder()
        elif choice == "9":
            print("Good luck out there, employee 👋")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")


# Run the menu
if __name__ == "__main__":
    show_menu()
