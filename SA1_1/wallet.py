from web3 import Web3

ganacheUrl = "http://127.0.0.1:7545" 
web3 = Web3(Web3.HTTPProvider(ganacheUrl))

class Account():
    def __init__(self):
        self.account = web3.eth.account.create()
        self.address = self.account.address

class Wallet():
    def checkConnection(self):
        if web3.is_connected():
           return True
        else:
            return False
            
    # Define makeTransaction method that accepts senderAddress, receiverAddress, amount, senderType
    
        # Set default address i.e web3.eth.defaultAccount to senderAddress
        

        # Check if senderType is 'ganache'
        
            # Pass a dict with "from", "to", "value" keys to web3.eth.send_transaction() method and store result in tnxHash
            
            
        