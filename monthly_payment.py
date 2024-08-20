def calculate_monthly_payment(principal,annual_rate,year):
    rate = annual_rate / 12 / 100
    months = years * 12
    payment = (principal * rate / 1 -(1+rate) **months) 
    return payment


principal = float(input("Lånebelopp: "))
annual_rate = float(input("Årsränta (%): "))
years = int(input("Löptid (år): "))
payment = calculate_monthly_payment(principal, annual_rate, years)
print(f"Din månatliga betalning är: {payment:.2f} kr")

"""
A = avbetalning per månad i kronor
P = totala lånebeloppet 
r = räntan per period (t.ex. om räntan är 9% blir det r = 0,09 / 12)
n = totalt antal betalningsperioder """