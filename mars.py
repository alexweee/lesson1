import ephem

final_planeta = "Mars"
#mars = ephem.Mars("2000/01/01")
mars = (getattr(ephem, final_planeta), ("2000/01/01"))
const = ephem.constellation(mars)

print(const)

