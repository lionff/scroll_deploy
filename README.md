
scroll deploy OmniBtc/Owlto/Merkly

# Установить либу если еще нет

pip install web3

# Запуск
python3 deploy.py

Берет приватники из privates.txt и рандомно деплоит контракты от OmniBtc, Owlto, Merkly
Минимум настроек: 

time_ot = 200 # Пауза междку кошельками в диапазоне от
time_do = 500 # Пауза ДО

randomim_koshelki = True # True or False - Перемешивание порядка кошельков
