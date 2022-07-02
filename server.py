from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep
from random import uniform

# Create an instance of ModbusServer
db = DataBank()
server = ModbusServer('127.0.0.1', 12345, no_block=True, data_bank=db)

try:
    print('Start server ...')
    server.start()
    print('Server is online')
    state = [0]
    while True:
        db.set_holding_registers(address=0, word_list=[int(uniform(0, 100))])
        if state != db.get_holding_registers(address=1):
            state = db.get_holding_registers(address=1)
            print('Value of Register has changed to ' + str(state))
        sleep(0.5)

except:
    print('Shutdown sever ...')
    server.stop()
    print('Server is offline')
