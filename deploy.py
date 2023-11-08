from web3 import Web3
import time
import random

abi = []
omnibtc_bytcode = '0x608060405243600055348015601357600080fd5b5060358060216000396000f3fe6080604052600080fdfea165627a7a72305820ba621ecf7b70183d2bc65f3b3a1ab23211f1ccdf5d5b61213d5ecd3f20ffefa60029'
owlto_bytcode = '0x6080604052348015600f57600080fd5b50603f80601d6000396000f3fe6080604052600080fdfea2646970667358221220bc612630cc0a226fd67c37cd542e43e860635ca379bfc2fd320a9af6eed16c6664736f6c63430008120033'
merkly_bytcode = '0x60806040526000805461ffff1916905534801561001b57600080fd5b5060fb8061002a6000396000f3fe6080604052348015600f57600080fd5b506004361060325760003560e01c80630c55699c146037578063b49004e914605b575b600080fd5b60005460449061ffff1681565b60405161ffff909116815260200160405180910390f35b60616063565b005b60008054600191908190607a90849061ffff166096565b92506101000a81548161ffff021916908361ffff160217905550565b61ffff81811683821601908082111560be57634e487b7160e01b600052601160045260246000fd5b509291505056fea2646970667358221220666c87ec501268817295a4ca1fc6e3859faf241f38dd688f145135970920009264736f6c63430008120033'

time_ot = 200 # Пауза междку кошельками в диапазоне от
time_do = 500 # Пауза ДО

randomim_koshelki = True # True or False - Перемешивание порядка кошельков

scroll_w3 = Web3(Web3.HTTPProvider('https://rpc.ankr.com/scroll'))

with open("privates.txt", "r") as f:
    addr_list = [row.strip() for row in f if row.strip()]
    if randomim_koshelki:
        random.shuffle(addr_list)

for private in addr_list:
    try:

        account = scroll_w3.eth.account.from_key(private)
        address = account.address

        print(f'Работаем с {address}')

        contract = scroll_w3.eth.contract(
            abi=abi,
            bytecode=random.choice([omnibtc_bytcode, owlto_bytcode, merkly_bytcode])
        )

        tx = contract.constructor().build_transaction({
            'from': address,
            'value': 0,
            "gasPrice": scroll_w3.eth.gas_price,
            'nonce': scroll_w3.eth.get_transaction_count(address),
        })

        signed_transaction = scroll_w3.eth.account.sign_transaction(tx, private)
        txn = scroll_w3.eth.send_raw_transaction(signed_transaction.rawTransaction)

        # Проверяем транзу
        while True:
            try:
                if scroll_w3.eth.get_transaction_receipt(txn)['status'] != 1:
                    time.sleep(random.randint(20, 30))
                else:
                    time.sleep(random.randint(5, 10))
                    break
            except:
                pass

        print(f"Transaction: https://scrollscan.com/tx/{txn.hex()}")
        time.sleep(random.randint(time_ot, time_do))

    except Exception as err:
        print(err)


