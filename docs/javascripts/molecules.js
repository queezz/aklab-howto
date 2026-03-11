/**
 * 3Dmol molecule viewer — compatible with Material for MkDocs instant navigation.
 * Initializes all .molecule-viewer elements on every navigation (document$).
 */
document$.subscribe(function () {
  if (typeof $3Dmol === "undefined") return;

  document.querySelectorAll(".molecule-viewer").forEach(function (el) {
    if (el.dataset.initialized) return;
    el.dataset.initialized = "true";

    const cid = el.dataset.cid;
    if (!cid) return;

    const viewer = $3Dmol.createViewer(el, {
      backgroundColor: "rgba(226,196,161,0.718)"
    });

    $3Dmol.download("cid:" + cid, viewer, {}, function () {
      viewer.setStyle({}, {
        stick: { radius: 0.15 },
        sphere: { scale: 0.25 }
      });
      viewer.zoomTo();
      viewer.render();
    });
  });
});
