document.addEventListener("DOMContentLoaded", () => {
  try {
    const elements = Array.from(document.querySelectorAll(".reveal"));
    if (!elements.length) {
      return;
    }

    if (!("IntersectionObserver" in window)) {
      elements.forEach((element) => element.classList.add("is-visible"));
      return;
    }

    const staggerStepMs = 90;
    const maxStaggerMs = 360;
    const totalElements = elements.length;
    let revealedCount = 0;

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
            revealedCount += 1;

            if (revealedCount >= totalElements) {
              observer.disconnect();
            }
          }
        });
      },
      {
        threshold: 0.18,
        rootMargin: "0px 0px -10% 0px",
      }
    );

    elements.forEach((element, index) => {
      const delayMs = Math.min(index * staggerStepMs, maxStaggerMs);
      element.style.transitionDelay = `${delayMs}ms`;
      observer.observe(element);
    });
  } catch (_) {
    document.querySelectorAll(".reveal").forEach((element) => {
      element.classList.add("is-visible");
    });
  }
});
