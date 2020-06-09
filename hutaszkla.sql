-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 09 Cze 2020, 23:53
-- Wersja serwera: 10.4.11-MariaDB
-- Wersja PHP: 7.2.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `hutaszkla`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `chlodzenie`
--

CREATE TABLE `chlodzenie` (
  `chlodzenieID` int(11) NOT NULL,
  `dataChlodzenia` date DEFAULT NULL,
  `godzinaChlodzenia` time DEFAULT NULL,
  `temp` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `chlodzenie`
--

INSERT INTO `chlodzenie` (`chlodzenieID`, `dataChlodzenia`, `godzinaChlodzenia`, `temp`) VALUES
(201, '2020-06-05', '12:34:28', 1200),
(202, '2020-06-06', '10:12:48', 1200),
(203, '2020-06-07', '15:28:31', 1200);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `logowanie`
--

CREATE TABLE `logowanie` (
  `login` varchar(15) NOT NULL,
  `haslo` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `logowanie`
--

INSERT INTO `logowanie` (`login`, `haslo`) VALUES
('admin', 'admin1');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `magazyn`
--

CREATE TABLE `magazyn` (
  `materialID` int(10) NOT NULL,
  `produktNazwa` varchar(40) NOT NULL,
  `cena` float NOT NULL,
  `dataZamowienia` date NOT NULL,
  `ilosc` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `magazyn`
--

INSERT INTO `magazyn` (`materialID`, `produktNazwa`, `cena`, `dataZamowienia`, `ilosc`) VALUES
(101, 'Piasek', 700, '2020-05-05', 10),
(102, 'Soda', 500, '2020-05-05', 1),
(103, 'Wapno', 300, '2020-05-05', 1),
(104, 'Piasek', 1400, '2020-05-25', 20),
(105, 'Soda', 1000, '2020-05-25', 2),
(106, 'Wapno', 600, '2020-05-25', 2);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `pracownik`
--

CREATE TABLE `pracownik` (
  `pracownikID` int(10) NOT NULL,
  `pracownikImie` varchar(40) NOT NULL,
  `pracownikNazwisko` varchar(40) NOT NULL,
  `stanowisko` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `pracownik`
--

INSERT INTO `pracownik` (`pracownikID`, `pracownikImie`, `pracownikNazwisko`, `stanowisko`) VALUES
(1, 'Paweł', 'Bornikojka', 'Magazynier'),
(2, 'Filip', 'Ankowiak', 'Magazynier'),
(3, 'Kuba', 'Ogryzek', 'Administrator'),
(4, 'Michał', 'Czarny', 'Administrator'),
(5, 'Piotr', 'Brzęka', 'Pracownik hali'),
(6, 'Jakub', 'Wodny', 'Pracownik hali'),
(7, 'Andrzej', 'Piwny', 'Pracownik hali'),
(8, 'Jan', 'Obra', 'Pracownik hali');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `chlodzenie`
--
ALTER TABLE `chlodzenie`
  ADD PRIMARY KEY (`chlodzenieID`);

--
-- Indeksy dla tabeli `logowanie`
--
ALTER TABLE `logowanie`
  ADD PRIMARY KEY (`login`);

--
-- Indeksy dla tabeli `magazyn`
--
ALTER TABLE `magazyn`
  ADD PRIMARY KEY (`materialID`);

--
-- Indeksy dla tabeli `pracownik`
--
ALTER TABLE `pracownik`
  ADD PRIMARY KEY (`pracownikID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
