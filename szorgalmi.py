


# ============================================================
# SPOTIFY ZENEI ADATHALMAZ ELEMZÉSE
# Kutatási projekt - Pandas és Matplotlib
# ============================================================


import pandas as pd
import sys
import numpy as np
import matplotlib.pyplot as plt
import os

try:
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
except ModuleNotFoundError:
    print("Hiányzó könyvtárak észleléve. Telepítés folyamatban (ez eltarthat fél percig)...")
import subprocess 

subprocess.check_call(
[sys.executable, "-m", "pip", "install", "matplotlib", "numpy", "pandas"]
)
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

print("Sikeres telepítés! A program indul...")

# ------------------------------------------------------------
# 1. ADATOK BETÖLTÉSE
# ------------------------------------------------------------

print("=" * 60)
print("SPOTIFY ADATELEMZÉSI PROJEKT")
print("=" * 60)

df = pd.read_csv("dataset.csv")

print("\n1. ADATOK BETÖLTÉSE")
print("Adatok mérete:", df.shape)

print("\nAz első 5 sor:")
print(df.head())

print("\nOszlopok és adattípusok:")
print(df.info())

# ------------------------------------------------------------
# 2. ADATOK ELLENŐRZÉSE
# ------------------------------------------------------------

print("\n2. ADATOK ELLENŐRZÉSE")

print("\nHiányzó értékek:")
print(df.isnull().sum())

print("\nDuplikált sorok száma:")
print(df.duplicated().sum())

print("\nStatisztikai összefoglaló:")
print(df.describe())

# ------------------------------------------------------------
# 3. ADATOK TISZTÍTÁSA
# ------------------------------------------------------------

print("\n3. ADATOK TISZTÍTÁSA")

df = df.drop_duplicates()

# Fontos oszlopok ellenőrzése
required_columns = [
    "track_genre",
    "popularity",
    "danceability",
    "energy",
    "duration_ms",
    "explicit"
]

df = df.dropna(subset=required_columns)

# Hibás értékek kiszűrése
df = df[
    (df["popularity"].between(0, 100)) &
    (df["danceability"].between(0, 1)) &
    (df["energy"].between(0, 1)) &
    (df["duration_ms"] > 0)
].copy()

# Dalhossz átalakítása percre
df["duration_min"] = df["duration_ms"] / 60000

print("Tisztítás utáni adatok mérete:", df.shape)

# Eredmények mappája
os.makedirs("eredmenyek", exist_ok=True)

# ------------------------------------------------------------
# 4. ALAPVETŐ STATISZTIKÁK
# ------------------------------------------------------------

print("\n4. ALAPVETŐ STATISZTIKÁK")

print("Dalok száma:", len(df))
print("Műfajok száma:", df["track_genre"].nunique())
print("Átlagos népszerűség:", round(df["popularity"].mean(), 2))
print("Átlagos dalhossz:", round(df["duration_min"].mean(), 2), "perc")
print("Átlagos energia:", round(df["energy"].mean(), 3))
print("Átlagos táncolhatóság:", round(df["danceability"].mean(), 3))

# ------------------------------------------------------------
# 5. KUTATÁSI KÉRDÉS 1.
# MELYIK ZENEI MŰFAJ A LEG NÉPSZERŰBB?
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("1. KUTATÁSI KÉRDÉS")
print("Melyik zenei műfaj a legnépszerűbb?")
print("=" * 60)

genre_popularity = (
    df.groupby("track_genre")["popularity"]
    .mean()
    .sort_values(ascending=False)
)

print("\nTop 10 legnépszerűbb műfaj:")
print(genre_popularity.head(10))

print("\nLegnépszerűbb műfaj:",
      genre_popularity.idxmax())

plt.figure(figsize=(10, 6))

genre_popularity.head(10).sort_values().plot(
    kind="barh"
)

plt.title("A 10 legnépszerűbb zenei műfaj")
plt.xlabel("Átlagos népszerűség")
plt.ylabel("Műfaj")
plt.tight_layout()
plt.savefig("eredmenyek/01_mufajok.png")
plt.show()

# ------------------------------------------------------------
# 6. KUTATASI KERDES 2.
# K-POP: TANCOLHATOSAG ES NEPSZERUSEG
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("2. KUTATASI KERDES")
print("K-pop tancolhatosag es nepszeruseg")
print("=" * 60)

# Kizárólag K-pop adatok kiválasztása
kpop_df = df[
    df["track_genre"].str.strip().str.lower() == "k-pop"
].copy()

# Maximum 250 adatpont a grafikonhoz
kpop_plot = kpop_df.sample(
    n=min(1000, len(kpop_df)),
    random_state=42
)

print("Osszes K-pop dal:", len(kpop_df))
print("Grafikonon megjeleno adatpontok:", len(kpop_plot))

# Korreláció az összes K-pop adaton
dance_corr = kpop_df["danceability"].corr(
    kpop_df["popularity"]
)

print("Korrelacio:", round(dance_corr, 3))

plt.figure(figsize=(9, 6))

plt.scatter(
    kpop_plot["danceability"],
    kpop_plot["popularity"],
    alpha=0.5
)

plt.title("K-pop: Tancolhatosag es nepszeruseg")
plt.xlabel("Tancolhatosag")
plt.ylabel("Nepszeruseg")

plt.tight_layout()
plt.savefig("eredmenyek/02_kpop_tancolhatosag.png")
plt.show()

# ------------------------------------------------------------
# 7. KUTATASI KERDES 3.
# K-POP: ENERGIA ES NEPSZERUSEG
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("3. KUTATASI KERDES")
print("K-pop energia es nepszeruseg")
print("=" * 60)

