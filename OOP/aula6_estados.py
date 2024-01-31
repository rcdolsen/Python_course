# Mantendo estados dentro da classe

class Camera:
    def __init__(self, nome, recording=False):
        self.nome = nome
        self.recording = recording

    def record(self):
        if self.recording:
            print(f'{self.nome} ja esta filmando')
            return 
        
        print(f'{self.nome} esta filmando')
        self.recording = True

    def stop_record(self):
        if not self.recording:
            print(f'{self.nome} nao esta filmando')
            return 
        
        print(f'{self.nome} parou de filmar')
        self.recording = False
    
    def photo(self):
        if self.recording:
            print(f'{self.nome} nao pode fotografar enquanto filma')
            return

        print(f'{self.nome} esta no modo fotografia')
        self.photo = True


c1 = Camera('Canon')
c2 = Camera('Leica')
c1.record()
c1.record()
c1.photo()
c1.stop_record()
c1.photo()
#print(c1.recording)
#print(c2.recording)
print('-' * 50)
c2.stop_record()
c2.record()
c2.record()
c2.photo()
c2.stop_record()