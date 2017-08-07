# -*- coding: utf-8 -*-

AGRI = "agri"
ECON = "econ"
EDUC = "educ"
ENER = "ener"
ENVI = "envi"
GOVE = "gove"
HEAL = "heal"
INTR = "intr"
JUST = "just"
REGI = "regi"
SOCI = "soci"
TECH = "tech"
TRAN = "tran"

# TODO: Use english texts and translate them
SUPER_THEME_CHOICES = (
    (AGRI, "Agroganadería, pesca y forestación"),
    (ECON, "Economía y finanzas"), 
    (EDUC, "Educación, cultura y deportes", ),
    (ENER, "Energía"),
    (ENVI, "Medio ambiente"), 
    (GOVE, "Gobierno y sector público"),
    (HEAL, "Salud"),
    (INTR, "Asuntos internacionales"),
    (JUST, "Justicia, seguridad y legales"),
    (REGI, "Regiones y ciudades"),
    (SOCI, "Población y sociedad"),
    (TECH, "Ciencia y tecnología"),
    (TRAN, "Transporte"),
)

EVENTUAL_ACCRUAL_PERIODICITY = "eventual"

ACCRUAL_PERIODICITY_DICT = {    
    "quarterly" : "R/P3M",
    "biannually": "R/P6M",
    "weekly": "R/P1W",
    "irregular": EVENTUAL_ACCRUAL_PERIODICITY,
    "fortnightly": "R/P2W",
    "monthly": "R/P1M",
    "asNeeded": EVENTUAL_ACCRUAL_PERIODICITY,
    "annually": "R/P1Y",
    "daily": "R/P1D",
    "notPlanned": EVENTUAL_ACCRUAL_PERIODICITY,
    "continual": "R/PT1S",
    "unknown": EVENTUAL_ACCRUAL_PERIODICITY
}
