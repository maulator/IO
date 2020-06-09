import mysql.connector

def dodaj(sql):
    polacz = mysql.connector.connect(host='localhost', database='hutaszkla', user='root', password='')
    cursor = polacz.cursor()
    cursor.execute(sql)
    polacz.commit()
    cursor.close()

def wyswietl(sql):
    polacz = mysql.connector.connect(host='localhost', database='hutaszkla', user='root', password='')
    cursor = polacz.cursor()  
    cursor.execute(sql)
    data = cursor.fetchall()
    return data

def dodaj_pracownika(id_prac,imie,nazwisko,stanowisko):
    sql = f"INSERT INTO `pracownik` (`pracownikID`, `pracownikImie`, `pracownikNazwisko`, `stanowisko`) \
    VALUES ('{id_prac}', '{imie}', '{nazwisko}', '{stanowisko}')"
    dodaj(sql)

def usun_pracownika(id_prac):
    sql = f"DELETE FROM `pracownik` WHERE `pracownik`.`pracownikID` = {id_prac}"
    dodaj(sql)
    ...
def wypisz(info,tabela):
    return (f"SELECT {info} FROM {tabela}")

def wypisz_all(tabela):
    return (f"SELECT * FROM {tabela}")
