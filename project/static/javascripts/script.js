



var swiper = new Swiper('.swiper', {
    slidesPerView: 4.8,
    spaceBetween: 25,
    loop: true,
    fade: 'true',
    grabCursor: 'true',
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
      dynamicBullets: false,
    },
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },

   
    breakpoints:{
        0: {
            slidesPerView: 3,
            spaceBetween: 10
        },
        520: {
            slidesPerView: 2,
        },
        950: {
            slidesPerView: 4.8,
            spaceBetween: 10
        },
    },
  });


