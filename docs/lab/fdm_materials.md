# FDM Plastics Reference

## PLA


Polylactic Acid — polyester from lactic acid  
<span style="color:#4FC3F7; font-weight:600;">
C<sub>3</sub>H<sub>6</sub>O<sub>3</sub>
</span>, CH3CHOHCOOH
	

[:material-flask-outline: PLA on PubChem](https://pubchem.ncbi.nlm.nih.gov/compound/612){ .md-button .md-button--primary target=_blank}
<div class="molecule-block">
<div class="molecule-viewer" data-cid="612"></div>
</div>

| Property | Value | FDM parameter | Typical |
|---|---|---|---|
| Tg | ~60 °C | Nozzle | 190–220 °C |
| Tm | ~170–180 °C | Bed | 0–60 °C |
| Density | ~1.24 g/cm³ | Cooling | Strong |
| Strength | ~50–60 MPa | Enclosure | Not required |



**Notes**

- very easy to print  
- stiff but brittle  
- excellent surface finish  
- poor heat resistance (~50 °C limit)

**Use**

prototypes, visual parts, detailed models

---

## PETG

Polyethylene Terephthalate Glycol-modified — glycol-modified PET polyester
It's related to [PET](#pet).

<span style="color:#4FC3F7; font-weight:600;">
C<sub>18</sub>H<sub>14</sub>O<sub>8</sub>
</span>

[:material-flask-outline: PETG on PubChem](https://pubchem.ncbi.nlm.nih.gov/compound/19046907){ .md-button .md-button--primary target=_blank}

<div class="molecule-block">
<div class="molecule-viewer" data-cid="19046907"></div>
</div>


| Property | Value | FDM parameter | Typical |
|---|---|---|---|
| Tg | ~80 °C | Nozzle | 230–250 °C |
| Tm | ~220–260 °C | Bed | 70–90 °C |
| Density | ~1.27 g/cm³ | Cooling | Moderate |
| Strength | ~45–50 MPa | Enclosure | Optional |

**Notes**

- excellent layer adhesion  
- tough, slightly flexible  
- low warping  
- tends to string  
- glossy surface  
- softens near ~80 °C

**Use**

functional parts, brackets, containers, moderately outdoor parts

---

## ABS

Acrylonitrile Butadiene Styrene — engineering thermoplastic terpolymer. 
Terpolymer is made of three monomers, see [ABS monomer components](#abs-monomer-components).

<span style="color:#4FC3F7; font-weight:600;">
(C<sub>8</sub>H<sub>8</sub> · C<sub>4</sub>H<sub>6</sub> · C<sub>3</sub>H<sub>3</sub>N)<sub>n</sub>
</span>, CH2=CH–Ph + CH2=CH–CH=CH2 + CH2=CH–CN

[:material-flask-outline: ABS on PubChem](https://pubchem.ncbi.nlm.nih.gov/compound/24756){ .md-button .md-button--primary target=_blank}


| Property | Value | FDM parameter | Typical |
|---|---|---|---|
| Tg | ~105 °C | Nozzle | 230–250 °C |
| Tm | — | Bed | 90–110 °C |
| Density | ~1.04 g/cm³ | Cooling | Low |
| Strength | ~40–45 MPa | Enclosure | Recommended |

**Notes**

- strong and tough  
- higher temperature resistance than PETG  
- prone to warping and cracking  
- acetone smoothing possible  
- characteristic odor while printing

**Use**

mechanical parts, enclosures, tools, prototypes requiring heat resistance

---

## ASA

Acrylonitrile Styrene Acrylate — weather-resistant ABS-like terpolymer  

<span style="color:#4FC3F7; font-weight:600;">
(C<sub>8</sub>H<sub>8</sub> · C<sub>3</sub>H<sub>3</sub>N · C<sub>4</sub>H<sub>6</sub>O<sub>2</sub>)<sub>n</sub>
</span>, CH2=CH–Ph + CH2=CH–CN + CH2=CH–COO–R



| Property | Value | FDM parameter | Typical |
|---|---|---|---|
| Tg | ~105 °C | Nozzle | 240–260 °C |
| Tm | — | Bed | 90–110 °C |
| Density | ~1.07 g/cm³ | Cooling | Low |
| Strength | ~45 MPa | Enclosure | Recommended |

**Notes**

- similar to ABS but UV stable  
- good heat resistance  
- strong functional parts  
- prone to warping  
- acetone vapor smoothing possible

**Use**

outdoor parts, enclosures, mechanical components, automotive-like parts

---


## PET

Polyethylene Terephthalate — aromatic polyester  

<span style="color:#4FC3F7; font-weight:600;">
C<sub>10</sub>H<sub>8</sub>O<sub>4</sub>
</span>, C6H4(CO2CH2CH2O)2

[:material-flask-outline: PET on PubChem](https://pubchem.ncbi.nlm.nih.gov/compound/18721140){ .md-button .md-button--primary target=_blank}

<div class="molecule-block">
<div class="molecule-viewer" data-cid="18721140"></div>
</div>

!!! info "Relation to PETG"
    **PETG** is a modified form of **PET**.

    PET already contains **ethylene glycol** in its backbone.  
    In **[PETG](#petg)** an additional glycol-type modifier is introduced during polymerization.

    This reduces crystallinity and makes PETG **more amorphous, tougher, and easier to process**, which is why PETG works well for FDM printing.

| Property | Value | FDM parameter | Typical |
|---|---|---|---|
| Tg | ~70–80 °C | Nozzle | 240–260 °C |
| Tm | ~250–260 °C | Bed | 70–90 °C |
| Density | ~1.38 g/cm³ | Cooling | Moderate |
| Strength | ~55–75 MPa | Enclosure | Optional |

**Notes**

- highly crystalline polymer  
- strong and stiff  
- excellent chemical resistance  
- low gas permeability  
- difficult to print in FDM  
- tends to warp and crystallize during cooling

**Use**

bottles, fibers (polyester), films, engineering plastics, packaging

---

## ABS monomers

ABS is a **terpolymer** produced by polymerizing three monomers:

- acrylonitrile — provides chemical resistance and stiffness  
- butadiene — provides toughness and impact resistance  
- styrene — provides rigidity and easy processing

---

### Acrylonitrile

<span style="color:#4FC3F7; font-weight:600;">
C<sub>3</sub>H<sub>3</sub>N
</span>, CH2=CH–CN

[:material-flask-outline: Acrylonitrile on PubChem](https://pubchem.ncbi.nlm.nih.gov/compound/7855){ .md-button .md-button--primary target=_blank}

<div class="molecule-block">
<div class="molecule-viewer" data-cid="7855"></div>
</div>

---

### Styrene

<span style="color:#4FC3F7; font-weight:600;">
C<sub>8</sub>H<sub>8</sub>
</span>, C6H5–CH=CH2

[:material-flask-outline: Styrene on PubChem](https://pubchem.ncbi.nlm.nih.gov/compound/7501){ .md-button .md-button--primary target=_blank}

<div class="molecule-block">
<div class="molecule-viewer" data-cid="7501"></div>
</div>

---

### 1,3-Butadiene

<span style="color:#4FC3F7; font-weight:600;">
C<sub>4</sub>H<sub>6</sub>
</span>, CH2=CH–CH=CH2

[:material-flask-outline: 1,3-Butadiene on PubChem](https://pubchem.ncbi.nlm.nih.gov/compound/7845){ .md-button .md-button--primary target=_blank}

<div class="molecule-block">
<div class="molecule-viewer" data-cid="7845"></div>
</div>