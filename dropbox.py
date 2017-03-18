import dropbox

class DropManager():

    def __init__(self, key=None):
        self.key=key
        self.api=""
        self.connect()

    def connect(self):
        self.api=dropbox.Dropbox(self.key)
        print("Conection done!!!")
        print(self.key.api)
        #print("Bienvenido !!" + self.getAccountInfo().name.display_name)

    def getAccountInfo(self):
        return self.api.users_get_current_account()

if __name__ == '__main__':
    db=DropManager("5rvGpinmKiYAAAAAAAAKjbgntDYp0Wz4UQaDb3jBWQDGgdozkn1qwZKlAkO91k4y")
