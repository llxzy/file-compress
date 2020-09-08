import unittest
import os
import main


def create_file(filepath):
    with open(filepath, "w") as f:
        f.write("Lorem ipsum")


class ConvertTest(unittest.TestCase):
    def test_first(self):
        # tests conversion
        input_path = "./tests/first/"
        self.assertTrue(len(os.listdir(input_path)) == 1)
        self.assertTrue(os.path.exists(input_path + "a"))
        main.convert(input_path)
        self.assertTrue(len(os.listdir(input_path)) == 1)
        self.assertTrue(os.path.exists(input_path + "a.gz"))
        self.assertFalse(os.path.exists(input_path + "a"))

        #cleanup
        os.remove(input_path + "a.gz")
        create_file(input_path + "a")

    
    def test_second(self):
        #tests ignoring already zipped files and directories
        input_path = "./tests/second/"
        self.assertTrue(len(os.listdir(input_path)) == 3)
        self.assertTrue(os.path.exists(input_path + "c"))
        self.assertTrue(os.path.exists(input_path + "a.gz"))
        self.assertTrue(os.path.isdir(input_path + "b"))
        main.convert(input_path)
        self.assertTrue(len(os.listdir(input_path)) == 3)
        self.assertTrue(os.path.exists(input_path + "c.gz"))
        self.assertFalse(os.path.exists(input_path + "c"))
        self.assertTrue(os.path.exists(input_path + "a.gz"))
        self.assertTrue(os.path.isdir(input_path + "b"))
        print(os.path.exists(input_path + "c"))

        #cleanup
        os.remove(input_path + "c.gz")
        create_file(input_path + "c")

        

if __name__ == "__main__":
    unittest.main()