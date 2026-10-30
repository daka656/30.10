import pandas as pd
df = pd.read_csv("./uczniowie.csv")

print("******")
print(df)
print("******")
srednia = df["Ocena"].mean()
print(srednia)
print("******")
print(df["Ocena"].max())
print("******")
print(df["Wiek"])
print("******")
dane = str(df)
with open("m.txt","w") as f:
    f.write(dane)
print("******------------------")
danejson = pd.read_json("uczniowie.json")
print(danejson)
print("*****")
for i in range(3):
    if(danejson.at[i, "Wiek"] > 17):
        print(f'Uczen numer {i} jest pelnoletni')
    else:
        print(f'Uczen numer {i} nie jest pelnoletni')




