class BasicBot :
    def process(self) :
        print("Reading text data...")

class LexBot(BasicBot) :
    def process(self) :
        super().process() # super()use karke hum parent class ka method call kar sakte hain
        print("Extracting Intent for AWS Lambda...")

my_travel_lexV2bot = LexBot()
my_travel_lexV2bot.process()