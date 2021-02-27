window.addEventListener('load',()=>{
    const preloader = document.querySelector('.preloader');
    preloader.classList.add("preload-finish");
});

const tl = gsap.timeline({ defaults: { ease: "power1.out" } });

tl.to(".some", { y: "0%", duration: 2, stagger: 1.25 });
tl.to(".slider", { y: "-100%", duration: 1.5, delay: 0.5 });
tl.to(".intro", { y: "-100%", duration: 1 }, "-=1");