import sys
from ROOT import TCanvas,TPostScript,gROOT,TH1D,TF1,TProfile2D,TEllipse,TGraph,TRandom3,TFile,TLatex,TLegend,TPaveText,TGraphErrors,kRed,gPad,kBlue,kGreen,kCyan,kAzure,kYellow,kTRUE
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


gROOT.Reset()
figdir="figs/"
name=os.path.basename(__file__)
epsfig=figdir+name.replace(".py",".eps")

nameX="Nr of missing equations"
# nameY="Complexity"
nameY="C_{a}"
Ymin=401    
Ymax=900-1 
Xmin=-0.1   
Xmax=1.2 

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
ay.SetTitleSize( 0.08 );
ax.SetTitleSize( 0.055 );
ay.SetLabelSize( 0.055 );
ax.SetLabelSize( 0.055 );
ax.SetNdivisions(102)

ax.SetTitleOffset(1.1)
ay.SetTitleOffset(1.1)
ay.Draw("same")
h.Draw()

size=1.4
gg1=TGraphErrors()
gg1.SetMarkerColor( 2 )
gg1.SetLineColor(1)
gg1.SetMarkerSize(size)
gg1.SetMarkerStyle(20)
gg1.SetLineWidth(1)
gg1.SetLineStyle(1)
x=0 
y=149*3 
gg1.SetPoint(0,x,y)
gg1.Draw("p")


def getData(xfile, which=4, color=1, ctype=24):

     cross2=TGraph()
     cross2.SetLineColor( 1 )
     cross2.SetMarkerColor( color )
     cross2.SetMarkerSize(1.4)
     cross2.SetMarkerStyle( ctype)
     cross2.SetLineWidth(2)
     cross2.SetLineStyle(1)

     nn=0
     with open(xfile, 'r') as file:
        for line in file:
             line=line.strip()
             if (len(line)<2): continue
             if (line.find("#")>-1): continue
             line=line.split(",")
             ran=int(line[0])
             par=int(line[1])
             rank=int(line[2])
             isbroken=int(line[3])
             y=rank*par
             x=isbroken
             print(y,x)
             cross2.SetPoint(nn,x,y)
             nn=nn+1                            

     return cross2 

ran1=getData("randomA.csv")
ran1.Draw("p")

leg2=TLegend(0.45, 0.7, 0.9, 0.85);
leg2.SetBorderSize(0);
leg2.SetTextFont(62);
leg2.SetFillColor(10);
leg2.SetTextSize(0.04);
leg2.AddEntry(gg1,"Standard Model","p")
leg2.AddEntry(ran1,"Random variations","p")
leg2.Draw("same");


myTextIt(0.72,0.9,color=1,size=0.08,text="Picat")


print (epsfig) 
gPad.RedrawAxis()
c1.Update()
ps1.Close()
if (myinput != "-b"):
              if (input("Press any key to exit") != "-9999"):
                         c1.Close(); sys.exit(1);




