
# Prepoznavanje lica pomoću KNN algoritma

Ovaj projekat implementira sistem za prepoznavanje lica u realnom vremenu korišćenjem kamere, OpenCV biblioteke, `face_recognition` biblioteke i K najbližih suseda (KNN) algoritma. Sistem je razvijen kao akademski projekat iz oblasti veštačke inteligencije.

## 🔧 Tehnologije

- Python 3.x
- OpenCV
- face_recognition
- NumPy

## 📁 Struktura projekta

```
projekat-knn/
├── main.py                  # Snimanje i enkodiranje lica korisnika
├── rec.py                   # Prepoznavanje lica u realnom vremenu
├── haarcascade_frontalface_default.xml  # Model za detekciju lica
├── data/                    # Folder sa enkodiranim .npy fajlovima
├── README.md                # Opis projekta
├── requirements.txt         # Spisak potrebnih Python biblioteka
```

## 📸 Funkcionalnosti

- Snimanje i enkodiranje lica korisnika
- Čuvanje vektora karakteristika u `.npy` fajl
- Učitavanje baze poznatih lica
- Prepoznavanje lica pomoću ručno implementiranog KNN algoritma
- Prikaz imena osobe iznad detektovanog lica

## ▶️ Pokretanje

1. Instaliraj potrebne biblioteke:

```
pip install -r requirements.txt
```

2. Prvo pokreni `loadData.py` da uneseš i sačuvaš uzorke lica.
   3. Zatim pokreni `recSystem.py` za prepoznavanje lica.

## 📂 Dataset

- `.npy` fajlovi se automatski kreiraju za svakog korisnika i čuvaju u `./data/` folderu.
- Svaki fajl sadrži 20 enkodiranih uzoraka lica.

## ⚠️ Napomena

- Potrebno je da `haarcascade_frontalface_default.xml` bude u istom folderu kao i skripte.
- Aplikacija koristi standardnu web kameru (`device 0`).

## 🖼️ Primeri prepoznavanja lica

U nastavku su prikazane slike koje ilustruju rad aplikacije u realnom vremenu:

![Prepoznavanje lica u realnom vremenu](images/rec1.png)
![Prepoznavanje lica u realnom vremenu](images/rec2.png)

Ova slika prikazuje primer gde aplikacija detektuje lice korisnika putem kamere i na osnovu prethodno snimljenih uzoraka uspešno prepoznaje osobu korišćenjem KNN algoritma.

## 📄 Autor

Milutin Jovanović  
Elektronski fakultet, Univerzitet u Nišu  
2024/2025 - Veštačka inteligencija
