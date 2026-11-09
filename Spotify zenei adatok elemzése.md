# Spotify zenei adatok elemzése

## A projekt bemutatása

A projekt célja a Spotify dalokat tartalmazó adathalmaz elemzése Python segítségével. A vizsgálat során a dalok népszerűségét és különböző zenei tulajdonságait elemeztem, például a táncolhatóságot, az energiát és a hosszúságot.

## Felhasznált technológiák

- **Python** – az adatok feldolgozásához
- **Pandas** – adatok betöltéséhez, tisztításához és elemzéséhez
- **NumPy** – numerikus műveletekhez
- **Matplotlib** – diagramok készítéséhez

## Adathalmaz

A projektben a Kaggle oldaláról letölthető Spotify Tracks Dataset adathalmazt használtam.

Adathalmaz: https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset

A letöltött CSV-fájlt `dataset.csv` néven kell elhelyezni a Python-programmal azonos mappában.

## Az adatok előkészítése

A program:
- Betölti a CSV-fájlt.
- Ellenőrzi az adatok felépítését.
- Eltávolítja a duplikált és hiányos sorokat.
- Kiszűri az érvénytelen értékeket.
- A dalok hosszát milliszekundumról percre alakítja.

## Vizsgált kutatási kérdések

1. **Melyik zenei műfaj a legnépszerűbb?**  
   A műfajok átlagos népszerűségének összehasonlítása.

2. **Van-e kapcsolat a K-pop dalok táncolhatósága és népszerűsége között?**  
   A táncolhatóság és a népszerűség kapcsolatának vizsgálata.

3. **Van-e kapcsolat a K-pop dalok energiája és népszerűsége között?**  
   Az energia és a népszerűség összefüggésének vizsgálata.

4. **Milyen hosszúságú dalok a legnépszerűbbek?**  
   A különböző hosszúságú dalok átlagos népszerűségének összehasonlítása.

5. **Népszerűbbek-e az explicit dalok?**  
   Az explicit és nem explicit dalok népszerűségének összehasonlítása.

6. **Milyen összefüggések vannak a zenei jellemzők között?**  
   A különböző zenei tulajdonságok közötti korrelációk vizsgálata.

**Fontos:** A 2. és 3. kérdésnél kizárólag K-pop dalokat vizsgáltam, és a diagramokon legfeljebb 250 véletlenszerű adatpontot jelenítettem meg. A korreláció kiszámításához az összes rendelkezésre álló K-pop adatot felhasználtam. A többi elemzés a teljes tisztított adathalmazon történik.

## Szükséges csomagok telepítése

A program futtatása előtt telepíteni kell a szükséges Python-könyvtárakat:

```bash
pip install pandas numpy matplotlib
```

## A program futtatása

1. Töltsd le a Kaggle-adathalmazt.
2. Helyezd a `dataset.csv` fájlt a Python-kód mellé.
3. Telepítsd a szükséges csomagokat.
4. Futtasd a Python-programot.

## Eredmények

A program létrehozza az `eredmenyek` mappát, amelyben az elkészített diagramok és az elemzések eredményei találhatók.

## Összegzés

A projekt során a Spotify zenei adatait dolgoztam fel és elemeztem. A cél az volt, hogy különböző statisztikai módszerekkel és diagramokkal megvizsgáljam a dalok népszerűségét, hosszúságát és zenei tulajdonságait.