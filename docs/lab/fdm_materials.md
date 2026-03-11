# FDM Plastics Reference

## PLA


Polylactic Acid — polyester from lactic acid  
<span style="color:#4FC3F7; font-weight:600;">
C<sub>3</sub>H<sub>6</sub>O<sub>3</sub>
</span>, CH3CHOHCOOH
	

[:material-flask-outline: PLA on PubChem](https://pubchem.ncbi.nlm.nih.gov/compound/612){ .md-button .md-button--primary target=_blank}
<div class="molecule-block">
<div id="pla_viewer" class="molecule-viewer"></div>
</div>

<script>
document.addEventListener("DOMContentLoaded", function () {
   let viewer = $3Dmol.createViewer(
    document.getElementById("pla_viewer"),
    { backgroundColor: "rgba(226,196,161,0.718)" }
    );
  $3Dmol.download("cid:612", viewer, {}, function() {
    viewer.setStyle({}, {
        stick: {radius: 0.15},
        sphere: {scale: 0.25}});
    viewer.zoomTo();
    viewer.render();
  });
});
</script>

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

<span style="color:#4FC3F7; font-weight:600;">
C<sub>10</sub>H<sub>8</sub>O<sub>4</sub>
</span>, C6H4(CO2CH2CH2O)2

[:material-flask-outline: PETG on PubChem](https://pubchem.ncbi.nlm.nih.gov/compound/612){ .md-button .md-button--primary target=_blank}

<div class="molecule-block">
<div id="petg_viewer" class="molecule-viewer"></div>
</div>

<script>
document.addEventListener("DOMContentLoaded", function () {
   let viewer = $3Dmol.createViewer(
    document.getElementById("petg_viewer"),
    { backgroundColor: "rgba(226,196,161,0.718)" }
    );
  $3Dmol.download("cid:7222", viewer, {}, function() {
    viewer.setStyle({}, {
        stick: {radius: 0.15},
        sphere: {scale: 0.25}});
    viewer.zoomTo();
    viewer.render();
  });
});
</script>


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

Acrylonitrile Butadiene Styrene — engineering thermoplastic terpolymer  

<span style="color:#4FC3F7; font-weight:600;">
(C<sub>8</sub>H<sub>8</sub> · C<sub>4</sub>H<sub>6</sub> · C<sub>3</sub>H<sub>3</sub>N)<sub>n</sub>
</span>, CH2=CH–Ph + CH2=CH–CH=CH2 + CH2=CH–CN

[:material-flask-outline: ABS on PubChem](https://pubchem.ncbi.nlm.nih.gov/compound/612){ .md-button .md-button--primary target=_blank}

<div class="molecule-block">
<div id="abs_viewer" class="molecule-viewer"></div>
</div>

<script>
document.addEventListener("DOMContentLoaded", function () {
   let viewer = $3Dmol.createViewer(
    document.getElementById("abs_viewer"),
    { backgroundColor: "rgba(226,196,161,0.718)" }
    );
  $3Dmol.download("cid:7501", viewer, {}, function() {
    viewer.setStyle({}, {
        stick: {radius: 0.15},
        sphere: {scale: 0.25}});
    viewer.zoomTo();
    viewer.render();
  });
});
</script>

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

[:material-flask-outline: ASA on PubChem](https://pubchem.ncbi.nlm.nih.gov/compound/612){ .md-button .md-button--primary target=_blank}

<div class="molecule-block">
<div id="asa_viewer" class="molecule-viewer"></div>
</div>

<script>
document.addEventListener("DOMContentLoaded", function () {
   let viewer = $3Dmol.createViewer(
    document.getElementById("asa_viewer"),
    { backgroundColor: "rgba(226,196,161,0.718)" }
    );
  $3Dmol.download("cid:5280535", viewer, {}, function() {
    viewer.setStyle({}, {
        stick: {radius: 0.15},
        sphere: {scale: 0.25}});
    viewer.zoomTo();
    viewer.render();
  });
});
</script>

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