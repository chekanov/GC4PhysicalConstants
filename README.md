# GC4PhysicalConstants

**Genetic Computing for Physical Constants using AI**

This repository contains analytic expressions with relationships among the fundamental constants of the Standard Model. These expressions are created through generic computation (GC), which is part of the artificial intelligence (AI) field. The goal of this library is to identify analytic patterns and relationships among fundamental physical constants, or to use these expressions in constructing models with a minimal number of free parameters. These data can serve as inputs for several AI techniques, including generative AI algorithms, for the analysis of patterns or structures that may reflect underlying relationships between Standard Model parameters in high-dimensional functional space.

If you use these data with analytic functions, please cite the following work:

> **"Discovering the Underlying Analytic Structure within Standard Model Constants Using Artificial Intelligence"**  
> S. V. Chekanov and H. Kjellerstrand, HEP-ANL-197373 (2025).  
> [arXiv:2507.00225](https://arxiv.org/abs/2507.00225) (Submitted to a journal)

<details>
  <summary><i>View BibTex Entry</i></summary>

```bibtex
@article{Chekanov:2025wzw,
    author = "Chekanov, S. V. and Kjellerstrand, H.",
    title = "{Discovering the underlying analytic structure
    within Standard Model constants using artificial intelligence}",
    eprint = "2507.00225",
    archivePrefix = "arXiv",
    primaryClass = "hep-ph",
    reportNumber = "HEP-ANL-197373",
    month = "6",
    year = "2025"
}
```
</details>

---

## Using JSON data

The main file for download is called ```standard_model_snippets.json.gz```. It is a dictionary file in the JSON format, after gzip compression. 
The file contains analytic expressions up to the rank 70. One can download it using  the ```wget``` or ```curl``` programs like this:

```
wget https://github.com/chekanov/GC4PhysicalConstants/raw/refs/heads/main/standard_model_snippets.json.gz
```

---

Here's a Python example of how to read this compressed JSON file:

```python
import gzip, json
jsonfilename = "standard_model_snippets.json.gz"
with gzip.open(jsonfilename, 'r') as fin:
    data = json.loads(fin.read().decode('utf-8'))
    print(data) # print data if you need
```
Here, ```data``` is a Pyhon dictionary, where the keys range from 6 to 70, representing analytic ranks. If you use other programs, simply ```gunzip``` this JSON file and read it as a text file.

Each value associated with a key is a list structured as follows:

```
[equation,error,predicted,target,pass]
```
where ```equation``` is the symbolic equation (using the notation close to LaTeX), ```error``` is the obtained uncertainty (expressed as a percentage to the target value), ```predicted``` is the predicted value, and 
```target``` is the actual value of the constant. The symbolic relations contain up to 2 variables. The variable ```pass``` is either 0 (do not pass dimensional analysis, if masses are replaced with the orinal masses), or 1  (pass the dimensional analysis). There are more than 83,400 analytic snippets. All duplicate entries have been removed. Note that  ```|predicted - target|``` difference is always within the measured uncertainty of the target value as defined by the Standard Model. The requirement of 1% for relative precision, as was set in the original paper, is not used.

## Using TXT data

Much larger datasets are avaliable in the form of compressed TXT files. They are:

``` bash
standard_model_snippets.txt.gz          # snippets afrer the rho-meson re-scaling
standard_model_snippets_no_norm.txt.gz  # snippets without the rho-meson re-scaling
```
Each line contains a snippet using the PiCAT notations for mathematical functions. On Linux, you can analyze such files without decompression like this:

``` bash
zgrep "m_u = " standard_model_snippets.txt.gz
```
search for the expressions for the mass of the UP-quark. 

Here is another example:

``` bash
zgrep "m_u = " standard_model_snippets.txt.gz | grep "m_H"
```
search for the expressions for the mass of the UP-quark, which must contain the mass of the Higgs boson (m_H). The names of the constants can be found in the original preprint.


## Using data with mass units

As a test, the GC analysis was also performed on the Standard Model inputs without normalization of masses by the rho(770) mass. See the file ```standard_model_snippets_original.json.gz``` or ```standard_model_snippets_no_norm.txt.gz```. The vast majority of snippets do not pass dimensional analysis, and the snippets for the electron and muon masses cannot be recovered due to the very large precision on such masses. Several interesting relations that pass the dimensional analysis can also be recovered in the original analysis with the rescaled masses, therefore, the method using the original masses is less intresting. We can send the file without rescaled masses by requests.

## Notes

(1) The file "standard_model_snippets.json.gz" is referred to as the *rho-meson snippet listing* since it uses the rho-meson mass for removing mass units and for error smoothing. The latter implies reducing the variability of errors and making them more uniform. This particle used for rescaling must not be fundamental, because using any fundamental mass would automatically exclude it from the dataset. We cannot use the Planck scale mass due to its extremely large value for genetic computing (limitted by the maximum value of 10^12). However, we are open to using other non-fundamental particles as well.

(2) It should be emphasized that the presence of the rho-meson mass (or any other non-fundamental particle used to obtain dimensionless constants) is merely a convenient method for deriving relationships in GC without violating dimensional consistency. It serves as an auxiliary parameter. In the final model or theory, the rho-meson mass must disappear after appropriate variable substitutions. All obtained relations can be converted to the correct physical masses (in GeV or MeV) using Table 3 or 4 of the preprint.

(3) We are constantly improving this set of analytic snippets as more CPU power becomes available. Therefore, the number of snippets above the rank 15 may be (slightly) larger than what was presented in the listings of the original paper. The differences mainly affect the least precise constants of the Standard Model.

---

S. V. Chekanov and H.Kjellerstrand (June 26, 2025)