# Maximum 250 adatpont a grafikonhoz
kpop_plot = kpop_df.sample(
    n=min(1000, len(kpop_df)),
    random_state=42
)

print("Osszes K-pop dal:", len(kpop_df))
print("Grafikonon megjeleno adatpontok:", len(kpop_plot))

# Korreláció az összes K-pop adaton
energy_corr = kpop_df["energy"].corr(
    kpop_df["popularity"]
)

print("Korrelacio:", round(energy_corr, 3))

plt.figure(figsize=(9, 6))

plt.scatter(
    kpop_plot["energy"],
    kpop_plot["popularity"],
    alpha=0.5
)

plt.title("K-pop: Energia es nepszeruseg")
plt.xlabel("Energia")
plt.ylabel("Nepszeruseg")

plt.tight_layout()
plt.savefig("eredmenyek/03_kpop_energia.png")
plt.show()

# ------------------------------------------------------------
# 8. KUTATÁSI KÉRDÉS 4.
# MILYEN HOSSZÚ DALOK A LEGNÉPSZERŰBBEK?
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("4. KUTATÁSI KÉRDÉS")
print("Dalhossz és népszerűség kapcsolata")
print("=" * 60)

df["duration_group"] = pd.cut(
    df["duration_min"],
    bins=[0, 3, 4, 5, float("inf")],
    labels=[
        "3 perc alatt",
        "3-4 perc",
        "4-5 perc",
        "5 perc felett"
    ]
)

duration_popularity = (
    df.groupby("duration_group", observed=True)
    ["popularity"]
    .mean()
)

print("\nÁtlagos népszerűség dalhossz szerint:")
print(duration_popularity)

print("\nLegnépszerűbb kategória:",
      duration_popularity.idxmax())

plt.figure(figsize=(9, 6))

duration_popularity.plot(kind="bar")

plt.title("Dalhossz és népszerűség")
plt.xlabel("Dalhossz")
plt.ylabel("Átlagos népszerűség")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("eredmenyek/04_dalhossz.png")
plt.show()

# ------------------------------------------------------------
# 9. KUTATÁSI KÉRDÉS 5.
# NÉPSZERŰBBEK-E AZ EXPLICIT DALOK?
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("5. KUTATÁSI KÉRDÉS")
print("Explicit dalok népszerűsége")
print("=" * 60)

explicit_popularity = (
    df.groupby("explicit")["popularity"]
    .mean()
)

print("\nÁtlagos népszerűség:")
print(explicit_popularity)

if True in explicit_popularity.index and False in explicit_popularity.index:

    explicit_value = explicit_popularity.loc[True]
    clean_value = explicit_popularity.loc[False]

    if explicit_value > clean_value:
        print("Az explicit dalok népszerűbbek.")
    elif explicit_value < clean_value:
        print("A nem explicit dalok népszerűbbek.")
    else:
        print("A két csoport népszerűsége azonos.")

plt.figure(figsize=(8, 5))

explicit_popularity.plot(kind="bar")

plt.title("Explicit és nem explicit dalok népszerűsége")
plt.xlabel("Explicit tartalom")
plt.ylabel("Átlagos népszerűség")
plt.xticks(
    [0, 1],
    ["Nem explicit", "Explicit"],
    rotation=0
)

plt.tight_layout()
plt.savefig("eredmenyek/05_explicit.png")
plt.show()

# ------------------------------------------------------------
# 10. PLUSZ ELEMZÉS: KORRELÁCIÓS MÁTRIX
# ------------------------------------------------------------

print("\n6. PLUSZ ELEMZÉS")
print("Korrelációs mátrix")

numeric_columns = [
    "popularity",
    "danceability",
    "energy",
    "valence",
    "tempo",
    "duration_min",
    "acousticness",
    "instrumentalness",
    "liveness",
    "speechiness"
]

correlation_matrix = df[numeric_columns].corr()

print(correlation_matrix.round(2))

plt.figure(figsize=(11, 8))

plt.imshow(correlation_matrix, cmap="coolwarm", vmin=-1, vmax=1)

plt.colorbar(label="Korreláció")

plt.xticks(
    range(len(numeric_columns)),
    numeric_columns,
    rotation=45,
    ha="right"
)

plt.yticks(
    range(len(numeric_columns)),
    numeric_columns
)

plt.title("Spotify változók korrelációs mátrixa")

plt.tight_layout()
plt.savefig("eredmenyek/06_korrelacio.png")
plt.show()

# ------------------------------------------------------------
# 11. EREDMÉNYEK MENTÉSE
# ------------------------------------------------------------

print("\n7. EREDMÉNYEK MENTÉSE")

genre_popularity.to_csv(
    "eredmenyek/mufajok_nepszerusege.csv"
)

duration_popularity.to_csv(
    "eredmenyek/dalhossz_nepszerusege.csv"
)

explicit_popularity.to_csv(
    "eredmenyek/explicit_nepszeruseg.csv"
)

correlation_matrix.to_csv(
    "eredmenyek/korrelacios_matrix.csv"
)

# ------------------------------------------------------------
# 12. VÉGSŐ ÖSSZEFOGLALÓ
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("A PROJEKT ELEMZÉSE BEFEJEZŐDÖTT")
print("=" * 60)

print("\nFŐBB EREDMÉNYEK:")

print("Legnépszerűbb műfaj:",
      genre_popularity.idxmax())

print("Táncolhatóság korreláció:",
      round(dance_corr, 3))

print("Energia korreláció:",
      round(energy_corr, 3))

print("Legnépszerűbb dalhossz-kategória:",
      duration_popularity.idxmax())

print("\nAz eredmények az 'eredmenyek' mappába kerültek.")

print("\nA program sikeresen lefutott!")
