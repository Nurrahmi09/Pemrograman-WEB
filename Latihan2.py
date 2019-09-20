class Motor(object):
  def __init__(self, a):
    self.a = a
  def cetakA(self):
    print("Motor = ", self.a)
 class mobil(object):
  def __init__(self, b):
    self.b = b
  def cetakB(self):
    print("mobil = ", self.b)
 class Pemilik(Motor, mobil):
  def __init__(self, a, b, c):
    Motor.__init__(self, a)
    mobil.__init__(self, b)
    self.c = c
  def cetakC(self):
  print("pemilik = ",self.c)
  
def main():
  obj= Pemilik("Yamaha NMax", "Honda Jazz", "Rizki")
  obj.cetakA()
  obj.cetakB()
  obj.cetakC()

if __name__ == "__main__":
  main()
   
