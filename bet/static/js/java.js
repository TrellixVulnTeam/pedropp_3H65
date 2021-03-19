
document.addEventListener('DOMContentLoaded', () => {

  // Get all "navbar-burger" elements
  const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

  // Check if there are any navbar burgers
  if ($navbarBurgers.length > 0) {

    // Add a click event on each of them
    $navbarBurgers.forEach( el => {
      el.addEventListener('click', () => {

        // Get the target from the "data-target" attribute
        const target = el.dataset.target;
        const $target = document.getElementById(target);

        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        el.classList.toggle('is-active');
        $target.classList.toggle('is-active');

      });
    });
  }

});


document.addEventListener('DOMContentLoaded', () => {
		var boton1 =  document.getElementById('boton1');
		var boton2 =  document.getElementById('boton2');
		var boton3 =  document.getElementById('boton3');
		var ventana = document.getElementById('modal1');
		boton1.onclick = function() {
			ventana.classList.toggle('is-active');
		
		};
		boton2.onclick = function() {
				ventana.classList.toggle('is-active');

		};
		boton3.onclick = function() {
				ventana.classList.toggle('is-active');

		};

		

});

document.addEventListener('DOMContentLoaded', () => {
		var boton =  document.getElementById('boton');
		var ventana = document.getElementById('modal1');
		var close = document.getElementById('del');
		var back = document.getElementById('modalback');
		var cancel = document.getElementById('cancel');
		close.onclick = function() {
			ventana.classList.toggle('is-active');
		
		};
		back.onclick = function() {
			ventana.classList.toggle('is-active');
		
		};
		cancel.onclick = function() {
			ventana.classList.toggle('is-active');
		
		};


});



document.addEventListener('DOMContentLoaded', () => {
		var desplegable =  document.getElementById('desplegable');
		desplegable.onclick = function() {
			desplegable.classList.toggle('is-active');
		
		};
		

});


function openTab(evt, tabName) {
  var i, x, tablinks;
  x = document.getElementsByClassName("content-tab");
  for (i = 0; i < x.length; i++) {
      x[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tab");
  for (i = 0; i < x.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" is-active", "");
  }
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " is-active";
}


function loadDoc(div,page) {

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById(div).innerHTML =
            this.responseText;
        }
    };
xhttp.open("GET", page, true);
xhttp.send();
}
