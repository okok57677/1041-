fa={}
print("Enter the fruit and amount...")
while True:
    f=input("")
    if (f==""):
        break
    fn,am=f.split()
    if not fn in fa:
        fa[fn]=int(am)
    else:
        fa[fn]=fa[fn]+int(am)
for i in fa:
    print(i,fa[i])
