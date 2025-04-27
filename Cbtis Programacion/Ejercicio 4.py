cantidades = [float(input("Cantidad: ")) for i in range(5)]
print("Resultado:", cantidades)

print("Mayor:", max(cantidades))
print("Menor:", min(cantidades))

for i, cantidad in enumerate(sorted(cantidades, reverse=True), 1):
    print(f"P{i}: {cantidad}")

# By Josue Alvarado Gutierrez