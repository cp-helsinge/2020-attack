# 2020 Attack

## Mapper

###o bj: spil objecter
Dette spil er skruet sammen, så det egner sig til samarbejde, gennem gidhub.

Vi følger [PEP8](https://www.python.org/dev/peps/pep-0008/) i videst muligt omfang. (Ret gerne ind, hvis du finder uinkonsistens) dog med den undtagelse at vi har opdelt programmet, så de fleste objekter, der indgår i spilet, er i deres eget modul (Som man gør i mange andre sprog, men altså normalt ikke i python) 
Dette har vi gjort, for at gøre det lettere at arbejde mange sammen, på det samme program, gennem github.

For atgøre det lettere at importere alle klasser, er der indført følgende regler:
- objekter der optræder i spilet, har hver sin klasse
- Hver af disse klasser, er i hver sin fil, i obj mappen
- Filnavnen definerer klassen, men selve klasse hedder "Create" i alle disse filer. På den måde referes til klassen som: obj.<navn>.Create(<parametre>) (navn er med småt)
- obj klasserne skal som minimum følgende:
    - __init__()
    - draw()
    - tick_advance()
    - rect

### gfx: grafik filer

### sound: lydfiler



