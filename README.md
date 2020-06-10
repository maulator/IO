# Instrukcja uruchomienia prototypu

1. Pobrać aplikację XAMPP
2. Po zainstalowaniu i uruchomieniu włączyć Apache oraz MySQL
3. W przeglądarce wpisać adres http://localhost/phpmyadmin/  albo można kliknąć przycisk Admin obok przycisku Start w aplikacji XAMPP
4. Utworzyć pustą bazę o nazwie: hutaszkla
5. Następnie należy zaimportować plik udostępniony w repozytorium o nazwie: hutaszkla.sql
6. Przed uruchomieniem prototypu należy zaimportować moduł mysql.connector(pip install mysql.connector)
7. Program wykorzystuje QT framework wiec może być potrzeba zaimportowania modułu pyqt5 (pip install pyqt5)
8. Po poprawnym zaimportowaniu modułów oraz bazy danych należy pobrać main.py oraz folder Modules i uruchomić plik main.py

# Informacje do przedestowania prototypu
1. Hasło do zalogowania się to, login: admin, hasło: admin1
2. Poprawna sekwencja sprawdzenia systemu jest następująca
    Start systemu -> Rozruch -> czekanie aż pasek rozruchu załaduje się do 100% -> włączenie przycisku Maszyny off -> Przycisk aktywuje
    działanie maszyn po czym można obserwować jak rośnie temperatura, która będzie rosła do 1220 stopni po czym pojawi się Warning,
    który spowoduje uruchomienie chłodzenia po czym temperatura zacznie spadać az do 1150 stopni.
3. Przycisk chłodzenie ręczne należy używać dopiero po wyłączeniu działania maszyn.
4. Niewskazane jest wielokrotne klikanie przycisków, ponieważ symulacja jest przeprowadzana na timerach oraz inkrementacji zmiennych, które
   się na siebie nakładają. (niestety nie udało mi się tego naprawić na czas)
5. Po skończonej symulacji przycisk stop dezaktywuje działanie przycisków z wyjątkiem przycisku Start.
6. W górnym rogu jest zegar, który odlicza działanie systemu od momentu naciśnięcia przycisku Start.
7. W założeniach temperatura oraz czas systemu miałbyć przekazywany do bazy danych po każdym Warningu o krytycznej temperaturze albo
   po wyłączeniu systemu.
   
