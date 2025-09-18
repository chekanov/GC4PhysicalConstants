# Dimensionless physical constants 
# For numeric computation, we assume that all known values have the same
# relative precision of a factor 10-100 better than the relative error on electron mass/rho-meson
# The currect precision is 0.03% for mass of electron/rho. This means that the constants
# such as PI or alpha_1 should be only 10-100 times better than the best measured value electron/rho
# In the case of the assymetric errors, we take tha largest one.
# in the case of asymetric errors, the largest is taken
# when dividing masses, use
# https://www.omnicalculator.com/statistics/error-propagation
# S.Chekanov (ANL)
## FULL SET OF CONSTANTS: https://pdg.lbl.gov/2025/reviews/contents_sports.html

# name, value, error, latex code 
constant={}
# hakank: change from 3.1415926535 +/- 0.0000000001
constant["PI"] = [3.14159,0.00001, "\\pi"]

# strength of interactions
constant["Fine-structure constant (inv)"]=[137.036,0.001, "\\alpha^{-1}"]
constant["Strong coupling constant at Z0"] = [0.1180, 0.0009, "\\alpha_S"]

# https://en.wikipedia.org/wiki/Dimensionless_physical_constant
# sin theta angles 
# Cabibo-Kobayashi-Maskawa mixing matrix
# page 14
# https://pdg.lbl.gov/2025/reviews/rpp2024-rev-ckm-matrix.pdf

constant["CKM 12-mixing angle"]=[0.22501,0.00068, "\\theta_{12}" ]
constant["CKM 23-mixing angle"]=[0.04183,0.00079, "\\theta_{23}"]
constant["CKM 13-mixing angle"]=[0.003732,0.000090, "\\theta_{13}"]
constant["CKM CP-violating phase"]=[1.147,0.026, "\\delta"]
# Maki-Nakagawa-Sakata mixing matrix removed since we do not use neutrino masses


# masses normalized by the rho_mass: 0.77526±0.00023 GeV or 775.26±0.23 MeV 
# https://pdg.lbl.gov/2025/listings/particle_properties.html
# Use MSbar masses for quarks 
constant["electron mass"] =[0.0006591, 0.0000002, "m_e" ]
constant["muon mass"] =    [0.13630,0.00004, "m_{\\mu}"]
constant["tau mass"] =     [2.2920,0.0007, "m_{\\tau}"]
constant["u-quark mass"] = [0.002786, 0.000090, "m_u"]
constant["d-quark mass"] = [0.006062, 0.000090, "m_d"]
constant["s-quark mass"] = [0.1206, 0.0010, "m_s"]
constant["c-quark mass"] = [1.6420, 0.0059, "m_c"]
constant["b-quark mass"] = [5.3956, 0.0092, "m_b"]
constant["t-quark mass"] = [222.583, 0.405, "m_t"]
constant["Z-boson mass"] = [117.622,0.035, "m_Z"]
constant["W-boson mass"] = [103.667,0.035, "m_W"]
constant["H-boson mass"] = [161.494,0.149, "m_H"]


# we will keep all constants (PI, alpha)  with the maximum precision 0.03%, as for the best measured
# particle (electrons)
def show():
  for key, value in constant.items():
      relError=value[1]/value[0]
      print(key, "[",value[2], "]  val=", value[0], "+-", value[1], " rel=",relError*100,"% ")  


show()

def showLatex():
    print("name & string & value & error & relative ")
    for key, value in constant.items():
      rel=100*float(value[1])/float(value[0])
      srel="%0.4f" % rel 
      s=key+" & " + "$"+str(value[2])+"$"+" & "+ str(value[0]) + " & "+ str(value[1])+" & "+srel  
      print(s+"\\\\")

showLatex()





