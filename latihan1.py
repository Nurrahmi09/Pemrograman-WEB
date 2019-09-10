class Lingkaran(object):
  def __init__(self, a, p, r):
    self.angka = a
    self.phi = p
    self.jari2 = r
  def KelilingLingkaran(self):
    return self.angka * self.phi * self.jari2
   
 def main():
  lingkaran1 = Lingkaran(9, 3.14, 4)
  
  print('objek lingkaran1')
  print('angka\t: ',lingkaran1.angka)
  print('phi\t: ', lingkaran1.phi)
  print('jari-jari\t: ',lingkaran1.jari2)
  print('Keliling Lingkaran\t= ',lingkaran1.KelilingLingkaran())
  
  lingkaran2 = Lingkaran(7, 3.14, 8)
  
  print('objek lingkaran2')
  print('angka\t: ',lingkaran2.angka)
  print('phi\t: ', lingkaran2.phi)
  print('jari-jari\t: ',lingkaran1.jari2)
  print('Keliling Lingkaran\t= ',lingkaran2.KelilingLingkaran())
  
if __name__ == "__main__":
  main()
  
 class lingkarann(object):
    def __init__(self, p, r, r1):
      self.phi1 = p
      self.jarijari = r
      self.jarijari1 = r1
     
    def LuasLingkaran(self):
    return self.phi1 * self.jarijari * self.jarijari1
    
 def main():
  lingkaran3 = lingkarann(3.14, 9, 3)
  
  print('Objek lingkaran3')
  print('phi\t: ', lingkaran3.phi1)
  print('jari-jari1\t : ',lingkaran3.jarijari)
  print('Luas Lingkaran\t= ',lingkaran3.LuasLingkaran())
  
  lingkaran4 = lingkarann(3.14, 10, 5)
  
  print('Objek lingkaran4')
  print('phi\t: ', lingkaran4.phi1)
  print('jari-jari1\t : ',lingkaran4.jarijari)
  print('Luas Lingkaran\t= ',lingkaran4.LuasLingkaran())
  
if __name__ == "__main__":
  main()
  
  
  
