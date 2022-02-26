'''
2. Feladat
A program generáljon 5 egész számot [0;10] intervallumon, tárolja egy halmazban. 
A felhasználónak meg kell próbálni kitalálni ezeket, olyan módon, hogy megad 5 számot, melyeket szintén halmazban tárol a gép.

A program tájékoztassa a felhasználót, a következőkről: hány darab számot talált el, és melyek ezek; hány számot nem talált el, és melyek ezek; mely számok kerültek rögzítésre a generálás vagy a felhasználó miatt; mely számok nem szerepeltek egyik halmazban sem!
'''

from random import randint

osszes = set([i for i in range(11)])
szamok = set()
while len(szamok)<5:
   szamok.add(randint(0,10))

beker = set([int(input('Szám (1-10): ')) for i in range(5)])

print()

sikeres = set(szamok & beker)
print(f'Ennyi számot találtál el: ',len(sikeres))
print(f'Eltalált számok: {sikeres}')

print()

el_nem_talalt = set(szamok - beker)
print(f'Ennyi számot találtál el: ',len(el_nem_talalt))
print(f'Nem eltalált számok: {el_nem_talalt}')

print()

rogzitesre_kerult_szamok = set(szamok | beker)
print(f'Ennyi szám került rögzítésre: ',len(rogzitesre_kerult_szamok))
print(f'Rögzített számok: {rogzitesre_kerult_szamok}')

print()

egyikbensem = set(osszes - rogzitesre_kerult_szamok)
print(f'Egyikben sem: ',len(egyikbensem))
print(f'Számok melyek egyikben sem szerepeltek: {egyikbensem}')