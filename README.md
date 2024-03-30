Problem wypasionej imprezy- rozwinięcie problemu plecakowego
=================================================================

Opis problemu:

Problem polega na zorganizowaniu imprezy na której będzie jak najwięcej osób, lecz każda osoba ma 3 preferencje - ilość posiłków, ilość napojów oraz ilość zakąsek. My jako organizatorzy mamy określoną ilość tych zasobów, a naszym zadaniem jest zoptymalizować dobór gości, aby jednocześnie spełnić te wymagania oraz nie przekroczyć ograniczeń dotyczących dostępnych posiłków, napojów i przekąsek. Naszym celem jest maksymalizacja liczby zaproszonych gości i zrobienia najlepszej imprezy jaką się da. W tym problemie plecakiem jest sala imprezowa, a 'przedmiotami' są ludzie których próbujemy zaprosić.



| Lp | Kategoria                                  | Złożoność          |
|----|--------------------------------------------|--------------------|
| 1  | Generator danych                           | O(n)               |
| 2  | Konwerter danych dla algorytmu genetycznego| O(n)               |
| 3  | Algorytm siłowy (rekurencyjny)            | O(2^n)             |
| 4  | Algorytm siłowy (iteracyjny)              | O(2^n)             |
| 5  | Algorytm zachłanny                         | O(n log(n))        |
| 6  | Algorytm genetyczny                        | O(n * P * G)       |

Legenda:
- n: liczba gości
- P: ilość genomów w populacji
- G: ilość generacji

