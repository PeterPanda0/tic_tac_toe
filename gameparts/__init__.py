"""Пакет для хранения модулей игры 'Крестики - Нолики'.

Содержит два модуля:
1. exceptions.py - в модуле два исключения:
    - FieldIndexError;
    - CellOccupiedError

2. parts.py - в модуле импортируемы класс Board:
"""
# Точка в записи означает текущий каталог.
from .parts import Board
