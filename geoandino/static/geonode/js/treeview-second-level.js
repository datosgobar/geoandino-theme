(function(window){

      document.querySelector( "a.toggle.toggle-nav" ).addEventListener("click",function(){
        var treeviewElements = document.querySelectorAll("span.indent");

          treeviewElements.forEach(
            function(element) {
              classie.add(element.parentNode,'treeview-second-level');
            }
        );
      });


  }(window));