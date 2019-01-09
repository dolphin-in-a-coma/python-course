(function($) {
    $(function() {
        function addLink() {
               var body_element = document.getElementsByTagName ('body') [0];
               var html = "";
               if (typeof window.getSelection != "undefined") {
                   var selection = window.getSelection();
                   if (selection.rangeCount) {
                       var container = document.createElement("div");
                       for (var i = 0, len = selection.rangeCount; i < len; ++i) {
                           container.appendChild(selection.getRangeAt(i).cloneContents());
                       }
                       html = container.innerHTML;
                   }
               } else {
                   return;
               }
               if (html.toString().split(' ').length < 10) {
                   return;
               }

               var pagelink = "<br/><br/> Источник: <a href='" + document.location.href+ "'>"  +document.location.href+ "</a> © Books.ru";
               var copytext = html + ' ' + pagelink;
               var newdiv = document.createElement('div');
               newdiv.style.position = 'absolute';
               newdiv.style.left = '-99999px';
               body_element.appendChild(newdiv);
               newdiv.innerHTML = copytext;
               selection.selectAllChildren(newdiv);
               window.setTimeout(function() {
                   body_element.removeChild(newdiv);
               },0);
        }
        document.oncopy = addLink;
    });
})(jQuery);