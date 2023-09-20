import unittest 
import dates_str as ds
import dates_file as df

class TestDatesFile(unittest.TestCase):
    self.assertRaises(TypeError,df.option2 , 1)

        
        
class TestDatesConsole(unittest.TestCase):
    def formato(self):
        self.assertEqual(20 de junho de 2020, 30 de junho de 2020, 10)
   def test_ano_bissexto(self):
       self.assertEqual(ds.option1(27 de Fevereiro de 2016, 1 de Março de 2016), 3)
            

if __name__ == " __main__" :
    unittest.main()
    