#
# bitfield manipulation test
#

import unittest
from bitField import bf


class TestBitField(unittest.TestCase):

    def setUp(self):
        pass;

    def test_zero_default(self):
        # make sure the shuffled sequence does not lose any elements
        k = bf()
        self.assertIsInstance(k,bf)
        self.assertEqual(int(k), 0)
        self.assertEqual(len(k), 0)
        self.assertFalse(k)

    def test_zero_default_length(self):
        k8 = bf(length=8)
        self.assertIsInstance(k8,bf)
        self.assertEqual(int(k8), 0)
        self.assertFalse(k8)


    def test_full_assign(self):
        # make sure the shuffled sequence does not lose any elements
        k = bf(0x1)
        self.assertIsInstance(k,bf)
        self.assertEqual(int(k), 1)
        self.assertTrue(int(k)==1)
        self.assertTrue(k)
        self.assertEqual(len(k), 0)


        k = bf(0xFF)
        self.assertIsInstance(k,bf)
        self.assertEqual(int(k), 0xFF)
        self.assertTrue(int(k)==0xFF)
        self.assertTrue(k)

        k = bf(0xFFFF)
        self.assertIsInstance(k,bf)
        self.assertEqual(int(k), 0xFFFF)
        self.assertTrue(int(k)==0xFFFF)
        self.assertTrue(k)


        k = bf(0xFFFFFFFF)
        self.assertIsInstance(k,bf)
        self.assertEqual(int(k), 0xFFFFFFFF)
        self.assertTrue(int(k)==0xFFFFFFFF)
        self.assertTrue(k)


    def test_full_assign_8bit(self):
        # make sure the shuffled sequence does not lose any elements
        k = bf(0x1,8)
        self.assertIsInstance(k,bf)
        self.assertEqual(int(k), 1)
        self.assertTrue(int(k)==1)
        self.assertTrue(k)
        self.assertEqual(len(k), 8)


        k = bf(0xFF,8)
        self.assertIsInstance(k,bf)
        self.assertEqual(int(k), 0xFF)
        self.assertTrue(int(k)==0xFF)
        self.assertTrue(k)

        k = bf(0xFFFF,8)
        self.assertIsInstance(k,bf)
        self.assertEqual(int(k), 0xFF)
        self.assertTrue(int(k)==0xFF)
        self.assertTrue(k)


        k = bf(0xFFFFFFFF,8)
        self.assertIsInstance(k,bf)
        self.assertEqual(int(k), 0xFF)
        self.assertTrue(int(k)==0xFF)
        self.assertTrue(k)

    def test_full_assign_16(self):
        # make sure the shuffled sequence does not lose any elements
        k = bf(0x1,length=16)
        self.assertIsInstance(k,bf)
        self.assertEqual(int(k), 1)
        self.assertTrue(int(k)==1)
        self.assertTrue(k)
        self.assertEqual(len(k), 16)


        k = bf(0xFF,length=16)
        self.assertIsInstance(k,bf)
        self.assertEqual(int(k), 0xFF)
        self.assertTrue(int(k)==0xFF)
        self.assertTrue(k)

        k = bf(0xFFFF,length=16)
        self.assertIsInstance(k,bf)
        self.assertEqual(int(k), 0xFFFF)
        self.assertTrue(int(k)==0xFFFF)
        self.assertTrue(k)


        k = bf(0xFFFFFFFF,length=16)
        self.assertIsInstance(k,bf)
        self.assertEqual(int(k), 0xFFFF)
        self.assertTrue(int(k)==0xFFFF)
        print int(k)

        k = bf(0x8000,length=16)
        self.assertIsInstance(k,bf)
        self.assertEqual(int(k), 0x8000)
        self.assertTrue(int(k)==0x8000)
        print int(k)

    def test_full_assign_32(self):
        # make sure the shuffled sequence does not lose any elements
        k = bf(0x1,length=32)
        self.assertIsInstance(k,bf)
        self.assertEqual(int(k), 1)
        self.assertTrue(int(k)==1)
        self.assertEqual(len(k), 32)


        k = bf(0xFF,32)
        self.assertIsInstance(k,bf)
        self.assertEqual(int(k), 0xFF)
        self.assertTrue(int(k)==0xFF)

        k = bf(0xFFFF,length=32)
        self.assertIsInstance(k,bf)
        self.assertEqual(int(k), 0xFFFF)
        self.assertTrue(int(k)==0xFFFF)


        k = bf(0xFFFFFFFF,32)
        self.assertIsInstance(k,bf)
        self.assertEqual(int(k), 0xFFFFFFFF)
        self.assertTrue(int(k)==0xFFFFFFFF)



    def test_full_assign_fail(self):
        # make sure the shuffled sequence does not lose any elements
        k = bf(2)
        self.assertIsInstance(k,bf)
        self.assertFalse(int(k)==1)
        self.assertNotEqual(int(k), 1)


    def test_slice_assign(self):
        k = bf()
        self.assertIsInstance(k,bf)

        k[3:7]=5
        self.assertIsInstance(k,bf)
        self.assertEqual(int(k), 0x28)
        k = bf()
        k[3:7]=7
        self.assertEqual(int(k), 0x38)
        k = bf()
        k[3:7]=15
        self.assertEqual(int(k), 0x78)

        #This test is to make sure we do not assign more than the slice
        k = bf()
        k[3:7]=0xFF
        self.assertEqual(int(k), 0x78)

        k = bf(0x0000)
        k[3:7]=0xF
        self.assertEqual(int(k), 0x78)

        k = bf(0x0000)
        k[4:8]=0xF
        self.assertEqual(int(k), 0xF0)

        k = bf(0xFFFF)
        k[4:8]=0x0
        self.assertEqual(int(k), 0x0FF0F)

        k = bf(0xFFFF)
        k[0:8]=0x0
        self.assertEqual(int(k), 0x0FF00)

        k = bf(0xFFFF)
        k[0:1]=0x0
        self.assertEqual(int(k), 0x0FFFE)

        k = bf(0xFFFF)
        k[15:16]=0x0
        self.assertEqual(int(k), 0x07FFF)



    def test_lsh(self):
        k = bf(1)
        self.assertEqual(int(k), 0x01)
        k <<= 1
        self.assertIsInstance(k,bf)
        self.assertEqual(int(k), 0x02)
        k <<= 1
        self.assertEqual(int(k), 0x04)
        k <<= 4
        self.assertEqual(int(k), 0x40)


        k = bf(0x0F)
        self.assertEqual(int(k), 0x0F)
        k <<= 1
        self.assertIsInstance(k,bf)
        self.assertEqual(int(k), 0x1E)
        k <<= 1
        self.assertEqual(int(k), 0x3C)
        k <<= 4
        self.assertEqual(int(k), 0x3C0)
        k <<= 4
        self.assertEqual(int(k), 0x3C00)

    def test_lsh_8(self):
        k = bf(1,8)
        self.assertEqual(int(k), 0x01)
        k <<= 1
        self.assertIsInstance(k,bf)
        self.assertEqual(int(k), 0x02)
        k <<= 1
        self.assertEqual(int(k), 0x04)
        k <<= 4
        self.assertEqual(int(k), 0x40)
        k <<= 4
        self.assertEqual(int(k), 0x00)

        #Check to make sure that the length has been remembered
        k = k | 0xFFFF
        self.assertEqual(int(k), 0xFF)


    def test_lsh_16(self):
        k = bf(0x0F,16)
        self.assertEqual(int(k), 0x0F)
        k <<= 1
        self.assertIsInstance(k,bf)
        self.assertEqual(int(k), 0x1E)
        k <<= 1
        self.assertEqual(int(k), 0x3C)
        k <<= 4
        self.assertEqual(int(k), 0x3C0)
        k <<= 4
        self.assertEqual(int(k), 0x3C00)
        k <<= 4
        self.assertEqual(int(k), 0xC000)
        k <<= 4
        self.assertEqual(int(k), 0x0000)

        #Check to make sure that the length has been remembered
        k = k | 0xFFFF
        self.assertEqual(int(k), 0xFFFF)

        #Check to make sure that the length has been remembered
        k = k | 0xFFFFFFFF
        self.assertEqual(int(k), 0xFFFF)



    def test_rsh(self):
        k = bf(0xFF)
        self.assertEqual(int(k), 0xFF)
        k >>= 1
        self.assertIsInstance(k,bf)
        self.assertEqual(int(k), 0x7F)
        k >>= 1
        self.assertEqual(int(k), 0x3F)
        k >>= 4
        self.assertEqual(int(k), 0x03)
        k >>= 4
        self.assertEqual(int(k), 0x00)

        k = bf(0xFFFF)
        self.assertEqual(int(k), 0xFFFF)
        k >>= 1
        self.assertEqual(int(k), 0x7FFF)
        k >>= 1
        self.assertEqual(int(k), 0x3FFF)
        k >>= 4
        self.assertEqual(int(k), 0x03FF)
        k >>= 4
        self.assertEqual(int(k), 0x003F)

        k = bf(0xFFFFFFFF)
        self.assertEqual(int(k), 0xFFFFFFFF)
        k >>= 1
        self.assertEqual(int(k), 0x7FFFFFFF)
        k >>= 1
        self.assertEqual(int(k), 0x3FFFFFFF)
        k >>= 4
        self.assertEqual(int(k), 0x03FFFFFF)
        k >>= 4
        self.assertEqual(int(k), 0x003FFFFF)


    def test_rsh_8(self):
        k = bf(0xFF,length=8)
        self.assertEqual(int(k), 0xFF)
        k >>= 1
        self.assertIsInstance(k,bf)
        self.assertEqual(int(k), 0x7F)
        k >>= 1
        self.assertEqual(int(k), 0x3F)
        k >>= 4
        self.assertEqual(int(k), 0x03)
        k >>= 4
        self.assertEqual(int(k), 0x00)

        #Check to make sure that the length has been remembered
        k = k | 0xFFFF
        self.assertEqual(int(k), 0xFF)



        k = bf(0xFFFFFFFF,8)
        self.assertEqual(int(k), 0xFF)
        k >>= 1
        self.assertEqual(int(k), 0x7F)
        k >>= 1
        self.assertEqual(int(k), 0x3F)
        k >>= 4
        self.assertEqual(int(k), 0x03)
        k >>= 4
        self.assertEqual(int(k), 0x00)
        #Check to make sure that the length has been remembered
        k = k | 0xFFFF
        self.assertEqual(int(k), 0xFF)



    def test_rsh_16(self):
        k = bf(0xFFF,length=16)
        self.assertEqual(int(k), 0xFFF)
        k >>= 1
        self.assertIsInstance(k,bf)
        self.assertEqual(int(k), 0x7FF)
        k >>= 1
        self.assertEqual(int(k), 0x3FF)
        k >>= 4
        self.assertEqual(int(k), 0x03F)
        k >>= 4
        self.assertEqual(int(k), 0x003)
        k >>= 4
        self.assertEqual(int(k), 0x000)


        k = bf(0xFFFFF,16)
        self.assertEqual(int(k), 0xFFFF)
        k >>= 1
        self.assertEqual(int(k), 0x7FFF)
        k >>= 1
        self.assertEqual(int(k), 0x3FFF)
        k >>= 4
        self.assertEqual(int(k), 0x03FF)
        k >>= 4
        self.assertEqual(int(k), 0x003F)

        #Check to make sure that the length has been remembered
        k = k | 0xFFFF
        self.assertEqual(int(k), 0xFFFF)

        #Check to make sure that the length has been remembered
        k = k | 0xFFFFFFFF
        self.assertEqual(int(k), 0xFFFF)

    def test_rsh_lsh_16(self):
        k = bf(0xFFF,length=16)
        self.assertEqual(int(k), 0xFFF)
        k >>= 1
        self.assertIsInstance(k,bf)
        self.assertEqual(int(k), 0x7FF)
        k >>= 5
        self.assertEqual(int(k), 0x03F)
        k <<= 4
        self.assertEqual(int(k), 0x03F0)
        k >>= 4
        self.assertEqual(int(k), 0x03F)
        k >>= 8
        self.assertEqual(int(k), 0x000)
        k <<= 4
        self.assertEqual(int(k), 0x000)


        #Check to make sure that the length has been remembered
        k = k | 0xFFFF
        self.assertEqual(int(k), 0xFFFF)

        #Check to make sure that the length has been remembered
        k = k | 0xFFFFFFFF
        self.assertEqual(int(k), 0xFFFF)

    def test_lsh_rsh_16(self):
        k = bf(0x0F,16)
        self.assertEqual(int(k), 0x0F)
        k <<= 1
        self.assertIsInstance(k,bf)
        self.assertEqual(int(k), 0x1E)
        k <<= 1
        self.assertEqual(int(k), 0x3C)
        k <<= 4
        self.assertEqual(int(k), 0x3C0)
        k >>= 4
        self.assertEqual(int(k), 0x3C)
        k <<= 8
        self.assertEqual(int(k), 0x3C00)
        k <<= 4
        self.assertEqual(int(k), 0xC000)
        k <<= 4
        self.assertEqual(int(k), 0x0000)
        k >>= 4
        self.assertEqual(int(k), 0x0000)

        #Check to make sure that the length has been remembered
        k = k | 0xFFFF
        self.assertEqual(int(k), 0xFFFF)

        #Check to make sure that the length has been remembered
        k = k | 0xFFFFFFFF
        self.assertEqual(int(k), 0xFFFF)




    def test_and(self):
        k = bf(1)
        k=k & 0x3
        self.assertIsInstance(k,bf)
        self.assertEqual(int(k), 0x001)

    def test_or(self):
        k = bf(1)
        k=k | 0x3
        self.assertIsInstance(k,bf)
        self.assertEqual(int(k), 0x003)

    def test_or_8(self):
        k = bf(0x3,8)
        k=k | 0x300
        self.assertIsInstance(k,bf)
        self.assertEqual(int(k), 0x003)

        k=k | 0x30
        self.assertEqual(int(k), 0x033)

    def test_or_16(self):
        k = bf(0x3,16)
        k=k | 0x300
        self.assertIsInstance(k,bf)
        self.assertEqual(int(k), 0x303)

        k = bf(0x3,16)
        k=k | 0x30
        self.assertEqual(int(k), 0x033)

        k=k | 0xF30
        self.assertEqual(int(k), 0xF33)

        k=k | 0xFFF00
        self.assertEqual(int(k), 0xFF33)


    def test_or_32(self):
        k = bf(0x3,32)
        k=k | 0x300
        self.assertIsInstance(k,bf)
        self.assertEqual(int(k), 0x303)

        k = bf(0x3,32)
        k=k | 0x30
        self.assertEqual(int(k), 0x033)

        k=k | 0xF30
        self.assertEqual(int(k), 0xF33)

        k=k | 0xFFF00
        self.assertEqual(int(k), 0xFFF33)

        k=k | 0x12300000
        self.assertEqual(int(k), 0x123FFF33)


    def test_read_bit(self):
        k = bf(0x6)
        self.assertIsInstance(k,bf)
        self.assertEqual(int(k), 0x006)
        self.assertEqual(k[0], 0x0)
        self.assertEqual(k[1], 0x1)
        self.assertEqual(k[2], 0x1)
        self.assertEqual(k[3], 0x0)


    def test_set_bit(self):
        k = bf(0x6)
        self.assertIsInstance(k,bf)
        self.assertEqual(int(k), 0x006)
        self.assertEqual(k[0], 0x0)
        self.assertEqual(k[1], 0x1)
        self.assertEqual(k[2], 0x1)
        self.assertEqual(k[3], 0x0)
        k[0]=1
        k[1]=0
        k[2]=0
        k[3]=1
        self.assertEqual(k[0], 0x1)
        self.assertEqual(k[1], 0x0)
        self.assertEqual(k[2], 0x0)
        self.assertEqual(k[3], 0x1)


    def test_str(self):
        k = bf(0x6)
        self.assertEqual(str(k),"110")
        k = bf(0)
        self.assertEqual(str(k),"0")

        k = bf(0x6,8)
        self.assertEqual(str(k),"00000110")
        k = bf(0,8)
        self.assertEqual(str(k),"00000000")


if __name__ == "__main__":
    unittest.main()
