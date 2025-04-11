import math

def overtime():
    scrap_sold = float(input("\nquota fulfilled: "))
    profitquota = float(input("profit quota: "))
    daysuntildeadline = int(input("days until deadline: "))

    # Overtime berekening
    overtime_score = math.floor((scrap_sold - profitquota) / 5 + 15 * daysuntildeadline)
    print("\novertime: ", overtime_score)

def target():
    gebruik_target = input("\nWil je een target instellen? (ja/nee): ").lower()

    if gebruik_target == "ja":
        target = float(input("Wat is je target (credits)? "))
        huidige_loot = float(input("Hoeveel credits heb je al ? "))
        dagen_over = int(input("Hoeveel dagen zijn er tot de deadline? "))
        aantal_spelers = int(input("Met hoeveel spelers ben je? "))

        resterend = target - huidige_loot

        if resterend <= 0:
            print(f"\n🎉 Je hebt je target van {target} credits al gehaald!")
        else:
            per_dag = resterend / dagen_over
            per_speler = per_dag / aantal_spelers
            print(f"\n🎯 Target: {target} credits")
            print(f"📦 Je hebt al: {huidige_loot} credits")
            print(f"📅 Dagen over: {dagen_over}")
            print(f"👥 Spelers: {aantal_spelers}")
            print(f"💰 Nodig per dag: {per_dag:.2f} credits")
            print(f"👤 Per persoon per dag: {per_speler:.2f} credits")


overtime()
