(function ($) {
  'use strict';

  var fullHeight = function () {
    $('.js-fullheight').css('height', $(window).height());
    $(window).resize(function () {
      $('.js-fullheight').css('height', $(window).height());
    });
  };
  fullHeight();

  // $(".toggle-password").click(function() {

  //   $(this).toggleClass("fa-eye fa-eye-slash");
  //   var input = $($(this).attr("toggle"));
  //   if (input.attr("type") == "password") {
  //     input.attr("type", "text");
  //   } else {
  //     input.attr("type", "password");
  //   }
  // });
})(jQuery);

const form = document.querySelector('.signin-form');

form.addEventListener('click', (e) => {
  const eye = e.target;
  if (!eye) return;
  const passwordInput = eye.previousElementSibling;
  if (!passwordInput) return;
  eye.classList.toggle('fa-eye');
  eye.classList.toggle('fa-eye-slash');

  if (passwordInput.type === 'password') passwordInput.type = 'text';
  else passwordInput.type = 'password';
});
