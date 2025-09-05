import sys
from ROOT import TCanvas,gStyle,TLine,TPostScript,gROOT,TH1D,TF1,TProfile2D,TEllipse,TGraph,TRandom3,TFile,TLatex,TLegend,TPaveText,TGraphErrors,kRed,gPad,kBlue,kGreen,kCyan,kAzure,kYellow,kTRUE
import ROOT
import os

print ('Number of arguments:', len(sys.argv), 'arguments.') 
print ('Argument List:', str(sys.argv))
print ('Use as: script.py -b 0 (or 1,2)') 
myinput="interactive"
if (len(sys.argv) ==2):
   myinput = sys.argv[1]
print ("Mode=",myinput) 

def myTextIt(x,y,color=1,size=0.08,text=""):
  l=TLatex()
  l.SetTextSize(size);
  l.SetNDC();
  # more like italic
  l.SetTextFont(52)
  l.SetTextColor(color);
  l.DrawLatex(x,y,text);

figdir="figs/"
name=os.path.basename(__file__)
epsfig=figdir+name.replace(".py",".eps")

nameX="Total complexity"
nameY="Nr of events"
Ymin=0
Ymax=10-1
Xmin=0
Xmax=1200-1 


gROOT.Reset()

######################################################
gROOT.SetStyle("Plain");
c1=TCanvas("c_massjj","BPRE",10,10,600,600);
# c1.Divide(3,3,0.008,0.007);
ps1 = TPostScript( epsfig,113)

c1.cd(1);
gPad.SetLogy(0)
gPad.SetLogx(0)
#gPad.SetTopMargin(0.05)
gPad.SetBottomMargin(0.13)
gPad.SetLeftMargin(0.19)
gPad.SetRightMargin(0.03)
gPad.SetTopMargin(0.02)
h=gPad.DrawFrame(Xmin,Ymin,Xmax,Ymax);
ax=h.GetXaxis(); ax.SetTitleOffset(1.1)
ay=h.GetYaxis();
ay.SetTitle( nameY );
ax.SetTitle( nameX );
ay.SetTitleSize( 0.05 );
ax.SetTitleSize( 0.05 );

gStyle.SetOptStat("nemr");

ax.SetTitleOffset(1.1)
ay.SetTitleOffset(1.4)
ay.Draw("same")
h.Draw()

h1=TH1D("system complexity","system complexity", 60, 0, 1200);
total=0

xtotalA=[]
xtotalB=[]
with open("randomA.csv", 'r') as file:
        for line in file:
             line=line.strip()
             if (len(line)<2): continue
             if (line.find("#")>-1): continue
             line=line.split(",")
             ran1=int(line[0])
             par1=int(line[1])
             rank1=int(line[2])
             isbroken1=int(line[3])
             if (isbroken1>0): par1=(par1+1) 
             y1=rank1*par1 
             xtotalA.append(y1)


with open("randomB.csv", 'r') as file:
        for line in file:
             line=line.strip()
             if (len(line)<2): continue
             if (line.find("#")>-1): continue
             line=line.split(",")
             ran2=int(line[0])
             par2=int(line[1])
             rank2=int(line[2])
             isbroken2=int(line[3])
             if (isbroken2>0): par2=(par2+1)
             y2=rank2*par2
             xtotalB.append(y2)

# fill histograms with complicity
for j in range(len(xtotalA)):
      print(xtotalA[j], xtotalB[j])
      x=xtotalA[j]+xtotalB[j]
      h1.Fill(x) 

h1.SetStats(1)
h1.Draw("histo")


print("In the case of missing equatins, we just take the existing rank and add extra variable=",total/15)
print("Average complexity for 15 tests=",total/15)
# standard model for 2 solutions has this complexity rank
# total ranks x nr of variables
SM=149*3 +118*1 
print("SM complexity=", SM)

v_line= TLine(SM,0,SM,2); # declare the vertical line
v_line.SetLineColor(2);
v_line.SetLineWidth(2);
v_line.Draw("L same");

myTextIt(0.24,0.5,color=2,size=0.05,text="SM system="+str(SM))

gPad.Update();

print (epsfig)
gPad.RedrawAxis()
c1.Update()
ps1.Close()
if (myinput != "-b"):
              if (input("Press any key to exit") != "-9999"):
                         c1.Close(); sys.exit(1);



