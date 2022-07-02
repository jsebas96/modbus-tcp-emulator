from pyModbusTCP.client import ModbusClient

client = ModbusClient(host='127.0.0.1', port=12345)
client.open()

# client.write_multiple_registers(1, [1, 2, 3])
regs = client.read_holding_registers(0, 5)
if regs:
    print(regs)
else:
    print('Unable to read registers')
client.close()
