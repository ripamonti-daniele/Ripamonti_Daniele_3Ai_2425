import datetime

oggi = datetime.datetime.now()
d = datetime.datetime(2008, 2, 12)

print(d.strftime("%d-%m-%Y"))
print(oggi.strftime("%d-%m-%Y"))

diff = oggi - d

print(diff)

if diff.days >= 6200:
    print("puoi partecipare")

else:
    print("sei troppo piccolo/a")
