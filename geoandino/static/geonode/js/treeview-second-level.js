(function(window){

      document.querySelector( "a.toggle.toggle-nav" ).addEventListener("click",function(){
        var treeviewElements = document.querySelectorAll(".list-group-item.node-treeview");

          treeviewElements.forEach(
            function(element) {
              classie.add(element,'treeview-second-level');
            }
        );
      });


  }(window));