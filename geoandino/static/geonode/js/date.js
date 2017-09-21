$( document ).ready(function() {

    var monthNames = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
      "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
    ];

      document.querySelectorAll('#dataset-info').forEach(
        function(el) {
            var d = new Date(el.innerText);
            el.innerText = d.getDay() + ' de ' + monthNames[d.getMonth()] + ' de ' + d.getFullYear();
      });
});