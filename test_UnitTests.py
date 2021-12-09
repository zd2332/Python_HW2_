import WhoAmI_File
def test_WhoAmI():
    assert WhoAmI_File.WhoAmI() != 'djr2132'
        
import BondPrice_File
def test_getBondPrice():
    assert round(BondPrice_File.getBondPrice(.03, 2000000, .04, 10,  1)) == 2170604
    assert round(BondPrice_File.getBondPrice(.03, 2000000, .04, 10,  2)) == 2171686

import BondDuration_File
def test_getBondDuration():
    assert round(BondDuration_File.getBondDuration(.03, 2000000, .04, 10,1),2) == 8.51

import BondPrice_E_File
def test_GetBondPriceE():
    yc = [.010,.015,.020,.025,.030]
    face = 2000000
    couponRate = .04
    assert round(BondPrice_E_File.getBondPrice_E(face, couponRate, yc)) == 2098949 

import BondPrice_Z_File
def test_GetBondPriceZ():
    yc = [.010,.015,.020,.025,.030]
    times=[1,1.5,3,4,7]
    face = 2000000
    couponRate = .04
    x = BondPrice_Z_File.getBondPrice_Z(face, couponRate, times, yc)
    assert round(x) == 1996533
    
import FizzBuzz_File
def test_FizzBuzz():
    x = FizzBuzz_File.FizzBuzz(40,45)
    assert x[0] == "buzz"
    assert x[1] == 41
    assert x[5] == "fizzbuzz"
