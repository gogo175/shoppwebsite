let menuIcon = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');

/*========== scroll sections active link ==========*/
let sections = document.querySelectorAll('section');
let navLinks = document.querySelectorAll('header nav a');

menuIcon.onclick = () =>{
  menuIcon.classList.toggle('bx-x'); 
  navbar.classList.toggle('active');
};
 window.onscroll = () => {
   sections.forEach(sec => {
      let top  = window.scrollY;
      let offset = sec.offsetTop - 150;
      let height = sec.offsetHeight;
      let id = sec.getAttribute('id');

      if(top >=  offset && top < offset + height ) {
          navLinks.forEach(links => {
            links.classList.remove('active');
            document.querySelector('header nav a[href*=' + id +']').classList.add('active');
          });
      };
   });
/*========== sticky navbar ==========*/
let header = document.querySelector('.header');

header.classList.toggle('sticky', window.scrollY > 100);

menuIcon.classList.remove('bx-x');
   navbar.classList.remove('active');
}; 

/*========== swiper ==========*/
var swiper = new Swiper(".mySwiper", {
    slidesPerView: 1,
    spaceBetween: 50,
    loop: true, 
    grabCursor:true,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });

/*========== dark light mode ==========*/

const toggleIcon = document.querySelector('.toggle-icone')

toggleIcon.addEventListener('click', () => {
    toggleIcon.classList.toggle('bx-sun');
    document.body.classList.toggle('dark-mode');
    document.toggleIcon.classList.toggle('color-mode');
});
/*========== RENVOIE DES DONNER AU BACK_END ==========*/

document.addEventListener('DOMContentLoaded', function() {
  const buttonConnecte = document.querySelector('#myButton_');

  buttonConnecte.addEventListener('click', () => {
      window.location.href = '/login_view';
  });
});


document.addEventListener('DOMContentLoaded', function() {
  const button_sinscrire = document.querySelector('#myButton');

  button_sinscrire.addEventListener('click', () => {
      window.location.href = '/user_regist_view';
  });
});



