import mimesis
from mimesis import Address

adrRU = Address(mimesis.locales.EN)

print("Adress:", adrRU.address())
