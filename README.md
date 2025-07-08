# GC4PhysicalConstants

**Genetic Computing for Physical Constants using AI**

This repository contains analytic snippets generated through generic computation (GC) for future AI-based analysis. The goal of this data is to identify patterns and relationships between fundamental physical constants. These data surve as the inputs for several AI techniques, including generative AI algorithms, for the analysis of patterns, or any structures that may reflect the underlying relations in high-dimensional functional space.

If you use these data with analytic functions, please cite the following work:

> **"Discovering the Underlying Analytic Structure within Standard Model Constants Using Artificial Intelligence"**  
> S. V. Chekanov and H. Kjellerstrand, HEP-ANL-197373, June 26, (2025).  
> [arXiv:2507.00225](https://arxiv.org/abs/2507.00225) (Submitted to a journal)

Bibtex entry:
```bibtex
@article{Chekanov:2025wzw,
    author = "Chekanov, S. V. and Kjellerstrand, H.",
    title = "{Discovering the underlying analytic structure within Standard Model constants using artificial intelligence}",
    eprint = "2507.00225",
    archivePrefix = "arXiv",
    primaryClass = "hep-ph",
    reportNumber = "HEP-ANL-197373",
    month = "6",
    year = "2025"
}
```

---

## Downloading the dataset

The main file for download is called ```standard_model_snippets.json.gz```. It is a Python dictionary file in the JSON format, after gzip compression. 
The file contains analytic expressions up to the rank 70. One can download it using  the ```wget``` or ```curl``` programs like this:

```
wget https://github.com/chekanov/GC4PhysicalConstants/raw/refs/heads/main/standard_model_snippets.json.gz
```

---

## How to Use the Files in This Repository

Here's a Python example of how to read thsi compressed JSON file:

```python
import gzip
import json

jsonfilename = "standard_model_snippets.json.gz"
with gzip.open(jsonfilename, 'r') as fin:
    data = json.loads(fin.read().decode('utf-8'))
```
Here, ```data``` is a dictionary where the keys range from 6 to 70, representing analytic ranks. Each value associated with a key is a list structured as follows:

```
[equation,error,predicted,target]
```
where ```equation``` is the symbolic equation (using the notation close to LaTeX), ```error``` is the obtained uncertainty (expressed as a percentage to the target value), ```predicted``` is the predicted value, and 
```target``` is the actual value of the constant.  There are more than 83,000 analytic snippets. All duplicate entries have been removed. 

The data listing does not have precision constraints applied. This means  ```|predicted - target|``` difference is always within the measured uncertainty of the target value as defined by the Standard Model. The limitation of  1% relative precision as in the in the original publication was not used.

## Using data with mass units

The GC analysis was also performed on the SM inputs without normalization of masses by the rho(770). In this case, the vast majority of snippets (>95%) do not pass dimensional analysis, and the snippets for the electron and muon masses cannot be recovered due to the very large precision on such masses. Still, there are several interesting relations that pass dimensional analysis. However, they can also be recovered in the original analysis with the rescaled masses.

## Note

The file "standard_model_snippets.json.gz" is referred to as the *rho-meson snippet listing*, since we use the rho-particle for removing mass units and for error smoothing. The latter  
implies reducing the variability of errors and making them more uniform. This particle must not be fundamental, because using any fundamental mass would exclude it from the dataset. We cannot use the Planck scale mass due to its extremely large value for genetic computing (limitted by the maximum value of 10^12). However, we are open to using other non-fundamental particles as well.

We are constantly improving this set of analytic snippets as more CPU power becomes available. Therefore, the number of snippets above the rank 15 may be larger than what was presented in the listings of the original paper. The differences mainly affect the least precise constants of the Standard Model.


---

S. V. Chekanov and H.Kjellerstrand (June 26, 2025)

