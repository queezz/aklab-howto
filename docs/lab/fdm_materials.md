# FDM Plastics Reference

## PLA
Polylactic Acid — polyester from lactic acid  
repeat unit `(C3H4O2)n`
https://pubchem.ncbi.nlm.nih.gov/compound/612


<div id="pla_viewer" class="molecule-viewer"></div>


| Property | Value | FDM parameter | Typical |
|---|---|---|---|
| Tg | ~60 °C | Nozzle | 190–220 °C |
| Tm | ~170–180 °C | Bed | 0–60 °C |
| Density | ~1.24 g/cm³ | Cooling | Strong |
| Strength | ~50–60 MPa | Enclosure | Not required |


<script>
document.addEventListener("DOMContentLoaded", function () {
  let viewer = $3Dmol.createViewer("pla_viewer",{backgroundColor:"gray"});
  $3Dmol.download("cid:612", viewer, {}, function() {
    viewer.setStyle({}, {stick:{}});
    viewer.zoomTo();
    viewer.render();
  });
});
</script>

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
repeat unit approximately `(C10H8O4)n`

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
(acrylonitrile + butadiene + styrene)

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
(acrylonitrile + styrene + acrylate rubber)

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