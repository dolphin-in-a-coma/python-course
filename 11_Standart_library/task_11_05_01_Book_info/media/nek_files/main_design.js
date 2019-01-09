var is_ie6 = false;
var is_ie7 = false;
jQuery.each(jQuery.browser, function(i, val) {
     if(i=="msie" && jQuery.browser.version.substr(0,3)=="6.0"){is_ie6 = true;}
     if(i=="msie" && jQuery.browser.version.substr(0,3)=="7.0"){is_ie7 = true;}
});

preloadImages=function(){
for(var i=0;i<arguments.length;i++) {
     jQuery('<img>').attr('src',arguments[i]);;
}
}

$(function() {
    var img_bg_4 = document.createElement("img");
    img_bg_4.src = "/static/images/bg-img-4.png";
    document.body.appendChild(img_bg_4);
});


function setCookie (name, value, expires, path, domain, secure) {
      document.cookie = name + "=" + escape(value) +
        ((expires) ? "; expires=" + expires : "") +
        ((path) ? "; path=" + path : "") +
        ((domain) ? "; domain=" + domain : "") +
        ((secure) ? "; secure" : "");
}

function initTabs() {
          $('div.tabs a').click(function(){
               if ($(this).parents('.tabs').hasClass('not-changeble')) {
                    return true;
               }
               tabIndex = $('div.tabs a').index(this);
               newTab = $('div.tab')[tabIndex];
               newLink = $('div.tabs table td')[tabIndex];
               
               if($.browser.opera){
                    $('div.tabs table tbody tr td').css({'border-bottom':'none','padding-bottom':'1px'});
               }
               $('div.tabs table td').removeClass('selected');
               $(newLink).addClass('selected');
               
               if($.browser.msie){
                    $('div.tab:visible').fadeOut(0, function(){
                         $(newTab).fadeIn(0);
                    });
               } else {
                    $('div.tab:visible').fadeOut(300, function(){
                         $(newTab).fadeIn(300);
                    });
               }
               return false;
          });
}

function sliderItemAutoWidth() {
     var elem = $('div#slider')
     containerWidth = elem.parent().width()  + "px"; // -51 
     elem.css({'width':containerWidth});
     sliderWidth = elem.width();
     if (sliderWidth < 640) {
          $('table.slider td', elem).css({'width':'153px','min-width':'153px','max-width':'153px'});
     } else {
          $('table.slider td', elem).css({'width':'170px','min-width':'170px','max-width':'170px'});
     }
}
     
function initSlider() {
     var elem = $('div#slider');
	 elem.css({'width':'458px'});
	 sliderItemAutoWidth();     
     
     $(window).resize(function() {
          elem.css({'width':'458px'});
          sliderItemAutoWidth();
     });


     var moving = false;
     var count_moved = 0;
     
     function sliderMove(dir, elem) {   
          if(moving) return;
          
          var  slider         = $('table.slider',  $(elem).parent());
          var  margin         = parseInt(slider.css('margin-left'));
          if(isNaN(margin)) {
               margin = 0;
          }
          
          var  slider_width  = parseInt(slider.parent().width());
          var  td_count       = $('table.slider .cover td').length;
          var  td_width       = parseInt($('td', slider).css('width'));
          
          var  td_count_visible     = Math.round(slider_width / td_width);
          
          
          $('.slider-left').show();
          $('.slider-right').show();

          if(dir=='+' && count_moved==0) {
                return false;
          }
         
          if(dir=='-' && count_moved+td_count_visible==td_count) {
                return false;
          }

          moving = true;
          $('table.slider',  $(elem).parent()).animate({
               'margin-left': (margin + parseInt(dir + td_width)) + 'px'
          }, 'slow', function() {
               moving = false;
               count_moved  = count_moved - parseInt(dir+1)
               
               if(dir=='+' && count_moved==0) {
                     $('.slider-left').hide();
               }
               if(dir=='-' && count_moved+td_count_visible==td_count) {
                     $('.slider-right').hide();
               }
               
          });
          
     }
     
     $('table.slider',elem).each(function() {
          var  slider         = $(this);
          var  td_count       = $('.cover td', slider).length;
          
          var  slider_width  = parseInt(slider.parent().width());
          var  td_width       = parseInt($('td', slider).css('width'));
          
          var  td_count_visible     = Math.round(slider_width / td_width);
          
          $('.slider-left').hide();
          if(td_count<=td_count_visible) {
               $('.slider-right').hide();
          }
          else  {
               $('.slider-right').show();
               return false;
          }

          
          var offset = (slider_width - td_width*td_count)/2+10;
     
          //slider.css('margin-left', offset+'px')
     })
     
     $('.slider-left').click(function() {
          sliderMove('+', this);
     })
     $('.slider-right').click(function() {
          sliderMove('-', this);
     })
};


          
var catalog = {
          
          delCategory: function(obj) {
               if(confirm('Вы действительно хотите скрыть категорию? ')) {
                    var id = $(obj).parents('.cat')[0].id.replace('cat-block-id-',"");
                    
                    this.hideCategory(id);
               }
          },
          
          checkCategory: function(obj) {    
                    var id = obj.id.replace('cat-list-row-',"");
               
                    $(obj).find('input').val()==0 ? this.showCategory(id):this.hideCategory(id);
          },

          hideCategory:function(id) {
               $('#cat-block-id-'+id).fadeOut(250);
               //alert(id)
               $('#cat-list-row-' + id).show();
               $('#cat-list-row-' + id +' input').val(0);

          },
          
          showCategory:function(id) { 
               $('#cat-block-id-'+id).fadeIn(250);
               
               $('#cat-list-row-' + id).hide();
               $('#cat-list-row-' + id +' input').val(1);

          },
          
          changeColor:function(el) {
               
               $(el).parent().find('li').removeClass('selected');
               $(el).addClass('selected');
               color = $(el).find('span').html();
               $(el).parent().parent().parent().css({'border-top-color':"#" + color});

               var input = $('.cat-block-color', $(el).parents('.cat'))
               
               input.val(color);
               
          },
          save: function(){
               
               $('#cat-sort').val( ($('.categories .block').sortable( 'serialize'  , {'key':'', 'expression':/(cat)[\-block]+(.+)/})) )
               return true;
          }, 
          
          defaultList: function() {
               var a =  this.defaultListArr ;
               
               for(var i in a) {
                    var v =  a[i][0]; 
                    
                    if(v==1)   {
                         this.showCategory(i);
                    }    
                    else {
                         this.hideCategory(i);
                    }
               } return false;
          },
          
          
          defaultColor: 'd0d9dd',
          
          defaultAll: function() {
               var a1 =  this.defaultListArr ;
               var k = '#cat-block-subrow-';
               
               var el, a2;
               for(var id in a1) {
                    this.showCategory(id);
                    el = $('#cat-block-id-'+id);
                    
                    a2 =  this.defaultListArr[id];
                    
                    for(var id2 in a2) {
                              $(k+id2).prop('checked', 'checked');
                    } 
                    
                    $('#cat-block-id-'+id + ' .block-params').css({'border-top-color':"#" + this.defaultColor});
                    $('#cat-block-id-'+id+' .cat-block-color').val( this.defaultColor );
               } 
               
               return false;
          },
          defaultBlock: function( el) {
               var id = el.id.replace("cat-block-default-",'')
               var a =  this.defaultListArr[id];
               var k = '#cat-block-subrow-';
         
               for(var i in a) {
                    var v = a[i]; 
                    
                    
                    if(v==1)   {
                         $(k+i).prop('checked', 'checked');
                    }    
                    else {
                         $(k+i).removeAttr('checked')
                    }
                    
                    
               } 
               
               $('#cat-block-id-'+id + ' .block-params').css({'border-top-color':"#" + this.defaultListColors[id]});
               
               $('#cat-block-id-'+id + ' .colors li').removeClass('selected');
               $('#cat-block-id-'+id + ' .cat-colors-'+this.defaultListColors[id]).addClass('selected');

               $('#cat-block-id-'+id+' .cat-block-color').val(this.defaultListColors[id]);
               
               return false;
          }
};
     
     
function catalogcatWidth()
{
          containerWidth = $('div.categories').width();
          categoryBlockWidth = (containerWidth / 2) - 6 + "px";
          $('div.cat').each(function(){
               $(this).css({'width':categoryBlockWidth});
          });
}   

function process_filters(base_url)
{
    var s = base_url.indexOf("?")==-1 ? "?":'&';
    
    var url = [];
          
      $('#listing-filter-select select, #listing-filter-select input').each(function() {
           url.push(this.name + '=' + this.value);
           base_url = base_url.replace(this.name, '_remove_');
      });
      
      var tmp = $('#listing-filter-tabs .selected')[0];
      if(tmp) {
           url.push( 'type='+ tmp.className.replace('selected', '').replace('last', '') );
      }

      base_url = base_url.replace(/_remove_[^&]*/gi, '').replace(/&&+/g, '').replace(/&+$/g, '');

      location.href = base_url+ s + url.join('&');
}
     
var initSubCategoryFilters = function(base_url) 
{  
     
     
     $('#listing-filter-select select').on('change', function(e) {
          process_filters(base_url);
     });
     
     $('#filter_img_find').on('click', function(e) {
          process_filters(base_url);
     });

     var tmp_url = [];
     $('#listing-filter-select select,#listing-filter-select input').each(function() {
          tmp_url.push( this.name + '=' + this.value );
     });
     $('#listing-filter-tabs a').each(function(i) {
          if(i==0) 
          {
               $(this).attr('href',base_url);
          }
          else
          {
               $(this).attr('href', this.href+'&'+tmp_url.join('&'))
          }
     });  
}


function initToggle() {
          $('ul.toggle a:first').click(function(){
               $(this).parent().removeClass('first').removeClass('first-selected').addClass('first-selected');
               $('ul.toggle a:last').parent().removeClass('second').removeClass('second-selected').addClass('second');
               return false;
          });
          $('ul.toggle a:last').click(function(){
               $(this).parent().removeClass('second').removeClass('second-selected').addClass('second-selected');
               $('ul.toggle a:first').parent().removeClass('first').removeClass('first-selected').addClass('first');
               return false;
          });
          $('div.advanced-search ul.toggle a:first').click(function(){
               if (is_ie6 || is_ie7) {
                    $('div.advanced-search .invisible').css({'display':'none'});
               } else {
                    $('div.advanced-search .invisible').slideUp(400);
               }
               $("#scope")[0].value='everywhere';
          });
          $('div.advanced-search ul.toggle a:last').click(function(){
               if (is_ie6 || is_ie7) {
                    $('div.advanced-search .invisible').css({'display':'block'});
               } else {
                    $('div.advanced-search .invisible').slideDown(400);
               }
               $("#scope")[0].value = 'types';
          });
          if (window.Context && (Context.scope == 'types'))
          {
               $('div.advanced-search ul.toggle a:last').click();
          }
}

function initHint() {
        if($('.hint').length==0)  return;
          
        hintCorners = '<span class="tl"></span><span class="tr"></span><span class="bl"></span><span class="br"></span>';
        $('span.hint').append(hintCorners);
          
        $('a.hint, ul.hint').mouseenter(function(e){
                           
            $('<span />')
            .attr({
                "class" : 'hint bodyhint'
            })
            .html( $(this).next('span.hint').html() )
            .appendTo('body');
                        
            var hint = $("body span.bodyhint");
            var border_top = $(window).scrollTop();
            var border_right = $(window).width();
			var left_pos;
			var top_pos;
			var offset = 10;
			
            if(border_right - (offset *2) >= hint.innerWidth() + e.pageX){
				left_pos = e.pageX+offset;
			} else{
				left_pos = border_right-hint.innerWidth()-offset;
			}

			if(border_top + (offset *2)>= e.pageY - hint.innerHeight()){
				top_pos = border_top +offset;
			} else{
                top_pos = e.pageY-hint.innerHeight()-offset;
			}

			hint.css({'display':'block'});
            hint.css({left:left_pos, top:top_pos});
    
        });
        $('a.hint, ul.hint').mouseleave(function(){
            $("body span.bodyhint").remove();            
        });
        $('span.hint').mouseenter(function(){
            $(this).css({'display':'block'});
        });
        $('span.hint').mouseleave(function(){
            $(this).css({'display':'none'});
        });
}


function initImgHover() {
          $('img.hover').mouseenter(function(){
               img_src = $(this).attr('src');
               ext = img_src.split('.').pop();
               img_src_tmp = img_src.slice(0, -(ext.length + 1));
               img_src_hover = img_src_tmp + '-hover.' + ext;
               $(this).attr('src', img_src_hover);
          });
          $('img.hover').mouseleave(function(){
               img_src = $(this).attr('src');
               ext = img_src.split('.').pop();
               img_src_tmp = img_src.slice(0, -(ext.length + 7));
               img_src_hover = img_src_tmp + '.' + ext;
               $(this).attr('src', img_src_hover);
          });
          

}

var preloadImages=function(){
     for(var i=0;i<arguments.length;i++) {
          jQuery('<img>').attr('src',arguments[i]);;
     }
}

var Preloader = function(e, parent) {
     var elem =  e;
    
    
     return {
          show: function() {
               elem.show();
          }    ,
          hide: function() {
               elem.hide();
          }   
          
     }
}


var map;
function GMapInit(options) {
      if (GBrowserIsCompatible()) {
          map = new GMap2(document.getElementById("map_canvas"));
          map.setCenter(new GLatLng(options.lat, options.lng), 11);
          map.setUIToDefault();
     }
     window.onunload = GUnload;
}  
function GMapCreateMarker(point, fio, url, avatar) 
{
     var marker = new GMarker(point, {});
          
     GEvent.addListener(marker, "click", function() {
         marker.openInfoWindowHtml("<img src='"+avatar+"' style='float:left;margin-right:10px'> <a href='"+url+"'>" + fio + "</a>");
     });  
     return marker; 
}
function YMapInit(options) {
         map = new YMaps.Map(document.getElementById("map_canvas"));
         map.setCenter(new YMaps.GeoPoint(options.lng, options.lat), 10);
         map.addControl(new YMaps.Zoom());
         map.addControl(new YMaps.MiniMap());
         map.addControl(new YMaps.TypeControl());
         map.addControl(new YMaps.ScaleLine());

         var u_style = new YMaps.Style();
         u_style.iconStyle = new YMaps.IconStyle();
         u_style.iconStyle.href = "pages/static/images/user-13.png";
         u_style.iconStyle.size = new YMaps.Point(38, 39);
         u_style.iconStyle.offset = new YMaps.Point(0, 0);
      
         window.onunload = map.destructor;
}  
function YMapCreateMarker(lat, lng, fio, url, avatar, def_style, interests, trader_info)
{
      interests = typeof interests !== 'undefined' ? interests : '';
      trader_info = typeof trader_info !== 'undefined' ? trader_info : '';
      
      var point = new YMaps.GeoPoint(lng,lat);
      var placemark = new YMaps.Placemark(point, {style: def_style});
      //map.addOverlay(placemark);
      //placemark.name = fio;
      placemark.description = "<div style='width:300px'><a href='"+url+"'> <img src='"+avatar+"' style='float:left;margin-right:10px'> </a> <a target='_blank' href='"+url+"'>" + fio + "</a>";
      if (interests) placemark.description += "<br><br>"+interests
      if (trader_info) placemark.description += "<br><br>"+trader_info
      placemark.description += "</div>"
      
         //  var marker = new GMarker(point, {});
          
     //GEvent.addListener(marker, "click", function() {
     //                    marker.openInfoWindowHtml("<img src='"+avatar+"' style='float:left;margin-right:10px'> <a href='"+url+"'>" + fio + "</a>");
     //});  
     return placemark; 
}


function init_debug()
{
     $(document).keydown(function(event){
          if (event.keyCode == 192)
          {
               $('#debug-block').toggle();
          }
        }
     );
     $('.debug-hide').click(function(){$('#debug-block').hide();});
     $('#debug-show').click(function(){$('#debug-block').show()});
}

function init_system_default() 
{
     
}

function initLeftSubmenu() 
{
          var curLI;
          var ieTimeout;
          if (!$('body').hasClass('home-page')) {
               mouseEnter2 = false;
               $('div.main-menu ul li.catalog').mouseenter(function(){
                    $('div.submenu').css({'display':'block'});
               });
               $('div.main-menu ul li.catalog').mouseleave(function(){
                    $('div.submenu').css({'display':'none'});
               });
               $('div.submenu').mouseenter(function(){
                    mouseEnter2 = true;
                    $(this).css({'display':'block'});
               });
               $('div.submenu').mouseleave(function(){
                    if (is_ie6 || is_ie7) {
                         if (!ieTimeout) {
                              mouseEnter2 = false;
                              $(this).css({'display':'none'});
                         }
                    } else {
                         mouseEnter2 = false;
                         $(this).css({'display':'none'});
                    }
               });
          }

          //hover
          var mouseEnter = false;
          var hp = true;
          if ($('div.submenu').css('display') != 'block') {
               hp = false;
               $('div.submenu').css({'display':'block','visibility':'hidden'});
          }
          $('div.submenu ul li').each(function(){
               liHeight = $(this).height();
               if (liHeight > 0) {
                    if (is_ie7) {
                         liHeight = liHeight - 3;
                    }
                    $(this).css({'height':liHeight});
               }
          });
          if (!hp) {
               $('div.submenu').css({'visibility':'visible','display':'none'});
          }
          $('div.submenu ul li').mouseenter(function(){
               //$('div.submenu ul li ul').css({'display':'none'});
               dropdownExist = $(this).find('ul').html();
               if ($(this).height() > 33 && $(this).height() < 48) {
                    $(this).addClass('h2');
               } else if ($(this).height() > 47 && $(this).height() < 62) {
                    $(this).addClass('h3');
               } else if ($(this).height() > 61) {
                    $(this).addClass('h4');
               }
               if (dropdownExist) {
                    $(this).find('ul li:first').addClass('first');
                    $(this).addClass('hovered');
                    $(this).find('ul').css({'display':'block'});
                    if (is_ie6 || is_ie7) {
                         liWidth = $(this).find('ul li').width() + "px";
                         $(this).find('ul a').css({'width':liWidth});
                         curLI = $(this).html();
                         if (!$('body').hasClass('home-page')) {
                              smWidth = 230 + $(this).find('ul').width();
                              $('div.submenu').css({'width':smWidth});
                         }
                    }
               } else {
                    if ($(this).parent().parent().hasClass('submenu')) {
                         curLI = $(this).html();
                    }
               }
          });
          $('div.submenu ul li').mouseleave(function(){
               if ($(this).parent().parent().hasClass('submenu')) {
                    curLI = false;
               }
               if (!mouseEnter) {
                    dropdownExist = $(this).find('span.dropdown').html();
                    $(this).removeClass('h2');
                    $(this).removeClass('h3');
                    $(this).removeClass('h4');
                    $('div.submenu').css({'width':'190px'});
                    if (dropdownExist) {
                         $(this).find('ul').css({'display':'none'});
                         $(this).removeClass('hovered');
                    }
               }
          });
          if (is_ie6 || is_ie7) {
               if ($('body').hasClass('home-page')) {
                    smIeFix = '<span class="smIeFix"></span>';
                    //$('div.submenu').append(smIeFix);
               }
          }
          var ieTimeout;
          $('span.dropdown').mouseenter(function(){
               mouseEnter = true;
          });
          $('span.dropdown').mouseleave(function(){
               if (!is_ie6 && !is_ie7) {
                    mouseEnter = false;
               }
          });
          if (is_ie6 || is_ie7) {
               $('div.submenu ul li ul').mouseenter(function(){
                    mouseEnter = true;
                    $(this).css({'display':'block'});
                    if (ieTimeout) {
                         window.clearTimeout(ieTimeout);
                    }
               });
               $('div.submenu ul li ul').mouseleave(function(){
                    selectedUL = $(this);
                    selectedLI = $(this).parent().parent().parent().parent().parent();
                    ieTimeout = window.setTimeout(function() {
                         mouseEnter = false;
                         if (curLI != selectedLI.html()) {
                              selectedUL.css({'display':'none'});
                              selectedLI.removeClass('hovered');
                              $('div.submenu').css({'width':'190px'});
                              window.clearTimeout(ieTimeout);
                         }
                    }, 150);
               });
          }

}

function initTopRegion() {
     // Regions
     mouseEnterRegion = false;
     
     var mouseEnterRegionSelect =  false;
     
     var timer = false;
     
     var timeout = null;
     
     function checktimer() {
          if(timer) clearTimeout(timer);
     }
     
     $('.region').click(function(){
          mouseEnterRegionSelect = false;
          //checktimer();
          $('div.menu_region').css({'display':'block'});
     });
     
     $('.region').mouseleave(function(){
          //$('div.menu_region').css({'display':'none'});
     });
     
     $('.operator').click(function(){
          mouseEnterRegionSelect = false;
          $('div.menu_region').css({'display':'block'});
          return false;
     });
     $('div.menu_region').mouseenter(function(){
          mouseEnterRegionSelect = false;
          mouseEnterRegion = true;
          //checktimer();
          if (timeout) clearTimeout(timeout);
          $(this).css({'display':'block'});
     });
     
     $('#header_region_other_wrapper select').mouseover(function(){
          mouseEnterRegionSelect = 1;
     });
     
     
     
     $('div.menu_region').mouseleave(function(){
          var self = this;
          //alert(mouseEnterRegionSelect);
          
          // hack for ie
          //if(!mouseEnterRegionSelect) $(self).css({'display':'none'});
           timeout = setTimeout(closeregion, 1000);    
               
     });
     
     function closeregion() {
        if(!mouseEnterRegionSelect) $('div.menu_region').css({'display':'none'});
        if (timeout) clearTimeout(timeout);
    }

     if (window.location.hash=='#regions') $('div.menu_region').css({'display':'block'});
     
}



function initTopMyBooks()
{
     // Mybooks
     mouseEnterMyBooks = false;
     $('img.mybooks').mouseenter(function(){
          $('div.mybooks').css({'display':'block'});
          $('img.mybooks').css({'display':'none'});
     });
     $('img.mybooks').mouseleave(function(){
          $('div.mybooks').css({'display':'none'});
          $('img.mybooks').css({'display':'block'});
     });
     $('div.mybooks').mouseenter(function(){
          mouseEnterMyBooks = true;
          $(this).css({'display':'block'});
          $('img.mybooks').css({'display':'none'});
     });
     $('div.mybooks').mouseleave(function(){
          mouseEnterMyBooks = false;
          $(this).css({'display':'none'});
          $('img.mybooks').css({'display':'block'});
     });
}


function initTopSearch() {
     // Eyes opacity in search field
     $('div.look-inside div.book-search input.submit').fadeTo(0, 0.4);
     $('div.search div.field input.submit').fadeTo(0, 0.4);
     $('div.search div.field input.submit').mouseenter(function(){
          $(this).fadeTo(0, 1);
     });
     $('div.search div.field input.submit').mouseleave(function(){
          $(this).fadeTo(0, 0.4);
     });
     $('div.look-inside div.book-search input.submit').mouseenter(function(){
          $(this).fadeTo(0, 1);
     });
     $('div.look-inside div.book-search input.submit').mouseleave(function(){
          $(this).fadeTo(0, 0.4);
     });

}

function initautoLabel() {
     // Auto hide/show label on text field
     $('.autolabel').focus(function () {
          if ($(this).prop('defaultValue') && $(this).prop('defaultValue') == $(this).val()) {
               $(this).val('')
          }
     });
     $('.autolabel').blur(function () {
          if ($(this).prop('defaultValue') && $(this).val() == '') {
               $(this).val($(this).prop('defaultValue'));
          }
     });
}


function submitHeaderRegionOther() {
     $('#header_region_form').submit();
}

function initHeaderRegionOther() {
     $('#header_mainregion_trigger').click(function(){
          if( $(this).hasClass('selected') ) {
               $(this).removeClass('selected');
               $('#header_region_other_wrapper').removeClass('selected');
          }
          else {
               $(this).addClass('selected');
               $('#header_region_other_wrapper').addClass('selected');
          }
     })
    
     $('.menu_region .menu_region_close').click(function(){
          $('.menu_region').hide();
     })
     
     $('#header_mainregion_other2').change(function(){
          submitHeaderRegionOther();
     })
     
     
     
     $('#header_mainregion_other').change(function(){
          var value = this.value;
          $('#header_mainregion_other2').hide();;
       
          if(value==-1) {
               return;
          }
          
          if(value==271 || value==304) {
                submitHeaderRegionOther(); 
                
                return;
                
          }
          
          mouseEnterRegion = true;
          $.post( '/member/ajax/get_regions_by_prnt.php', {parent:value}, function(d) {
               d = eval('('+d+')');
               
               var select = $('#header_mainregion_other2'); 
               var selected = false;
               select.html( '<option value=1>не выбрано</option>');
               for(var i in d) {
                    selected = header_region_sub_id == d[i].id ? 'selected':'';
                    select.append('<option value="'+d[i].id+'" '+selected+'>'+d[i].ru_name+"</option>");
               }
              
               select.show();
               mouseEnterRegion = false;
               
               if(header_region_show) {
                    $('div.menu_region').css({'display':'block'});
               }    
               else {
                    header_region_show = true;
               } 
          });
     });
     
     var header_region_show = true;
     if( $('#header_mainregion_other').val() == 1 || $('#header_mainregion_other').val() == 0 )  {
          header_region_show = false;
          $('#header_mainregion_other').trigger('change');
     }
}

function someFixes() 
{
     if($.browser.mozilla){
          $('div.cat table a').css({'background-position':'0 4px'});
          $('div.expanded table a').css({'background-position':'0 5px'});
     }
     
     if (!is_ie6 && !is_ie7) {
          $('div.big-user-info div.userpic').append($('td.left-block img.bow'));
     } else {
          imgHeight = $('div.big-user-info div.userpic img').height() + 4;
          bowTop = "438px";
          if (imgHeight < 197) {
               imgDiff = 197 - imgHeight;
               bowTop = 438 - imgDiff + "px";
          } else if (imgHeight > 197) {
               imgDiff = imgHeight - 197;
               bowTop = 438 + imgDiff + "px";
          }
          $('td.left-block img.bow').css({'top':bowTop});
     }

}


$(document).ready(function() {
     
     initLeftSubmenu() ;

     initTopMyBooks();
     
     initTopSearch();
     
     initTopRegion();
     
     initautoLabel();
     
     someFixes();

     initHint();

     preloadImages(
               '/static/images/buttons/tobasket-hover.gif',
               '/static/images/buttons/tobasket-mini-hover.gif'
     );
     
     initImgHover();
     
     initHeaderRegionOther();

     init_1click();

     init_debug();
     eval(init_function);
     
     submenu();
});

function init_1click() {
     $('.order_one_click').click(function() {
          var t = confirm('Нажмите Ok, если Вы хотите осуществить заказ в 1 клик. Все содержимое корзины и этот товар будут помещены в заказ, который немедленно будет оформлен. При расчете стоимости доставки будет учтен ваш основной адрес');
          
          return t;
     });
     initSlider();
}



function initPageMain() {
     initTabs();
     initSlider();
}

function initPageCustomerProductPremium() {
     initPagePremiumDates();
     
     $("input[name='premium_from']").change(function(){
          calc_premium_price();
     })
     
     $("input[name='premium_to']").change(function(){
          calc_premium_price();
     })
}

function isValidDate(dateString) {
  var regEx = /^\d{2}\.\d{2}\.\d{4}$/;
  return dateString.match(regEx) != null;
}

function calc_premium_price() {
    if ( isValidDate($("input[name='premium_from']").val()) && isValidDate($("input[name='premium_to']").val())) {
        // end - start returns difference in milliseconds 
        
        var from = $("input[name='premium_from']").val().split(".");
        var f_from = new Date(from[2], from[1], from[0]);
                              
        var to = $("input[name='premium_to']").val().split(".");
        var f_to = new Date(to[2], to[1], to[0]);
        
        var diff2 =  f_to - f_from;
        if (diff2 >= 0 ) {
            // get days
            var days2 = diff2/1000/60/60/24 + 1;
            
            var summ = days2 * premium_price_per_day
            $(".price_premium").html(summ);
            
            if (summ <= account_money) {
                $(".price_premium_alert").hide();
                $(".bt").show();
            }
            else {
                $(".price_premium_alert").show();
                $(".bt").hide();
            }
        } else {
            alert('Дата окончания не может быть меньше, чем дата начала'); 
            $("input[name='date_to']").val('');
        }
    }
}

function initPagePaidInsale() {
          
     $("select[name='insale_pack_cnt']").change(function(){
          calc_paid_insale_price();
     })
     
     $("select[name='insale_pack_days']").change(function(){
          calc_paid_insale_price();
     })
}

function calc_paid_insale_price() {
    if ( $("select[name='insale_pack_cnt']").val() && $("select[name='insale_pack_days']").val()) {                                     
            
            $.post( '/ajax/get_insale_pack_summ.php', { days: $("select[name='insale_pack_days']").val(), cnt: $("select[name='insale_pack_cnt']").val() })
              .done(function( data ) {
                    var summ = data
                    $(".price_premium").html(summ);
                    
                    if (summ <= account_money) {
                        $(".price_premium_alert").hide();
                        $(".bt").show();
                    }
                    else {
                        $(".price_premium_alert").show();
                        $(".bt").hide();
                    }
              });        
    }
}

function initPage404() {
     initTabs();
}

function initPageCat() {
     initSlider();


     $('.cat table a').click(function(e) {
          e.stopPropagation()
          return true;
     });
     $('.cat table').click(function() {
          if ($(this).parents('.cat').hasClass('expanded')) {
               $(this).parents('.cat').removeClass('expanded');
          } else {
               $(this).parents('.cat').addClass('expanded');
          }
     });
     
     catalogcatWidth();
     
     $(window).resize(function() {
          catalogcatWidth()
     });


}

function initPageInobookCat() {
     $('.cat table a').click(function(e) {
          e.stopPropagation()
          return true;
     });
     $('.cat table').click(function() {
          if ($(this).parents('.cat').hasClass('expanded')) {
               $(this).parents('.cat').removeClass('expanded');
          } else {
               $(this).parents('.cat').addClass('expanded');
          }
     });
     
     catalogcatWidth();
     
     $(window).resize(function() {
          catalogcatWidth()
     });


}

var checking_price=0
var int_price=0;
var int_price;

function check_price(format, sub) {
		
        if (checking_price==0)
        {
            int_price = setInterval("check_price('"+format+"', "+sub+")", 5000);
            checking_price=1
            
            if (format=='xls')
            {
                $('#container_price_xls').append('<img src="/static/images/price_loader.gif" alt=Загрузка..." id="loading_xls" />');
                $('#link_price_xls').addClass('link_price_loading');

            }
            if (format=='xml')
            {
                $('#container_price_xml').append('<img src="/static/images/price_loader.gif" alt=Загрузка..." id="loading_xml" />');
                $('#link_price_xml').addClass('link_price_loading');
            }
        }
        
        $.ajax({
				url: '/price_main.php',
				type: 'GET',
                dataType: 'json',
				data: 'format=' + format + '&sub=' + sub + '&t=' + (Math.random() * (10000000 - 1) + 1),
 
				success: function(data) {
                    
                    if (data.status!='ready') return;
                    clearInterval(int_price);
                    checking_price=0
                    
                    if (format=='xls') 
                    {
                        $('#loading_xls').fadeOut(500, function() {
                                $(this).remove();
                            });
                        $('#link_price_xls').removeClass('link_price_loading');
                    }
                    else if (format=='xml') 
                    {
                        $('#loading_xml').fadeOut(500, function() {
                                $(this).remove();
                            });
                        $('#link_price_xml').removeClass('link_price_loading');
                    }
                    if (data.status=='ready') 
                    {
                        if (sub=='160382') alert("Готово!");
                        else window.location.href=data.url;
                    }
                }
			});	
}


var checking_order=0
var int_order=0;
var int_order;

function update_dostup(num) {
		
        if (checking_order==0)
        {
            int_order = setInterval("update_dostup('"+num+"')", 5000);
            checking_order=1
            
            $('#container_update_dostup').append('<img src="/static/images/price_loader.gif" alt=Загрузка..." id="loading_dostup" />');
            $('#link_update_dostup').addClass('link_price_loading');
        }
        
        $.ajax({
				url: '/member/ajax/order/update_product_dostup_main.php',
				type: 'GET',
                dataType: 'json',
				data: 'order_id=' + num + '&t=' + (Math.random() * (10000000 - 1) + 1),
 
				success: function(data) {
                    
                    if (data.status!='ready') return;
                    clearInterval(int_order);
                    checking_order=0
                    

                    $('#loading_dostup').fadeOut(500, function() {
                                $(this).remove();
                            });
                    $('#link_update_dostup').removeClass('link_price_loading');
                    
                    if (data.status=='ready') 
                    {
                        window.location.href = window.location.href;
                    }
                }
			});	
}

var mail_generating=0
var int_generate=0;
var int_generate;

function mail_generate(id, add, obj) {
		
        if (!add) add= ''
		if (mail_generating==0)
        {
            int_generate = setInterval("mail_generate('"+id+"', '"+add+"')", 5000);
            mail_generating=1
            
                $(obj).parents('.sortable-item').find('.container_loading').append('<img src="/static/images/price_loader.gif" alt=Загрузка..." id="loading_process" />');
                $(obj).parents('.sortable-delete').hide();
        }

        $.ajax({
				url: '/site-admin/mail/generate'+add+'.php',
				type: 'GET',
				data: 'generate'+add+'=' + id + '&t=' + (Math.random() * (10000000 - 1) + 1),
 
				success: function(data) {
                    if (data!='ready') return;
                    clearInterval(int_generate);
                    mail_generating=0
                    

                    $('#loading_process').fadeOut(500, function() {
                                $(this).remove();
                            });
                    $(obj).parents('.sortable-delete').show();
                    
                    if (data=='ready') 
                    {
                        alert('готово!')
						window.location.href = window.location.href
                    }
					
					
                }
			});	
}


function initPageSubCatalog() {
     initTabs();
     initSlider();
     
     
}

function initPageCatalogEdit() {

     $(".categories .block").sortable({});
     $(".categories .block").disableSelection();
     
     
     $(".cat img.cat-close").click(function() {catalog.delCategory(this)});
     
     $(".cat ul.colors li").click(function() {catalog.changeColor(this)});
     
     
     $(".cat-list-row a").click(function() {catalog.checkCategory(this.parentNode);return false;});

     $(".cat-list-default").bind('click',  function() {catalog.defaultList(this);return false;});
     $(".cat-block-default").bind('click', function() {catalog.defaultBlock(this);return false;});
     $(".cat-all-default").bind('click', function() {catalog.defaultAll(this);return false;});

     $('.cat table a').click(function() {
          if ($(this).parents('.cat').hasClass('expanded')) {
               $(this).parents('.cat').removeClass('expanded');
          } else {
               $(this).parents('.cat').addClass('expanded');
          }
          return false;
     });
     $('.cat table').dblclick(function() {
          if ($(this).parents('.cat').hasClass('expanded')) {
               $(this).parents('.cat').removeClass('expanded');
          } else {
               $(this).parents('.cat').addClass('expanded');
          }
     });
     
     $('.cat ul.colors li').each(function(){
          color = "#" + $(this).find('span').html();
          $(this).css({'background':color});
          if ($(this).hasClass('selected')) {
               $(this).parent().parent().parent().css({'border-top-color':color});
          }
     });
     
     catalogcatWidth();
     
     $(window).resize(function() {
          catalogcatWidth()
     });
}
    
function initPageComments() {   
     $('.comment_rating').bind('click', commentSaveRating );
}  

function initPageProduct() {
     initTabs();
     initSlider();

     $('#item_desc_show').click(function() {
          $(this).hide();
          $('#item_desc_hidden').show();
          $('#item_desc_end').hide();
          return false;
     })
                
     $('#item_desc_hide').click(function() {
          $('#item_desc_show').show();
          $('#item_desc_hidden').hide();
          $('#item_desc_end').show();
          return false;
     })
                

     var LI  = lookInside();
          
     initPageComments();
     
     initProductSendToFriend();
     
     initTinyMCE({
          "mode":"exact",
          "element":"comment_textarea",
          'edSettings':edSettings
     });
 
    $(".input_any_price").keydown(function(e) {

        if (e.shiftKey || e.ctrlKey || e.altKey) { // if shift, ctrl or alt keys held down 
            e.preventDefault();         // Prevent character input 
        } else { 
            var n = e.keyCode; 
            if (!((n == 8)              // backspace 
            || (n == 46)                // delete 
            || (n == 190)               // dot 
            || (n >= 35 && n <= 40)     // arrow keys/home/end 
            || (n >= 48 && n <= 57)     // numbers on keyboard 
            || (n >= 96 && n <= 105))   // number on keypad 
            ) { 
                e.preventDefault();     // Prevent character input 
            } 
        }
    });
                
    var window_once_showed = 0
    $('a#add_to_cart').click(function() {
                
        if (window_once_showed != 1 && editionpage)
        {
            window_once_showed = 1
            popupwindow('Вы собираетесь положить в корзину одно из изданий произведения «'+product_title+'». Пожалуйста, перед оформлением заказа в корзине проверьте, что вам нужно именно это издание.<br><br>Для продолжения кликните «В корзину» еще раз.')
            return false;
        }
        
        if (window_once_showed != 1 && demandpage)
        {
            window_once_showed = 1
            popupwindow('Внимание! Книга печатается по технологии Print-On-Demand (печать по требованию), поэтому полиграфия может отличаться от оригинального издания.<br><br>Для продолжения кликните «В корзину» еще раз.')
            return false;
        }
                        
        if (is_any_price)
        {
            if (!user_id)
            {
                popupwindow('Данная возможность доступна только нашим <a href=\"/member/register.php\">зарегистрированным</a> покупателям');
                return false;
            }
                            
            if ( $('.input_any_price').val() && $('.input_any_price').val() > 0 )
            {
                $('a#add_to_cart').attr('href', to_cart_link + "&any_price="+$('.input_any_price').val()); 
            }
        }
                
    });
    
    $('a#only_for_vips').click(function() {    
                
        if (is_any_price)
        {
            if (!user_id)
            {
                popupwindow('Данная возможность доступна только нашим <a href=\"/member/register.php\">зарегистрированным</a> покупателям');
                return false;
            }
        }
        Javascript:popupwindow('Купить файл с книгой могут только наши <a target=\'_blank\' href=\'/actions/id.php?id=17\'>постоянные покупатели</a>. Но даже если Вы пока еще не относитесь к ним, Вы можете купить файл вместе с <a target=\'_blank\' href=\''+eversion_product1_url+'?show=1\'>бумажной версией</a> этой книги. Для этого кликните по <a href=\''+eversion_url_cart+''+(is_any_price?'&any_price='+$('.input_any_price').val()+"&currency_id="+currency_id+"&id_product="+eversion_id_product2:'')+'\'>ссылке</a> '+(is_any_price?'':'общая стоимость '+eversion_price+' руб.)')+'<br><br>Спасибо за понимание.');
        return false;
    });
                
}

function initPageInobookProduct() {
     initProductSendToFriend();
}

function initPageErrorsIndex() {
     var LI  = lookInside();
}
   
function initPageErrorsAdd() {
     var LI  = lookInside();
     
     initTinyMCE({
          "mode":"textareas",
          'edSettings':edSettings
     });
}
     


function initPageMessageAdd()
{
     initTinyMCE({
          "mode":"textareas",
          //'edSettings':edSettings,
          b1: ['emotions'],
          plugins:['emotions']
     });
     
     
}


function initPageSearch() {
     initToggle()
}


function initPageMemberSubscriptions() {
     initToggle()
}

function initPageBookslistTrade() {
     $('#a_bookslist_trade_file').click(function() 
     {
          $('#bookslist_trade_file_list').prepend(
               "<div id='bookslist_trade_file'>"+
               "<input type='file' name='img[]'/><br /><br /></div>");
          return false;
     })
}

// Send Link to Friend
function initProductSendToFriend() {
     $('a.send-to-friend').click(function() {
          if ($(this).css('background-image') == 'none') {
               $('#send-to-friend').css({'display':'none'});
               $(this).css({'background':'url(/static/images/bg-9.gif) repeat-x 0 96%'});
          } else {
               
               linkPositionLeft = $(this).position().left;
               linkPositionTop = $(this).position().top;

               send_width = $('#send-to-friend').width();
               send_height = $('#send-to-friend').height();
                  
               linkPositionLeft = linkPositionLeft - (send_width/2) + 100;
               linkPositionTop = linkPositionTop - send_height - 15;
               
               $('#send-to-friend').css({'display':'block'});
            $('#send-to-friend').css({'left':linkPositionLeft + 'px', 'top':linkPositionTop + 'px'});

               $(this).css({'background-image':'none'});
          }
          return false;
     });
     $('#send-to-friend .close').click(function() {
          $('#send-to-friend').css({'display':'none'});
          $('a.send-to-friend').css({'background':'url(/static/images/bg-9.gif) repeat-x 0 96%'});
     });
};


var itemSaveCommentRatingArr = {};
var pagetype = 'product';

     function  commentSaveRating(id,m) {
          
		  if($(this).hasClass('up')) {
             m = 1; 
             id = this.id.replace('comment_rating_up','');
          }
          else {
             m = -1;
             id = this.id.replace('comment_rating_down','');
          }
          
          var elem = this;
          
          if(typeof itemSaveCommentRatingArr[id] == 'undefined') {
     
               $.get('/ajax/save_rating_comment.php?id='+id+'&mark='+m+'&type='+pagetype, function(data) {
                  data=1; // temporary
                  if(data==1) {
                         
                         itemSaveCommentRatingArr[id] =data; 
                         
                         var mark = parseInt($('span', elem).html());
                         
                         mark ++;
                         
                         $('span', elem).html(mark)
                  }
               });
          
          }
          
          return false;
     } 
     
     function  comment_answer(id) {
          
          $("#answer_to_id").val(id);
          $("#post_answer").html('Ответ на комментарий '+ id + ' <a href="#" onclick="javascript:clear_comment_answer(); return false;">(стереть)</a>');
          return false;
     } 
     
     function  clear_comment_answer() {
          
          $("#answer_to_id").val('');
          $("#post_answer").html('');
          return false;
     }
     


function initTinyMCE(options)
{    
     options = options || {};
     options.mode = options.mode || 'textareas';
     options.element = options.element || '';
     options.edSettings = options.edSettings || {};
     
     options.b1 = options.b1 || [];
     options.plugins = options.plugins || [];
     options.theme_advanced_buttons1 = options.theme_advanced_buttons1 || [];
     
     if(options.b1.length) {
          options.b1 = ','+options.b1.join(',');
     } 
     else {
          options.b1 = '';
     }
     
     if(options.plugins.length) {
          options.plugins = ','+options.plugins.join(',');
     } 
     else {
          options.plugins = '';
     }
     
     if (!options.theme_advanced_buttons1.length) {
          options.theme_advanced_buttons1 = "images, bold,italic,underline,formatselect, link, unlink";
     }
     
     tinyMCE.init({
          mode : options.mode,
          elements: options.element,
          theme : "advanced",
          theme_advanced_buttons1 : options.theme_advanced_buttons1+options.b1,
          theme_advanced_buttons2:'',
          theme_advanced_buttons3:'',
          theme_advanced_blockformats:"p,blockquote",
          theme_advanced_toolbar_location : "top",
          theme_advanced_toolbar_align : "left",
          theme_advanced_statusbar_location : "bottom",
          theme_advanced_resizing : true,
          relative_urls : false,
          remove_script_host : true,language : 'ru',
          plugins : "safari,pagebreak,style,layer,table,save,advhr,advimage,advlink,images,inlinepopups,insertdatetime,preview,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template" + options.plugins,
          img_plugin: options.edSettings
     });     
}


function initPageDelivery() {

     /*
     return;
     // Delivery Type Toggle
     $('div.delivery-type dl.level-1 dt a').click(function(){return;
          //$('div.delivery-type dl.level-1 dt').removeClass('selected');
          //$('div.delivery-type dl.level-1 dd').removeClass('selected');
          //$('div.delivery-type dl.level-1 dd:visible').prev().removeClass('selected');
          //$('div.delivery-type dl.level-1 dd:visible').removeClass('selected');
          
          if ($(this).parent().hasClass('selected')) {
               $(this).parent().removeClass('selected');
               $(this).parent().next().removeClass('selected');
          } else {
               $(this).parent().addClass('selected');
               $(this).parent().next().addClass('selected');
          }
          return false;
     });
     $('div.delivery-type dl.level-2 dt label input').click(function(){return;
          if ($(this).parent().parent().parent().parent().hasClass('level-2')) {
               if ($(this).parent().parent().parent().hasClass('selected')) {
                    $(this).parent().parent().parent().removeClass('selected');
                    $(this).parent().parent().parent().next().removeClass('selected');
                    $(this).attr({'checked':''});
               } else {
                    $(this).parent().parent().parent().addClass('selected');
                    $(this).parent().parent().parent().next().addClass('selected');
                    $(this).attr({'checked':'checked'});
               }
          }
     });*/
         
        $.widget( "ui.combobox", {
            _create: function() {
                    var input,
                    that = this,
                    select = this.element.hide(),
                    selected = select.children( ":selected" ),
                    value = selected.val() ? selected.text() : "",
                    wrapper = this.wrapper = $( "<span>" )
                        .addClass( "ui-combobox" )
                        .insertAfter( select );
 
                function removeIfInvalid(element) {
                    var value = $( element ).val(),
                        matcher = new RegExp( "^" + $.ui.autocomplete.escapeRegex( value ) + "$", "i" ),
                        valid = false;
                    select.children( "option" ).each(function() {
                        if ( $( this ).text().match( matcher ) ) {
                            this.selected = valid = true;
                            return false;
                        }
                    });
                    if ( !valid ) {
                        // remove invalid value, as it didn't match anything
                        $( element )
                            .val( "" )
                            .attr( "title", "Нет результатов" )
                            .tooltip( "open" );
                        select.val( "" );
                        setTimeout(function() {
                            input.tooltip( "close" ).attr( "title", "" );
                        }, 2500 );
                        input.data( "autocomplete" ).term = "";
                        return false;
                    }
                }
 
                input = $( "<input>" )
                    .appendTo( wrapper )
                    .val( value )
                    .attr( "title", "" )
                    .addClass( "ui-state-default ui-combobox-input" )
                    .autocomplete({
                        delay: 0,
                        minLength: 0,
                        source: function( request, response ) {
                            var matcher = new RegExp( $.ui.autocomplete.escapeRegex(request.term), "i" );
                            response( select.children( "option" ).map(function() {
                                var text = $( this ).text();
                                if ( this.value && ( !request.term || matcher.test(text) ) )
                                    return {
                                        label: text.replace(
                                            new RegExp(
                                                "(?![^&;]+;)(?!<[^<>]*)(" +
                                                $.ui.autocomplete.escapeRegex(request.term) +
                                                ")(?![^<>]*>)(?![^&;]+;)", "gi"
                                            ), "<strong>$1</strong>" ),
                                        value: text,
                                        option: this
                                    };
                            }) );
                        },
                        select: function( event, ui ) {
                            ui.item.option.selected = true;
                            that._trigger( "selected", event, {
                                item: ui.item.option
                            });
                            select.trigger("change");                             
                        },
                        change: function( event, ui ) {
                            if ( !ui.item )
                                return removeIfInvalid( this );
                        }
                    })
                    .addClass( "ui-widget ui-widget-content ui-corner-left" );
 
                input.data( "autocomplete" )._renderItem = function( ul, item ) {
                    return $( "<li>" )
                        .data( "item.autocomplete", item )
                        .append( "<a>" + item.label + "</a>" )
                        .appendTo( ul );
                };
                
                input.val( '' );
                input.focus();
 
                $( "<a>" )
                    .attr( "tabIndex", -1 )
                    .attr( "title", "Показать все" )
                    .tooltip()
                    .appendTo( wrapper )
                    .button({
                        icons: {
                            primary: "ui-icon-triangle-1-s"
                        },
                        text: false
                    })
                    .removeClass( "ui-corner-all" )
                    .addClass( "ui-corner-right ui-combobox-toggle" )
                    .click(function() {
                        // close if already visible
                        if ( input.autocomplete( "widget" ).is( ":visible" ) ) {
                            input.autocomplete( "close" );
                            removeIfInvalid( input );
                            return;
                        }
 
                        // work around a bug (likely same cause as #5265)
                        $( this ).blur();
 
                        // pass empty string as value to search for, displaying all results
                        input.autocomplete( "search", "" );
                        input.focus();
                    });
 
                    input
                        .tooltip({
                            position: {
                                of: this.button
                            },
                            tooltipClass: "ui-state-highlight"
                        });
            },
 
            destroy: function() {
                this.wrapper.remove();
                this.element.show();
                $.Widget.prototype.destroy.call( this );
            }
        });
        
        
        $('#combobox271').live("change", function() {              
            ayaMap.goToPoint($(this).val(),false);
            $('.level-2').children('dt').hide();
            $( "#dtdelivery271_"+$(this).val()).show();
            $('#order_delivery_next').show();
            $("#ddelivery271_"+$(this).val()).prop('checked', true);         
            $("#ddelivery271_"+$(this).val()).trigger('click');
        });
        $('#combobox304').live("change", function() {              
            ayaMap.goToPoint($(this).val(),false);
            $('.level-2').children('dt').hide();
            $( "#dtdelivery304_"+$(this).val()).show();
            $('#order_delivery_next').show();
            $("#ddelivery304_"+$(this).val()).prop('checked', true);         
            $("#ddelivery304_"+$(this).val()).trigger('click');
        }); 
}

function checkYaPoint($val) 
{
    $('.level-2').children('dt').hide();
    $( "#dtdelivery"+$val).show();
    $('#order_delivery_next').show();    
    $("#ddelivery"+$val).prop('checked', true);         
    $("#ddelivery"+$val).trigger('click');
    $('html, body').animate({
        scrollTop: $("#order_delivery_next").offset().top
    }, 2000);
    ayaMap.close();
}

var yaMapsPoints = [];
var yaMapsCity;
     
function initPagePassword() {
     initChooseToggle();
}    
 
function initPageOrder() {
          $('a.pdf').click(function() {
               linkPositionLeft = $(this).parent().position().left;
               linkPositionLeft = linkPositionLeft - 90 + "px";
               linkPositionTop = $(this).parent().position().top;
               linkPositionTop = (linkPositionTop - $(this).parent().parent().find('div.popup').height()) + 10 + "px";
               $(this).parent().parent().find('div.popup').css({'display':'block'});
               $(this).parent().parent().find('div.popup').css({'left':linkPositionLeft, 'top':linkPositionTop});
               return false;
          });
          $('div.popup .close').click(function() {
               $(this).parent().parent().css({'display':'none'});
          });
}    
 
function initPageOrderPayments() {
     initChooseToggle();
}    
 
function initPageOrderQuestion() {
     initChooseToggle();
}    
 
function initChooseToggle() 
{
     $('dl.choose dt label input').click(function(){
          if ($('dl.choose dd').html())
          {
               $pp = $(this).parent().parent();
               if ($pp.hasClass('selected')) 
               {
                    $pp.removeClass('selected');
                    $('dl.choose dd:visible').removeClass('selected');
                    $(this).prop({'checked':''});
               } 
               else 
               {
                    $('dl.choose dd:visible').removeClass('selected');
                    $('dl.choose dt.selected').removeClass('selected');
                    $pp.next().addClass('selected');
                    $pp.addClass('selected');
                    $(this).prop({'checked':'checked'});
               }
          }
     });
}     
     
// Gift
$(document).ready(function() {
     $(document).click(function(e) {
          if( $(e.target).parents('.popup.gift').length==0 )
               $('.popup.gift').hide();
     })
     $('p.gift a, .popuptext').hover(function() {
          $('.popup.gift').hide();
          var id = this.id.replace('a_','')
          
          var popup = $('#'+id);
          
          if ($('.popuptext').val()) return;
          
          linkPositionLeft = $(this).position().left  - Math.round(popup.width() / 2) + Math.round($(this).width() / 2 ); 
          linkPositionLeft = linkPositionLeft  + "px";
          linkPositionTop = $(this).parent().position().top; 
          
          linkPositionTop = (linkPositionTop - popup.height()) - 10 ;
          
          var popup_h = popup.height()
          if ($(this).parent().offset().top < popup_h) {
               linkPositionTop +=  popup_h - $(this).parent().offset().top + 40 ;;
          }
          
          linkPositionTop= linkPositionTop+ "px"

          popup.css({'display':'block'});
          popup.css({'left':linkPositionLeft, 'top':linkPositionTop});
          return false;
     }, function() {
          
     });
     $('div.popup.gift .close').click(function() {
          $(this).parent().parent().css({'display':'none'});
     });
     
     if(window.location.hash == '#gift') $("p.gift a").trigger('mouseenter');
});  

///////////////////////////////////////////////////////////////////////////     

function calc_merged_cost()
{
     sum = 0;
     $(".choosen_order").each(function(){ 
          if (!this.checked)
          {
               return;
          }
          sum+=ListForMerge[this.value].cost
     });
     $("#cost_added").html(sum);
     $("#cost_result").html(sum + order_cost);
}

function init_merge()
{
     $popup = $('div.unt-popup');
     $('div.unite table.catalog tbody tr').mouseenter(function(){
          $(this).addClass('hovered');
          popupTop = $(this).offset().top - 240 + "px";
          $popup.css({'left':'410px','top':popupTop,'display':'block'});
          $("#popup_cost_added").html(ListForMerge[this.id].cost);
          $("#popup_cost_result").html(order_cost + ListForMerge[this.id].cost);
     });
     $('div.unite table.catalog tbody tr').mouseleave(function(){
          $(this).removeClass('hovered');
          $popup.css({'display':'none'});
     });
     $popup.mouseenter(function(){
          $(this).css({'display':'block'});
     });
     $popup.mouseleave(function(){
          $(this).css({'display':'none'});
     });
     $(".choosen_order").click(calc_merged_cost);
};
     
     
$(document).keyup(function(e) {
        if (e.keyCode == 27) {
            $('div.black').fadeOut(250);
            $('div.white').fadeOut(250);
            $('div.whitepopup').fadeOut(250);
        }   // esc
     });
 
var lookInside = function() {
     var preloader, last;
     
     preloader = Preloader($('#product_look_inside .ajaxpreloader'));
     
     var init_type = '';
     
     var last_all = {};
     
     var selected_preview = 0;
     
     if( $('#look_inside_covers .hidden' ).length ) {
          init_type = 'covers';
     }
     else if( $('#look_inside_inside .hidden' ).length ) {
          init_type = 'inside';
     } 
     else if( $('#look_inside_pdf .hidden' ).length ) {
          init_type = 'pdf';
     }
     else {
          init_type = 'contents';
     }
     
     last = {type:init_type, id:0, item_id:''};
     
     var ling = false;
     
     $('#product_look_inside ul.covers li').each(function(){
          if(this.id == 'look_inside_contents') return;
          
          var cnt = $('.hidden', this).length;
          
          $('#'+this.id+'_cnt', this).html('<span style="white-space:nowrap">(1 / '+cnt+')</span>');
          
     });
     
     $('#product_previews a').click(function () {
          
          $('#product_preview_big  img').attr('src', this.href);
          
          
          selected_preview = $('#product_previews a').index(this); 
          return false;
     });

      $('a.look-inside, #product_preview_big a').click(function(){
          $('div.black').fadeIn(0);
          $('div.black').fadeTo(0, 0);
          $('div.black').fadeTo(500, 0.5);
          
          if (is_ie6 || is_ie7) {
               $('div.white').fadeIn(0);
               blockWidth = $('div.white div.block').children('div').width() + 10 + "px";
               $('div.white').css({'width':blockWidth});
               $('div.white').fadeOut(0);
          }
          
          windowWidth = $(window).width();
          popupWidth = $('div.white').width();
          popupLeft = (windowWidth - popupWidth) / 2 + "px";
		  popupTop = getPageScroll()[1] + (getPageHeight() / 10) + "px";
          $('div.white').css({'left':popupLeft, 'top':popupTop});
          $('div.white').fadeIn(500);
          
     
          last = {type:init_type, id: 0, item_id: ''};
          if(last.type=='covers') {
               last.id = selected_preview;
          }
          
          show();
          return false;
     });
    $('#product_look_inside ul .cover, #product_look_inside ul .descr').click(function() 
     {
          if(ling) return;
          var type = ($(this).parents('li').attr('id')).replace('look_inside_','');
          
          var item_id = '#'+($(this).parents('div.item_row').attr('id'));

          last.type = type;
          last.id = 0;
          last.item_id = item_id;
          
          if (typeof last_all[last.type] != 'undefined') {
               last.id = last_all[last.type];
          }
          
          show();
          return false;
     });
     
     // only one element, there is no need in arrows
     var lis = $('#product_look_inside .covers li');
     var a_in_lis = $('a', lis);
    //alert(lis.length);
    //alert(a_in_lis.length);
     if(lis.length==1 && a_in_lis.length==1) {
          $('#product_look_inside .slider-lookinside-right').hide();
          $('#product_look_inside .slider-lookinside-left').hide();
     }
     
     $('#product_look_inside .slider-lookinside-right').click(function() {
          right();
     }) 
     
     $('#product_look_inside .slider-lookinside-left').click(function() {
          left();
     }) 
     
     $('div.black').click(function(){
          $('div.black').fadeOut(250);
          $('div.white').fadeOut(250);
     });
     
     $('div.white .close').click(function(){
          $('div.black').fadeOut(250);
          $('div.white').fadeOut(250);
     });
     
     var right = function() {
          if(ling) return;
          var section = ($('#product_look_inside '+last.item_id+' ul.covers #look_inside_'+last.type+ ' .hidden' ));
          
          last.id ++;
          
          if( last.id>=section.length ) {
               last.id = 0;
              
               section = $('#product_look_inside '+last.item_id+' ul.covers #look_inside_'+last.type+ '' ).next(); 
               if(section.length && section[0].tagName.toLowerCase() =='b') {
                    section = section.next();
               } 
              
               if(section.length==0) {
                    section = $('#product_look_inside '+last.item_id+' ul.covers li').first(); 
               }
               
               last. type = section.attr('id').replace('look_inside_','');
               
          }
          
          show();
     }
     
     var left = function() {
          if(ling) return;
          var section = ($('#product_look_inside '+last.item_id+' ul.covers #look_inside_'+last.type+ ' .hidden' ));
          
          last.id--;
          
          
          if( last.id<0 ) {
               
               
               section = $('#product_look_inside '+last.item_id+' ul.covers #look_inside_'+last.type+ '' ).prev();
               if(section.length && section[0].tagName.toLowerCase() =='b') {
                    section = section.prev();
               } 
             
               if(section.length==0) {
                    section = $('#product_look_inside '+last.item_id+' ul.covers li'); 
                    section = section.last();
               } 
               
               last.id = $('.hidden',section).length-1;
               
               last. type = section.attr('id').replace('look_inside_','');
               
          }
          
          show();
     }
     

     var show = function()
     {
          if(ling) return;
          
          
          $('#product_look_inside ul.covers li').removeClass('selected');
          if (last.item_id)
          {
            $('#product_look_inside '+last.item_id+' ul.covers #look_inside_'+last.type+ '' ).addClass('selected');
          }
          
          if (last_all['item_id'] != last.item_id) last.id = 0;
              
          last_all[last.type] = last.id;
          last_all['item_id'] = last.item_id;
                    
          if(last.type=='contents') 
          {
               $('#product_look_inside .middle-block table img').hide()
               
               var src = ($('#product_look_inside '+last.item_id+' ul.covers #look_inside_'+last.type+ ' div.hidden' ).eq(last.id)).html()
               
               $('#product_look_inside .middle-block table  div').html(src)
          }
          else 
          if(last.type=='pdf') 
          {
               $('#product_look_inside .middle-block table img').hide()
               
               var src = ($('#product_look_inside '+last.item_id+' ul.covers #look_inside_'+last.type+ ' div.hidden' ).eq(last.id)).html()
               
               $('#product_look_inside .middle-block table  div').html(src)
          }
          else
          {
               preloader.show();
               ling = true;
               
               var src = $('#product_look_inside '+last.item_id+' ul.covers #look_inside_'+last.type+ ' div.hidden' ).eq(last.id).find('a').attr('href');
               
               var tmpImg = new Image();
               
               if (last.item_id)
               {
                   var cnt = $(last.item_id+' #look_inside_'+last.type+ ' div.hidden' ).length;                   
             
                   $(last.item_id+' #look_inside_'+last.type+ '_cnt').html('<span style="white-space:nowrap">('+(last.id+1)+' / '+cnt+')</span>');
               }
               
             
               tmpImg.onload = function() {
                    preloader.hide();
                    $('#product_look_inside .middle-block table img').show()
                    $('#product_look_inside .middle-block table div').html('')
                    
                    $('#product_look_inside .middle-block table img').attr('src', src)

                    if(tmpImg.width>670)
                         $('#product_look_inside .middle-block table img').width(670)
                    
                    ling = false;
                    
                    delete(tmpImg);
               }
               tmpImg.onerror = function() {
                    preloader.hide();
                    alert('Изображение не найдено!');
                    ling = false;
                    delete(tmpImg);
               }

               tmpImg.src = src;

          }
     }
     
     return {
          setLastType: function( type){
               last.type = type;
          }
     }

}


var windowSelectUser = {
     options: {},
     
     userFriendsSelected:{},
     
     select_friends_last: '',
     
     init: function(options) {
          this.options = options || {};
          
          
          var obj=this;
          $(document).ready(function() {
               $('#window-select-friends-add').click(function() {
                    alert('Добавлено');
                    return false;
               });

               $('#window-select-friends-close').click(function() {
                    $("#window-select-friends").dialog('close');
                    
                    $('select[name='+obj+select_friends_last+']').val('unknown');
                    return false;
               });
               
               $('#window-select-friends-all').click(function() {
                    
                    var frame = document.getElementById('window-select-friends-frame');
                     frame.contentWindow.selectAll();
                    return false;

               });
               $('#window-select-friends-none').click(function() {
                    var frame = document.getElementById('window-select-friends-frame');
                    frame.contentWindow.diselectAll();
                    return false;

               });
               
               
               obj['init_show_'+ options.show_type](options.show_selector, options.show_tmp || '');
          });
     },
     
     
     init_show_select: function(selector, param) {
          var obj=this;
                    $(selector).change(function() {
                         val = (this.value);
                         
                         if(val == param) {//alert(1);
                              obj.select_friends_last = this.name;
                                        $("#window-select-friends").dialog({
                                        modal: true,
                                             width:700,
                                             close: function(event, ui) { 
                                             
                                                  $('select[name='+obj.select_friends_last+']').val('unknown');
                                                  obj.userFriendsSelected={};
                                                  
                                                  var frame = document.getElementById('window-select-friends-frame');
                                                  frame.contentWindow.diselectAll();
                                              }
                                        });
                              
                         }
                    })
     },
     
     
     init_show_a: function(selector) {
                    var obj = this;
                         
                    $(selector).click(function() {
                         $("#window-select-friends").dialog({
                         modal: true,
                              width:700,
                              close: function(event, ui) { 
                              
                                   $('select[name='+obj.select_friends_last+']').val('unknown');
                                   obj.userFriendsSelected={};
                                   
                                   var frame = document.getElementById('window-select-friends-frame');
                                   frame.contentWindow.diselectAll();
                               }
                         });
                    }
                    );   
               return !true;
     }
};


function restore_question_change($obj)
{
     if (!!!$obj)
     {
          return;
     }
     $block = $("#customquestionblock");
     if ('custom' != $obj.val())
     {
          $block.hide();
     }
     else
     {
          $block.show();
     }
}

function init_register()
{
     $tmp = $("#restore_question_id");
     $tmp.change(function(){
          restore_question_change($(this));
     }
     );
     restore_question_change($tmp);
}
///////////////////////////////////////////////////////////////////////////

function initOrderCalendar() {
     $('#order_calendar .calendar').bind('click', function() { 
     
          if($('#order_calendar div').css('display') =='none' )
               $('#order_calendar div').show() 
          else {
               $('#order_calendar div').hide() 
          }
     });
     
     $("#order_calendar1 ").datepicker({
               dateFormat:'dd.mm.yy',
               showOn: 'both',
               buttonImage: '/static/images/icons/calendar-1.gif',
               buttonImageOnly: true
          });
     $("#order_calendar2 ").datepicker({
               dateFormat:'dd.mm.yy',
               showOn: 'both',
               buttonImage: '/static/images/icons/calendar-1.gif',
               buttonImageOnly: true
          });
}

function initOrderHistory() {
     initOrderCalendar();
}

function initOrderIndex() {
     initOrderCalendar();
     $("#orders_list_filter").change(function(){
          this.form.submit();
     })
}

function initCalendar(id, type, date_offset) {
     type = typeof type !== 'undefined' ? type : 0;
     
     date_offset = typeof date_offset !== 'undefined' ? date_offset : new Date(2000, 01, 01);
     
     $.datepicker.regional['ru'] = {
        monthNames: ['Яварь', 'Февраль', 'Март', 'Апрель',
        'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь',
        'Октябрь', 'Ноябрь', 'Декабрь'],
        dayNamesMin: ['Вс','Пн','Вт','Ср','Чт','Пт','Сб'],
        firstDay: 1,
     };
     
     $.datepicker.setDefaults($.datepicker.regional['ru']);
     
     $("#"+id).datepicker({
               dateFormat:(type==1?'dd.mm.yy':'yy-mm-dd'),
               showOn: 'both',
               buttonImage: '/static/images/icons/calendar-1.gif',
               buttonImageOnly: true,
               minDate: date_offset,
               beforeShow: function()
              {
                   setTimeout(function()
                   {
                       $(".ui-datepicker").css("z-index", 999999);
                   }, 10); 
              }
          });         
      
}

function initPagePremiumDates() {
     $(function() { initCalendar('stat_calendar1', 1, 1); initCalendar('stat_calendar2', 1, 1);});
}

function initPagePartnerStatistics() {
     $(function() { initCalendar('stat_calendar1'); initCalendar('stat_calendar2');});
}

function initPageMessage() {
     
     $(function() {
          $('#messages').find(' input').click(function(e) {(e.stopPropagation())});
          
          $('dl.messages dt').mouseenter(function(){
               $(this).addClass('hovered');
               corners = '<span class="tl"></span><span class="tr"></span><span class="bl"></span><span class="br"></span>';
               $(this).find('div.block').append(corners);
               $(this).find('span.gradread').css({'display':'none'});
               $(this).find('span.gradnew').css({'display':'none'});
               $(this).find('span.gradhover').css({'display':'block'});
          });
          $('dl.messages dt').mouseleave(function(){
               $(this).removeClass('hovered');
               $(this).find('span.gradread').css({'display':'block'});
               $(this).find('span.gradnew').css({'display':'block'});
               $(this).find('span.gradhover').css({'display':'none'});
          });
          $('dl.messages dt').click(function(){
               href = $(this).find('p.msg a').attr('href');
               document.location = href;
          });

          $('#messages_filter a.check').click(function() {
               var  type = this.className.replace('check ', '');
               
               
               if(type=='all') {
                    $('#messages').find(' input').prop('checked','checked');
               }
               else if(type=='none') {
                    $('#messages').find(' input').removeAttr('checked');
               }
               else {
                    $('#messages').find(' input').removeAttr('checked');
                    $('#messages').find('.'+type).find('input').prop('checked','checked');
               }
              
               
               return false;
          
          });})
          
     jQuery('#message_action_choise').change(function()  
     {
          if(this.value!='')
          {
                                                                 
               var len = jQuery('#messages input:checked').length;
               
               if(len==0) {
                    alert('Выберите сообщения для групповой операции');
                    this.value = 0;
                    return false;
               }
               
               jQuery('#messages  #message_action').val(this.value);
               
               jQuery('#messages form').trigger('submit');
          }
          return true;
     });

}

function init_agreed()
{
     $("#agreed").click(function(){
          $btn = $("#btn");
          if (this.checked)
          {
               $btn.removeAttr("disabled");
          }
          else
          {
               $btn.attr("disabled", "disabled");
          }
     });
}
///////////////////////////////////////////////////////////////////////////

function numbers_round(number, rate) { 
    if(rate >= 1 || rate == 0) { 

        return Math.ceil(number); 

    } 
    if(rate <= 0.05 ) { 

        return Math.round(number*100)/100;

    } 
    return Math.round(number*10)/10;

}
///////////////////////////////////////////////////////////////////////////

function initStageContactInfo()
{
     $("#sms_on").click(function(){
          $block = $("#sms_number_block");
          if (this.checked)
          {
               $block.addClass("displayed");
          }
          else
          {
               $block.removeClass("displayed");
          }
     });
     
    $("input[name='phone']").mask("+99999999999?99999", {placeholder:" "});
}
///////////////////////////////////////////////////////////////////////////

function discode_show($obj)
{
     $("#discode-show-block").hide();
     $("#discode-input-block").show();
     return false;
}

function discode_hide($obj)
{
     $("#discode-input-block").hide();
     $("#discode-show-block").show();
}

function initStageConfirmation()
{
     $(".discode-input-trigger").click(discode_show);
     $("#btn_discode_cancel").click(discode_hide);
     
      $('#order_confirmation_address_change').click(function(){
          Window('window_user_addressbooks').show();
          return false;
     });
    
     
     $('#order_confirmation_address_list a').each(function() {
          var t = this;
          $(this).parent().click(function() {
               location.href = t.href;
          });
          
          
     }) 
     
     
          
     initAjaxContent('a_ajaxcontent_agreement', 'user_agreement');
}
///////////////////////////////////////////////////////////////////////////

function initCart()
{
     $(".discode-input-trigger").click(discode_show);
}
///////////////////////////////////////////////////////////////////////////

function initStageAdminCityDelivery()
{
     $("#id_city").click(function(){
		  AddressSelector(
				{ // fields
					//;
				},
				{ // options
					level: 'City', 
					popup_id: 'address-selector',
					onSelect: function(data)
						{
							$('#dregion_name').html(' ('+data.region.name + ' ' + data.region.socr + ' / ' + data.city.name+')');
							$('#id_city').val(data.city.code);
							
						},
					baseurl: '/static/kladr/data'
				});
     });
}
///////////////////////////////////////////////////////////////////////////

var deliveries =  function() {
     
     var _$ = {
          mode: 'full',
          only_econom: false,
          
          set_mode: function( mode ) {
               this.mode = mode;
          },

          
          init: function() {
               this.preloader = Preloader( $('#deliveryajaxpreloader')  );
               
               var me = this;
               
               $('dl.level-1 .dr_sub').click(function() {                   
                    var  id = this.id.replace('dr_sub', ''); 
                    me.mode != 'simple' ? me.check(this, id):me.check_from_array(this, id);
                    $(this).addClass('selected');
                    $(this).siblings('.dr_sub').removeClass('selected');
               });     
                    
               $('.delivery-type .dr').click(function() {
                    var  id = this.id.replace('dr', '');                  
                        me.mode != 'simple' ? me.check(this, id):me.check_from_array(this, id);
                    return false;
               });
               
               $('.delivery-type div select').change(function() {
                    var id = this.value;
                    me.mode != 'simple' ? me.check(this, id):me.check_from_array(this, id);
                    return false;
               });
               
               $('.delivery-type #dr1-1, .delivery-type #dregion_name').click(function() {
                    me.onClickKladr();
					return false;
               });
               
               if(typeof order_context != 'undefined' && order_context.region && order_context.region != 1)
               {
               
                         if( $('#dr'+ order_context.region+'-'+order_context.country ) .length) {
                              var obj = $('#dr'+ order_context.region+'-'+order_context.country )[0];
                              
                              var  id =  obj.id.replace('dr', '');
                         }
                         else if( $('.dcountries select ').find("option[value='"+order_context.region+"']") .length ) {
                              $('.dcountries select ').find("option[value='"+order_context.region+"']").prop("selected","selected");
                              
                              var obj = $('.dcountries select ')[0];
                              
                              var id = obj.value;
                         }
                         else if( $('#dregions'+ order_context.country) .length ){
                              $('#dr'+ order_context.country+'-1' ).trigger('click');
                              
                             $('.dcountries select ').find("option[value='"+order_context.country+"']").prop("selected","selected");

                              var obj = $('#dregions'+ order_context.country+' select');
                              $(obj).find("option[value='"+order_context.region+"-"+order_context.country+"']").prop("selected","selected");
                              obj = obj[0];
                              
                              var id = obj.value;
                              
                         }

                         
                         function handler() 
                         {
                              var dt_delivery = $('#dtdelivery'+ order_context.region+'_'+order_context.delivery );
                              
                              dd_delivery = dt_delivery.next();
                              
                              dt_delivery.addClass('selected');
                              dd_delivery.addClass('selected');
                              
                              if($('input', dt_delivery)[0])
                                   $('input', dt_delivery)[0].click()
                              
                              if($('input', dd_delivery)[order_context.complectation])
                                   $('input', dd_delivery)[order_context.complectation].click();
                         }
                         
                         if (me.mode != 'simple')
                         { 
                              me.check(obj, id, handler);
                         }
                         else
                         {
                              me.check_from_array(obj, id);
                              $("#ddelivery"+order_context.region+'_'+order_context.delivery).trigger('click');
                         }
                         
               } else this.hide_last();
          },
          
          show: function(dt) {
               var dd = dt.next();
               dt.addClass('selected');
               dd.addClass('selected');
          },
          
          hide: function(dt) {
               var dd = dt.next();
               dt.removeClass('selected');
               dd.removeClass('selected');
          },
          
          
          hide_last: function() {
               
               $('.delivery-type dt').removeClass('selected');
               $('.delivery-type dd').removeClass('selected');
               $('.delivery-type  .dregions, .dcountries, .dsubgroups271, .dsubgroups304').hide();
              
          },
          
          check_button_next: function() {
               var delivery = $('.delivery-type input[name=delivery]:checked').val();
               var complectation = $('.delivery-type input[name=complectation]:checked').val();
               
               
               if(delivery>0 && complectation!='') {
                    $('#order_delivery_next').show();
               }
               else {
                    $('#order_delivery_next').hide();
               }
          },
          
          default_complectation: {},
          
          currency_ticker:'руб',
          currency_rate: 1,
               
          // show complectations
          check_delivery:function(obj) {
                    if ($(obj).parents('.level-3').length) return;
                    
                    var dt = $(obj).parents('dt');
                   
                    var dd = dt.next();
                    
                    $('dt', dt.parent()).removeClass('selected');
                    $('dd', dt.parent()).removeClass('selected');
                    
                    if(!this.only_econom) 
                    {
                         dt.addClass('selected');
                         dd.addClass('selected');
                    }
                   
                    
                    id = obj.id .replace('ddelivery','').split('_');
                    
                    var  default_complectation = this.default_complectation[id[0]] [id[1]];
                    
                   
                    $('input',dd)[default_complectation].checked = true;
                    
                    this.check_button_next();
                    
                    return false;
          },
          
          
         // check parent delivery
          check_complectation:function(obj) {
                    
                    var dt = $(obj).parents('dt');
                    var dd = dt.next();
                    
                    var order_product__price_ = order_product__price;
                    
                    var delivery_price = parseFloat($('#'+obj.id+'_price').html());
                    
                    var all_price = delivery_price+order_product__price_;
                    all_price = Math.round(all_price*100)/100;
                    
                    id = obj.id.replace('dcomplectation', '').split('_')
                    
                    var selected_complectation = obj.value;
                    selected_complectation = selected_complectation.split('_')

                    
                    this.default_complectation[id[0]] [id[1]] = selected_complectation[2];
                    
                    var delivery_dt = $('#dtdelivery'+id[0]+'_'+id[1]);
                    
                    
                    if(delivery_price==0) 
                    {
                         delivery_price = 'бесплатно';
                    }
                    else 
                    {
                         delivery_price += ' '+this.currency_ticker;
                    }
                    $(delivery_dt).find('.delivery_price').html(delivery_price);
                    $(delivery_dt).find('.all_price').html(Math.round(all_price*100)/100);
                    
                    this.check_button_next();
                    
                    return false;
          },
          onClickKladr: function() {
			var me = this;
			AddressSelector(
				{ // fields
					'kladr_region':'Region.name',
					'kladr_subregion':'SubRegion.name',
					'field_city':'City.name',
					'city_code':'City.code'
				},
				{ // options
					level: 'City', 
					popup_id: 'address-selector',
					onSelect: function(data)
						{
							$('#dregion_name').html(data.region.name + ' ' + data.region.socr + ' / ' + data.city.name);
							me.check($("#russian_region")[0], '1000000-1');
							
						},
					baseurl: '/static/kladr/data'
				});
		  },
          check: function(obj, id, handler) {
               if(typeof id == 'undefined') return;
               
               $('#order_delivery_next').hide();
               $('.delivery-type input[name=delivery]').removeAttr('checked');
               $('.delivery-type input[name=complectation]').removeAttr('checked');
               
               
               
               id = id.split("-");
               
               region = id[0];
               country = (typeof id[1] !== 'undefined')  ? id[1]:region;
               delivery_type = (typeof id[2] !== 'undefined')  ? id[2]:'0';
               if (region==0) {
                    
                    return this.show_countries(obj);;
               }
               if ((region==271 || region==304) && delivery_type == '0') {                    
                    return this.show_sub_groups(obj, region);
               }
              
               var dt = $(obj).parents('dt');
               
               var dd = dt.next();

			   if ($('#dregions'+region).length){
						this.hide_last();
						if(obj.tagName.toLowerCase()=='select') $(obj).parent().show();
						
						
						return this.show_region(region);;
				   }
				   
				   if (obj.tagName.toLowerCase() !='select' && obj.tagName.toLowerCase() !='div') { 
						// если доставки уже есть
                        
						if (dd.html() != '') {
							 this.hide_last();
							 //this.show(dt);
							 //return false;
                             dd.html('');
						}
				   }
			   
               
               
               this.preloader.show();
               
               var me = this;
               $.post('/member/ajax/order/get_delivery_by_region.php?order='+id_order_exists,
                         {region_id:region, country_id:country,kladr_region:$('#kladr_region').val(),field_city:$('#field_city').val(),city_code:$('#city_code').val()},
                         function(data) {
                              
                              
                              data = eval(data);
                              order_product__price_ = data.cart_price;
                              order_product__price  = data.cart_price;

                              me.currency_ticker = data.ticker;
							  
							  if (region == 1000000) 
							  {
								region = data.region_id;
							  }
							  
							  me.default_complectation[region] = {};

                              data = data.region_deliveries;

                              var html = '';
                              var options = '';
                              var price = 0; 
                              var tmp; 
                              var count = 0;
                              var map_count = 0;
                              var yaMapsPoints = []
                              var old_data = []
                              var new_data = []
                              var iteration = 0;
                              old_data = data;
                              for(var d in data) 
                              {
                                new_data[data[d].id] = data[d];
                              }
                              data = new_data;
                              for(var d in old_data) 
                              {
                                   d = old_data[d].id;
                                   if (delivery_type == '1' && data[d].delivery_type != '1') continue;
                                   if (delivery_type == '3' && (data[d].delivery_type == '1' || data[d].delivery_type == '2')) continue;
                                   
                                   price = order_product__price_;
                                   
                                   tmp = parseFloat(data[d].price_final); 
                                   if(!isNaN(tmp )) {
                                        price += tmp 
                                        price  = Math.round(price*100)/100;
                                   }
                                   
                                   count++;
                                   
                                   var deliv_checked = '';//count == 1 ? 'checked="checked"':'';
                                   
                                   //var delivery_desc=$('#delivery_desc'+d).html() || '';
                                   var delivery_desc =  data[d].delivery_desc ? data[d].delivery_desc : '';
                                   
                                   if ((region == '271' || region == '304') && delivery_type == '2' && data[d].delivery_type == '2')
                                   {
                                   map_count++;
                                   options+= '<option value="'+data[d].id+'">'+data[d].delivery_name+' ('+data[d].price_final+')</option>';
                                   yaMapsPoints[map_count-1] = {id: data[d].id, content: map_count, dl_kind: data[d].id, x :data[d].delivery_coords_lat, y: data[d].delivery_coords_lng, zoom: 15, name:data[d].delivery_name, baloon:"<div><img src=\"http://www.books.ru/static/images/icons/eyes.gif\" width=\"32\" height=\"23\" alt=\"\"  style=\"padding: 0px 5px 0px 0px; vertical-align: middle;\"/><b style=\"color: #1270B8; vertical-align: middle;\">"+data[d].delivery_name+"</b></div><div>"+delivery_desc+(data[d].link_books?" <a href=\""+data[d].link_books+"\" target=\"_blank\">Подробнее</a>":"")+"<p class=\"ymaps-point\">&nbsp;</p><a class=\"ymaps-point\" href=\"#/\" onclick=\"checkYaPoint('"+region+"_"+data[d].id+"'); return false;\">Выбрать</a></div>"};
                                   }
                                    

                                   html += '<dt id="dtdelivery'+region+'_'+data[d].id+'">'+
                                        '<div class="col-1">'+
                                             '<label for="ddelivery'+region+'_'+data[d].id+'"><input type="radio" name="delivery" value="'+data[d].id+'" id="ddelivery'+region+'_'+data[d].id+'" '+deliv_checked+'/>'+(data[d].delivery_name?data[d].delivery_name:data[d].name)+'</label>'+
                                             '<p> '+delivery_desc+' </p> '
                                        +'</div>'+
                                        '<div class="col-2">'+
                                             '<p class="price"><strong><span class="price"> <span class="all_price">'+(price)+'</span> <span class="rub">'+me.currency_ticker+'</span></span> </strong></p>'+
                                             '<p>'+(eng==1?'Price':'Товаров на')+' <strong><span class="price">'+order_product__price_+' <span class="rub">'+me.currency_ticker+'</span></span> </strong><br/>'+(eng==1?'delivery':'доставка')+' <strong  class="delivery_price">'+data[d].price_final+'</strong></p>'+
                                        '</div>'+
                                        '<div class="clear"></div>'+
                                   '</dt>'
                                   ;
                                   
                                    me.only_econom = (data[d].price.length == 1)
                                   
                                   if (me.only_econom)
                                   {
                                        me.default_complectation[region][d] = 0;
                                        html += '<dd><input type="radio" value="'+region+'_'+data[d].id+'_0" name="complectation" id="dcomplectation'+region+'_'+data[d].id+'_0" '+compl_checked+'/></dd>';
                                   }
                                   else {
                                   
                                        html += '<dd>'+
                                             '<p>'+(eng==1?'Complectation':'Способ комплектации')+':</p>'+
                                             '<dl class="level-3">';
                                             
                                        for(var c in data[d].price){ 
                                        
                                             price = Math.round(order_product__price_*100)/100;
                                             
                                             tmp = parseFloat(data[d].price[c]); 
                                             if(!isNaN(tmp)) {
                                                  price+= tmp;
                                                  price = Math.round(price*100)/100;
                                             }
                                             
                                             if(order_product__count=== 1)
                                             {
                                                  me.default_complectation[region][d] = 0;
                                             }
                                             else 
                                             {
                                                  me.default_complectation[region][d] = data[d].complectation;
                                             }
                                            
                                             var compl_checked = '';//data[d].complectation ==c ? 'checked="checked"':'';
                                             
                                             var tmp_price = parseFloat(data[d].price[c]);
                                             if(isNaN(tmp_price)) 
                                             {
                                                  tmp_price = 0;
                                             }
                                             tmp_price = Math.round(tmp_price*100)/100;
                                             
                                             var complectatio_desc=$('#complectation_desc'+c).html() || '';
                                             
                                             html+='<dt>'+
                                                       '<div class="col-1">'+
                                                            '<label for="dcomplectation'+region+'_'+data[d].id+'_'+c+'"><input type="radio" value="'+region+'_'+data[d].id+'_'+c+'" name="complectation" id="dcomplectation'+region+'_'+data[d].id+'_'+c+'" '+compl_checked+'/>'+ order_delivery_complect[c] +'</label>'+
                                                            '<p>' + complectatio_desc + '</p>'+
                                                            '<div class=\'hidden\'  id="dcomplectation'+region+'_'+data[d].id+'_'+c+'_price">'+(tmp_price)+'</div>'+
                                                       '</div>'+
                                                       '<div class="col-2">'+
                                                       '    <p class="price"><span class="price">'+(price)+' <span class="rub">'+me.currency_ticker+'</span></span></strong></p>'+
                                                            '<p>'+(eng==1?'Price':'Товаров на')+' <strong><span class="price">'+(order_product__price_)+' <span class="rub">'+me.currency_ticker+'</span></span></strong><br/>'+(eng==1?'delivery':'доставка')+' <strong>'+data[d].price[c]+'</strong></p>'+
                                                       '</div>'+
                                                       '<div class="clear"></div>'+
                                                  '</dt>';

                                             
                                        }
                                        
                                        html += '</dl></dd>';
                                   }    
                              }                              

                              if(html != '') {
                                   html = '<div class="level-2"><dl class="level-2"> '+
                                             (((region == '271' || region == '304') && delivery_type == '2') ?'<div class="level2_header">'+'Выберите из списка или на карте:</div><div class="ui-widget">'+
                                                '<select id="combobox'+region+'" name="id_delivery">'+
                                                    options +
                                                '</select>'+
                                             '</div>'+ 
                                             '<div id="self_items_map'+region+'" class="content_upload" style="margin:10px 10px 20px 20px; width: 600px; height: 600px">Загрузка карты...</div>':'')+ 
                                      
                                             html +
                                          '</dl><span class="arr"></span><span class="tl"></span><span class="tr"></span><span class="bl"></span><span class="br"></span></div>'   
                              }
                              
                              me.hide_last();
                              dt.find('.dcountries').show();
                              me.show(dt);
                              dt.find('.dsubgroups271').show();
                              me.show(dt);
                              dt.find('.dsubgroups304').show();
                              me.show(dt);

                              if(obj.tagName.toLowerCase()=='select') $(obj).parent().show();
                              
                              
                              dd.html(html)
                              
                              if (region == '271' && delivery_type == '2')
                              { 
                              ayaMap=new yaMap({
                                state:{
                                        center: [55.76,37.64],
                                        zoom:10
                                        },
                                id:"#self_items_map"+region,
                                go:false,
                                points:typeof yaMapsPoints!="undefined"?yaMapsPoints:null
                             });                           
                         
                             $("#combobox"+region ).combobox();
                             $('.level-2').children('dt').hide();                             
                             }
                             
                             if (region == '304' && delivery_type == '2')
                              { 
                              ayaMap=new yaMap({
                                state:{
                                        center: [59.935097, 30.312544],
                                        zoom:11
                                        },
                                id:"#self_items_map"+region,
                                go:false,
                                points:typeof yaMapsPoints!="undefined"?yaMapsPoints:null
                             });                           
                         
                             $("#combobox"+region ).combobox();
                             $('.level-2').children('dt').hide();
                           
                             
                             }
                           
                              $('dl.level-2 dt label input', dd).click(function() {
                                   me.check_delivery(this);
                              });
                              $('dl.level-3 dt label input', dd).click(function() {
                                   me.check_complectation(this);
                              });
                              
                              me.preloader.hide();
                              
                              if(handler) {
                                   handler();
                              }
                              
                              $('.price .rub', dd).html(me.currency_ticker);

                         });
                         
          },
          check_from_array: function( obj, id, handler) {
               
               $('#order_delivery_next').hide();
               $('.delivery-type input[name=delivery]').removeAttr('checked');
               $('.delivery-type input[name=complectation]').removeAttr('checked');
               
               
               
               id = id.split("-");
               
               region = id[0];
               country = (typeof id[1] !== 'undefined')  ? id[1]:region;
               if (region==0) {
                    
                    return this.show_countries(obj);;
               }
              
               var dt = $(obj).parents('dt');
               
               var dd = dt.next();


               if ($('#dregions'+region).length){
                    this.hide_last();
                    if(obj.tagName.toLowerCase()=='select') $(obj).parent().show();
                    
                    return this.show_region(region);;
               }
               
               
               if (obj.tagName.toLowerCase() !='select') { 
                    // если доставки уже есть
                    if (dd.html() != '') {
                         this.hide_last();
                         this.show(dt);
                         return false;
                    }
               }
               
               var me  = this; 
               data = region_deliveries[region] ;
             
               var html = '';
               var price = 0; var tmp; var count = 0; 
               var deliv_checked = '';
              
               for(var d in data) {
                    d_id = data[d];
                    d_name = deliveries_names[d_id];
                    d_desc = deliveries_desc[d_id];
                    
                    count++;
                    
                                   
                    //delivery_desc=$('#delivery_desc'+d_id).html() || '';
                                                   
                    html += '<dt id="dtdelivery'+region+'_'+d_id+'">'+
                         '<div class="col-1">'+
                              '<label for="ddelivery'+region+'_'+d_id+'"><input type="radio" name="delivery" value="'+region+'_'+d_id+'" id="ddelivery'+region+'_'+d_id+'" '+deliv_checked+'/>'+d_name+'</label>'+
                              '<p>'+d_desc+' </p> '
                         +'</div>'+
                         '<div class="col-2">'+
                         '</div>'+
                         '<div class="clear"></div>'+
                    '</dt>';
                                   
                    html += '<dd>'+
                         '<p>Способ комплектации при доставке<br/>курьером:</p>'+
                         '<dl class="level-3">';
                         
                    
                    html += '</dl></dd>';
               }
                              
                         if(html != '') {
                              html = '<div class="level-2"><dl class="level-2"> '
                                        + html +
                                     '</dl><span class="arr"></span><span class="tl"></span><span class="tr"></span><span class="bl"></span><span class="br"></span></div>'   
                         }

                         me.hide_last();
                         dt.find('.dcountries').show();
                         me.show(dt);

                         if(obj.tagName.toLowerCase()=='select') $(obj).parent().show();
                         
                         
                         dd.html(html)
                         $('dl.level-2 dt label input', dd).click(function() {
                              $('#order_delivery_next').show();
                         });
                         
                              

          },
          
          
          
          show_countries:function( obj ) {
                    this.hide_last();
                    
                    
                    var dt = $(obj).parent(); 
                    
                    
                    this.show_region( $('.dcountries select').val() );
                    
                    this.show(dt);
                    
                    $('.delivery-type .dcountries').show()
                    ;

                    return true;
          },
              
          show_sub_groups:function( obj, region ) {
                    this.hide_last();                  
                    
                    var dt = $(obj).parent(); 
                    
                    this.show(dt);
                    
                    $('.dsubgroups'+region).show();

                    return true;
          },
          
          toggle: function( dt ) {
               var dd = dt.next();
               if(dt.hasClass('selected')) {
                    this.hide(dt);
               }
               else {
                    this.show(dt);
               }
               return true;
          },

          
          show_region: function(region) {
              
              if(region ==1 ) {
                    this.show ( $('#dr1-1').parent() )
              } 
               
               $('#dregions'+region).show();
                    
               return true;
          }
                   
     }
     
     $(document).ready(function() {
          _$ . init();});                                 
     
     return  _$ ;                               
                               
}


var payments =  function() {
     
     var _$ = {
          init: function(){
               var obj = this;
               $('#payment-type-user input').click(function() {
                    obj.check_user(this);
               });
               $('#payment-type-sertificate input').click(function() {
                    obj.check_sertificate(this);
               });
               $('#payment-selected-sertificate input[name=paymethod]').click(function() {
                    obj.check_paymethod(this);
               });
               
               $('#payment-sertificate-submit').click(function() {
                    return obj.submit_sertificate(this);
               });
               
               $('#payment-additional').click(function() {
                    obj.add_payment(this);
                    return false;
               });
               
          },
          
          check_user: function(o) {
               var selected_paymethod =  $('#payment-selected-sertificate input[name=paymethod]:checked').val();
;
               
              
               if(o.value == 'Person') {
                    $('#payment-selected-user').show();
                    $('#payment-selected-user-l').hide();
               }
               else {
                    if(selected_paymethod == 6) {
                         $('#payment-selected-sertificate-error').html('Наложенный платеж только для физических лиц!');
                         
                         $('#payment-type-user-p').prop('checked', 'checked');
                         
                         return false;
                    }    
                    
                    $('#payment-selected-user').show();
                    $('#payment-selected-user-l').show();
               }
               
               return true;
          },
          
          check_sertificate: function(o) {
               if(order_product_price_all <=user_balance ) {
                    return false;
               }
               
               if(o.value == 'N') {
                    $('#payment-selected-sertificate').show();
                    $('#payment-selected-sertificate-yes').hide();
               }
               else {
                    $('#payment-selected-sertificate').show();
                    $('#payment-selected-sertificate-yes').show();
               }
          },
          
          check_paymethod: function(obj) {
               $('#payment-selected-sertificate-error').html('');
               
               $('#payment-selected-sertificate ul li blockquote').hide();
               
               var b = $(obj).parents('li').find('blockquote');
               
               if($.trim(b.html()) != '') {
                    b.show();
               }
               
               // наложенный платеж - только для физ.лиц
               if( obj.value == 6 ) {
                    if($('#payment-type-user-l')[0].checked) {
                         $('#payment-selected-sertificate-error').append('Наложенный платеж только для физических лиц!');
                         $('#payment-type-user-p')[0].click();
                    }

                    if( order_region == 271  || order_region == 304) {
                         $('#payment-selected-sertificate-error').append('В Москве и Санкт-Петербурге заказ идет по почте');
                    }
               }

               if ( typeof order_paymethods != 'undefined') 
               {
                    ticker_of_paymethod = Paymethods[obj.value].Currency.ticker;
                    $('.payable .rub').html(Paymethods[obj.value].Currency.ticker);
                    
                    $('#cost_amount').html(Paymethods[obj.value].Cost.amount+ ' <span class="rub">'+ticker_of_paymethod+'</span>');
                    $('#cost_with_discount').html(Paymethods[obj.value].Cost.with_discount+ ' <span class="rub">'+ticker_of_paymethod+'</span>');
                    $('#cost_discount').html(Paymethods[obj.value].Cost.discount+ '%');
                    $('#order_right_delivery_price').html(Paymethods[obj.value].Cost.delivery+ ' <span class="rub">'+ticker_of_paymethod+'</span>');
                    $('#order_right_price').html( Paymethods[obj.value].Cost.checkout + ' <span class="rub">'+ticker_of_paymethod+'</span>');
               }
          },
          
          submit_sertificate: function() {
               $('#payment-selected-sertificate-yes .error_message').html('');
               var series = $.trim($('#payment-sertificate-series').val());
               
               /*if(series == '') {
                    $('#payment-selected-sertificate-yes .error_message').html('Введите серию сертификата <br/>');;
                    return false;
               }*/
               
               
               var code = $.trim($('#payment-sertificate-code').val());
               
               if(code == '') {
                    $('#payment-selected-sertificate-yes .error_message').html('Введите код сертификата <br/>');;
                    return false;
               }
               
               
                    

               return true;
               
          },
          
          add_payment: function(obj) {
               $('#payment-additional-choose').show();
               
               return false;
          }
          
     }

     $(document).ready(function() {
          _$ . init();});                                 
     
     return  _$ ;                               
                               
}


function initPageSupplierEdit() {
     initTabs();
     
     $('#a_supplier_edit_file').click(function() 
     {
          $('#supplier_edit_file_list').prepend(
               "<div id='supplier_edit_file'>"+
               "<select name='imgtype[]'>"+
               "<option value=''> -- тип не указан -- </option>"+
               "<option value='cover'>Обложка</option>"+
               "<option value='inside'>Заглянуть внутрь</option>"+
               "</select> <input type='file' name='img[]'/> </div>");
     })
         
     $('#a_supplier_edit_file_format').click(function() 
     {
          $('#supplier_edit_file_formats_list').prepend(
               "<input type='file' name='efile[]'/><br/>");
     })
     
     
     supplierLoadCatsByParent(0);
     supplierLoadAuthors();
     supplierLoadSeries();
     
     initTinyMCE({
          "mode":"exact",
          "element":"annotation",
          b1: ['code, fontsizeselect, forecolor'],
     });
     
     initTinyMCE({
          "mode":"exact",
          "element":"short_text",
          b1: ['code, fontsizeselect, forecolor'],
     });
     
     $('a.ajax_link').click(function (event) 
    { 
       event.preventDefault(); 

       $(this).closest( "div.sortable-item" ).hide();
       var url = $(this).attr('href');
       $.get(url, function(data) {
         //alert(data);
        });

     });
 

     
}

function initPageCustomerProductsEdit() {
     initTabs();
     
     $('#a_supplier_edit_file').click(function() 
     {
          $('#supplier_edit_file_list').prepend(
               "<div id='supplier_edit_file'>"+
               "<select name='imgtype[]'>"+
               "<option value=''> -- тип не указан -- </option>"+
               "<option value='cover'>Обложка</option>"+
               "<option value='inside'>Заглянуть внутрь</option>"+
               "</select> <input type='file' name='img[]'/> </div>");
     })
     
     
     supplierLoadCatsByParent(0);
     supplierLoadAuthors();
     supplierLoadSeries();
     
     initTinyMCE({
          "mode":"exact",
          "element":"annotation",
          theme_advanced_buttons1 : "images, bold,italic,underline,separator,bullist,numlist",
     });
     
     initTinyMCE({
          "mode":"exact",
          "element":"contents",
          theme_advanced_buttons1 : "images, bold,italic,underline,separator,bullist,numlist",
     });
         
     
}

function supplierLoadAuthors() {
     $('#suppier_edit_autor_search').click(function ()
     {
          var value = $('#suppier_edit_autor').val();
          
          var search_by = 'ru_last_name';
          
          if($('#suppier_edit_autor_bycod').prop('checked') == true) 
               search_by = 'id';
               
          
          var obj = $('#suppier_edit_autor_list');
          var obj_selected = $('#suppier_edit_autor_selected');
          $.getJSON('/ajax/get_authors.php?q='+value+'&by='+search_by, function(data) {
               obj.html('');
               for(var i in data) {
                    obj.append(
                         '<div><input type="checkbox" id="author'+i+'"/>  <a target="_blank" href="/author/-'+i+'/">' + data[i].fullname + '</a> ('+i+') - товаров '+data[i].items_cnt+'</div>'
					);
               }
               
               $('input',obj).click( function( ) {
                    var t = $(this).parent().remove();
                   
                    t.find('input').attr('name', 'authors[]').attr('value', this.id.replace('author', '')).removeAttr('id');
                    
                    obj_selected.append(t);
                    
                    obj_selected.find('p').hide();

               });
          });
          
          
          return false;     
     }     
     );
}

function supplierLoadSeries() {
     $('#supplier_edit_series_search').click(function ()
     {
          var value = $('#suppier_edit_series').val();
              
          var obj = $('#suppier_edit_series_list');
          var obj_selected = $('#suppier_edit_series_selected');
          $.getJSON('/ajax/get_series.php?q='+value+'', function(data) {
               obj.html('');
               for(var i in data) {
                    obj.append(
                         '<div><input type="checkbox" id="series'+i+'"/>  ' + data[i] + ' ('+i+')</div>'
                    );
               }
               
               $('input',obj).click( function( ) {
                    var t = $(this).parent().remove();
                   
                    t.find('input').attr('name', 'series[]').attr('value', this.id.replace('series', '')).removeAttr('id');
                    
                    obj_selected.empty().append(t);
                    
                    obj_selected.find('p').hide();
               });
          });
          
          
          return false;     
     }     
     );
}

     
function supplierLoadCatsByParent(cat_id) {
     
     
     var table = document.getElementById("supplier_product_Cat_list");
     var table_sel = document.getElementById("supplier_product_Cat_selected");
     
     
     
     $.getJSON('/ajax/get_categories.php?subcategory='+cat_id, function(data) {
          var tr;
          table.innerHTML ='';
          data.list = data.list||{};
          data.parent = data.parent||{};
          
           tr = document.createElement('tr');
      
           td_link =document.createElement('td');
          td_check =document.createElement('td');
          td_link.className = 'parent';
          td_link.innerHTML = "Категории раздела &laquo;<a href='/subcategory.php?subcategory="+i+"' target='_blank'>"+data.parent.category + "</a>&raquo;";
          
          if(data.parent.parent)
               td_check.innerHTML = "<a href='' onclick='return supplierLoadCatsByParent("+data.parent.parent+");'>Вверх</a>";
               
          tr.appendChild(td_link);
          tr.appendChild(td_check);
          table.appendChild(tr);
          
          if (data.list.length == 0) 
          {
                    tr = document.createElement('tr');
                    td_link =document.createElement('td');
                    td_link.className = 'link';
                    td_link.innerHTML = "Подкатегорий нет";
                    tr.appendChild(td_link);
                    table.appendChild(tr);
          }
          else {
               for (var i in data.list) {
                    tr = document.createElement('tr');
                    
                    td_link =document.createElement('td');
                    td_check =document.createElement('td');
                    
                    td_link.className = 'link';
                    td_link.innerHTML = "<a href='/subcategory.php?subcategory="+i+"' target='_blank' onclick='return supplierLoadCatsByParent("+i+");'>"+data.list[i] + "</a>";
                    
                    var checked = '';
                    
                    if($('#cat_sel'+i)[0])
                    {
                         checked='checked="checked"';
                    }
                    
                    td_check.innerHTML = '<input type="checkbox" '+checked+' id="cat'+i+'">';
                    
                    tr.appendChild(td_link);
                    tr.appendChild(td_check);
                    
                    table.appendChild(tr);
                    
                    $('input', td_check).click(function() {
                         var id = +this.id.replace('cat', '');
                         if(!this.checked) {
                              $('#cat_sel'+id).remove();
                              return;
                         }
                         
                         $("#no_cat_selected").hide();
                         var tr = $(this).parent().parent().clone();
                         
                         tr[0].id = 'cat_sel'+this.id.replace('cat', '');
                         
                         $('input',tr).removeAttr('id').attr('name', 'category[]').attr('value', this.id.replace('cat', '')).click(function() {
                              $(this).parent().parent().remove();
                              $('#cat'+id).removeAttr('checked');
                         });
                         
                         table_sel.appendChild(tr[0])
                    })

               }
          }
          
          
          //alert(table.innerHTML);
     });
     return false;
     
     }
///////////////////////////////////////////////////////////////////////////
     
function init_order_view_page()
{
     var $black = $('div.black');
     var $appeared = $('#cancel_reason');
     $('a.order-cancel').click(function()
     {
          $black.fadeIn(0).fadeTo(0, 0).fadeTo(500, 0.5);
          
          windowWidth = $(window).width();

          popupWidth = $appeared.width();
          popupLeft = (windowWidth - popupWidth) / 2 + "px";
          $appeared.css({'left':popupLeft});
          $appeared.fadeIn(500);
          $appeared.show();
          return false;
     });
     restore = function()
     {
          $appeared.hide();
          $black.fadeOut(250);
          return false;
     }
     $black.click(restore);
     $('#btn_no_cancel').click(restore);
}
///////////////////////////////////////////////////////////////////////////

function Window(el) {
     if(!document.getElementById(el)){
          return;
     }
     
     var obj = document.getElementById(el);
     
     //var back_fon = 
     
     var r = {
          close: function() {
               $('div.black').fadeOut(250);
               $('div.white').fadeOut(250);
          },
          
          show:function() 
          {
               $('div.black').fadeIn(0);
               $('div.black').fadeTo(0, 0);
               $('div.black').fadeTo(500, 0.5);
               
               if (is_ie6 || is_ie7) {
                    $(obj).fadeIn(0);
                    blockWidth = $('div.block', obj).children('div').width() + 10 + "px";
                    $(obj).css({'width':blockWidth});
                    $(obj).fadeOut(0);
               }
               
               windowWidth = $(window).width();
			   windowHeight = $(window).height();
               popupWidth = $(obj).width();
			   popupHeight = $(obj).height();
               popupLeft = (windowWidth - popupWidth) / 2 + "px";
			   popupTop = getPageScroll()[1] + (getPageHeight() / 10) + "px";
               $(obj).css({'left':popupLeft, 'top':popupTop});
               $(obj).fadeIn(500);
          }, 
          
          set_content: function(content) {
               $('div.block', obj).html(content);
               
               return this;
          }
     }
     
     $('div.black').click(function(){
          r.close()
     });
     $('div.white span.close').click(function(){
          r.close()
     });

     return r;
}


function Windowpopup(el) {
     if(!document.getElementById(el)){
          return;
     }
     
     var obj = document.getElementById(el);
     
     //var back_fon = 
     
     var r = {
          close: function() {
               $('div.black').fadeOut(250);
               $('div.whitepopup').fadeOut(250);
          },
          
          show:function() 
          {
               $('div.black').fadeIn(0);
               $('div.black').fadeTo(0, 0);
               $('div.black').fadeTo(500, 0.5);
               
               if (is_ie6 || is_ie7) {
                    $(obj).fadeIn(0);
                    blockWidth = $('div.block', obj).children('div').width() + 10 + "px";
                    $(obj).css({'width':blockWidth});
                    $(obj).fadeOut(0);
               }
               
               windowWidth = $(window).width();
			   windowHeight = $(window).height();
               popupWidth = $(obj).width();
			   popupHeight = $(obj).height();
               popupLeft = (windowWidth - popupWidth) / 2 + "px";
			   popupTop = getPageScroll()[1] + (getPageHeight() / 10) + "px";
               $(obj).css({'left':popupLeft, 'top':popupTop});
               $(obj).fadeIn(500);
          }, 
          
          set_content: function(content) {
               $('div.block', obj).html(content);
               
               return this;
          }
     }
     
     $('div.black').click(function(){
          r.close()
     });
     $('div.whitepopup .close').click(function(){
          r.close()
     });

     return r;
}

// getPageScroll() by quirksmode.com
  function getPageScroll() {
    var xScroll, yScroll;
    if (self.pageYOffset) {
      yScroll = self.pageYOffset;
      xScroll = self.pageXOffset;
    } else if (document.documentElement && document.documentElement.scrollTop) {	 // Explorer 6 Strict
      yScroll = document.documentElement.scrollTop;
      xScroll = document.documentElement.scrollLeft;
    } else if (document.body) {// all other Explorers
      yScroll = document.body.scrollTop;
      xScroll = document.body.scrollLeft;
    }
    return new Array(xScroll,yScroll)
  }

  // Adapted from getPageSize() by quirksmode.com
  function getPageHeight() {
    var windowHeight
    if (self.innerHeight) {	// all except Explorer
      windowHeight = self.innerHeight;
    } else if (document.documentElement && document.documentElement.clientHeight) { // Explorer 6 Strict Mode
      windowHeight = document.documentElement.clientHeight;
    } else if (document.body) { // other Explorers
      windowHeight = document.body.clientHeight;
    }
    return windowHeight
  }

  
  
function initAjaxContent(element, alias) 
{
     $('#'+element).click(function()
     { 
          ( Window('window_user_agreement') ).show();

          return false;
     });
}

function init_stage_personal()
{
     init_register();
     $(".choicer").click(function(){
          $register = $("#yes_personal");
          if ((this.checked) && 'yes' == this.value)
          {
               $register.addClass("active");
          }
          else
          {
               $register.removeClass("active");
          }
     }
     );
}


/*According*/
$(document).ready(function() {
     //return;
     var a = $(".isbn-list-arrow a, .isbn-list-arrow img");                   
     var down = $(".isbn-list li.down");
     var up = $(".isbn-list li.up ");
     var according_block = $(".additional_data")
     a.live("click", function() {
          according_block.slideToggle(800);
          return false;
     })
     down.click(function() {
          $(".isbn-list li.down").css({'display':'none'});
          $(".isbn-list li.up").css({'display':'block'});
     })
     up.click(function() {
          $(".isbn-list li.up").css({'display':'none'});
          $(".isbn-list li.down").css({'display':'block'});
     })
     
     $(".more-links li.down, .more-links li.up").live("click", function() {
          $(".note").css('display')=='none' ? $('.note').show():$(".note").hide();
          $(".all_note").toggle();
          return false;
     })
         
     $(".more-links li.down ").click(function() {
          $(".more-links li.down").css({'display':'none'});
          $(".more-links li.up").css({'display':'block'});
     })
     $(".more-links li.up ").click(function() {
          $(".more-links li.up").css({'display':'none'});
          $(".more-links li.down").css({'display':'block'});
     })
         
     
     $(".more-links-editions li.down, .more-links-editions li.up").live("click", function() {
		  var editions_annotatiom_id = this.id.replace('li_annot','')          
          var editions_annotatiom_note = $('#note'+editions_annotatiom_id);
          var editions_annotatiom_all_note = $('#all_note'+editions_annotatiom_id);
          
          editions_annotatiom_note.css('display')=='none' ? editions_annotatiom_note.show():editions_annotatiom_note.hide();
          editions_annotatiom_all_note.toggle();
          return false;
     })
         
     $(".more-links-editions li.down").click(function() {
          
          var editions_annotatiom_id = this.id.replace('li_annot','')          
          var editions_annotatiom_more_down = $(".more-links-editions li#li_annot"+editions_annotatiom_id+".down");
          var editions_annotatiom_more_up = $(".more-links-editions li#li_annot"+editions_annotatiom_id+".up");
          
          editions_annotatiom_more_down.css({'display':'none'});
          editions_annotatiom_more_up.css({'display':'block'});
     })
     $(".more-links-editions li.up").click(function() {
          var editions_annotatiom_id = this.id.replace('li_annot','')          
          var editions_annotatiom_more_down = $(".more-links-editions li#li_annot"+editions_annotatiom_id+".down");
          var editions_annotatiom_more_up = $(".more-links-editions li#li_annot"+editions_annotatiom_id+".up");
          
          editions_annotatiom_more_up.css({'display':'none'});
          editions_annotatiom_more_down.css({'display':'block'});
     })
     
     
})
// Tabs new
function submenu(element){
     return function(){
          var el
          if(element)
               el = document.getElementById(element)
          else
               el = this
          tabIndex = $('ul.catalogitem-tabs li a').index(el);
          newTab = $('div.tab')[tabIndex];
          newLink = $('ul.catalogitem-tabs li')[tabIndex];
          
          /*if($.browser.opera){
               $('div.tabs table tbody tr td').css({'border-bottom':'none','padding-bottom':'1px'});
          }*/
          $('ul.catalogitem-tabs li').removeClass('active');
          $(newLink).addClass('active');
          
          if($.browser.msie){
               $('div.tab:visible').fadeOut(0, function(){
                    $(newTab).fadeIn(0);
               });
          } else {
               $('div.tab:visible').fadeOut(300, function(){
                    $(newTab).fadeIn(300);
               });
          }
          return false;
     }
}
$(document).ready(function() {
     $('ul.catalogitem-tabs li a').click(submenu());
     $('ul.stars').click(submenu('comments'));
     $('a.leave-recall').click(submenu('comments'));
     $('a.open-editions').click(submenu('editions'));
});  // Dropdown

$(document).ready(function() {
     $( document ).click(function(e){
          if($(e.target).parents("div.search_list").length==0 && $(e.target).parents("div.field span.everywhere").length==0) {
               $('div.search_list').hide();     
          }
          
     })
     $('div.field span.everywhere').click(function(){
          $('div.search_list').show();
     });
     $('div.search_list a.close').click(function(){
          $('div.search_list').hide();
     })
     $('div.search_list ul li a').click(function(){
          id = this.id.replace('inlinesearch_where_','')
          
          $('#inlinesearch_where').val(id );
          $('#inlinesearch_where_text span').html( this.innerHTML);
          $('div.search_list').hide();
          
          
          return false;
     })
     
})

//hover eyes

$(document).ready(function() {
     
     $('div.hover, div.mybooks').mouseenter(function(){
           logo_src = $('img.logo').attr('src');
           logo_src = logo_src.split('.gif');
           logo_src_hover = logo_src[0] + '_hover.gif';
           $('img.logo').attr('src', logo_src_hover);
     });
     $('div.hover, div.mybooks').mouseleave(function(){
           logo_src = $('img.logo').attr('src');
           logo_src = logo_src.split('_hover.gif');
           logo_src_hover = logo_src[0] + '.gif';
           $('img.logo').attr('src', logo_src_hover);
     });
     
     
})


//clipboard
<!--
function copy_clip(meintext)
{
 if (window.clipboardData) 
   {
   // для IE
   window.clipboardData.setData("Text", meintext);
   }
   else if (window.netscape) 
   { 
     try {
     if (netscape.security.PrivilegeManager.enablePrivilege)
        netscape.security.PrivilegeManager.enablePrivilege('UniversalXPConnect');
        // netscape.security.PrivilegeManager.enablePrivilege('UniversalBrowserRead');
        // netscape.security.PrivilegeManager.enablePrivilege("UniversalBrowserWrite")
     } catch (e) {alert('Настройка безопасности браузера не позволяет обращаться к буферу обмена!\n'+e); return;}

        var clip = Components.classes['@mozilla.org/widget/clipboard;1']
                          .createInstance(Components.interfaces.nsIClipboard);
        //alert(clip);
        if (!clip) return;
        
        var trans = Components.classes['@mozilla.org/widget/transferable;1']
                           .createInstance(Components.interfaces.nsITransferable);
        if (!trans) return;
        
        trans.addDataFlavor('text/unicode');
        
        var str = new Object();
        var len = new Object();
        
        var str = Components.classes["@mozilla.org/supports-string;1"]
                         .createInstance(Components.interfaces.nsISupportsString);
        
        var copytext=meintext;
        
        str.data=copytext;
        
        trans.setTransferData("text/unicode",str,copytext.length*2);
        
        var clipid=Components.interfaces.nsIClipboard;
        
        if (!clip) return false;
        
        clip.setData(trans,null,clipid.kGlobalClipboard);
   
   }
   alert("В буфер обмена сохранено:\n\n" + meintext);
   return false;
}
//-->


function initProfilePhotoUpload() 
{
     jQuery('#profile_photo').change(function() {
          $('#profile_form').trigger('submit');
     });
}
function initProfilePhotoCrop() 
{
     
}

function popupwindow(text, width, type) 
{
    width = typeof width !== 'undefined' ? width : 320;
    type = typeof type !== 'undefined' ? type : 'normal';
    $('#window_popup .block #popup_space').html(text);
    $('#window_popup').width(width);
    $('#window_popup .block #popup_space').width(parseInt(width)-10);
    if (type == 'slim') {$('#window_popup').addClass("slim");}
    else if (type == 'noborder') {$('#window_popup').addClass("noborder");}
    else {
        $('#window_popup').removeClass("slim");
        $('#window_popup').removeClass("noborder");
    }
    Windowpopup('window_popup').show();
    return false;
}


var window_once_showed = 0
function popupwindow_once(text) 
{
    if (window_once_showed == 1) return true;
    window_once_showed = 1
    $('#window_popup .block #popup_space').html(text);
    Windowpopup('window_popup').show();
    return false;
}

$(document).ready(function(){
	$("#author_annotation_button").click(function (){
		$("#author_annotation").css("display","none");
		$("#author_annotation_edit").css("display","block");
		initTinyMCE({
          "mode":"exact",
          "element":"author_annotation_edit_area",
           b1: ['code, fontsizeselect, forecolor'],
        });
	});
	$("#author_annotation_save").click(function (){
		$("#author_annotation").css("display","block");
		$("#author_annotation_edit").css("display","none");
		tinyMCE.triggerSave();
		var annotation = $("#author_annotation_edit textarea").val();
		var ru_first_name = $("#author_ru_first_name_edit_area").val();
		var ru_last_name = $("#author_ru_last_name_edit_area").val();
		var id = $("#author_id").val();
				$.ajax({
				url: '/ajax/save_author_annotation.php',
				type: 'POST',
				data: 'id='+id+'&annotation='+encodeURIComponent(annotation)+'&ru_first_name='+encodeURIComponent(ru_first_name)+'&ru_last_name='+encodeURIComponent(ru_last_name)+($("input#set_revised").is(':checked') ?'&set_revised=Y':'')
                })
                  .done(function( data ) {
                    //$("#author_annotation").html(annotation);
					//$("#author_name_area").html(ru_first_name+" "+ru_last_name);
                    window.location.reload(true);
                  })
                ;
	});	
    
    var delay = (function(){
      var timer = 0;
      return function(callback, ms){
        clearTimeout (timer);
        timer = setTimeout(callback, ms);
      };
    })();
    
    $('input#cart_cnt_id').bind('change keyup', function () {
        if ($(this).val() && isNaN( $(this).val() )) {
            $(this).val('1')
        }
        if ($(this).val()) {
            delay(function(){
              $('#cart_form').submit();
            }, 4000 );
        }
    });
    
    $(".mobile_version_b").click(function (e){
		e.preventDefault();
        $.removeCookie("fv", { path: '/', domain: '.books.ru' });
        window.location = window.location.href.replace(/www\.books\.ru/, 'm.books.ru');        
	}); 
    
    $(document).on('click', 'a.add_to_cart_ajax', function (e) {
        e.preventDefault();
        var a_tag = $(this);
        var url = $(this).attr('href');
        a_tag.css({'cursor' : 'wait'});
        $(document.body).css({'cursor' : 'wait'});
        $.get( url+'&ajax=1', function( data ) {
          $( "div.cart_state" ).html( data.cart_state );
          if ($(a_tag).find("img[src$='tobasket-mini.gif']").length || $(a_tag).find("img[src$='tobasket-mini-hover.gif']").length ) 
            a_tag.replaceWith('<a rel="nofollow" href="/cart.php"  title="Перейти в корзину"><img src="/static/images/buttons/goto-basket-mini.gif" alt="перейти в корзину" title="перейти в корзину"  /></a>');
          if ($(a_tag).find("img[src$='tobasket.gif']").length || $(a_tag).find("img[src$='tobasket-hover.gif']").length) 
            a_tag.replaceWith('<a rel="nofollow" href="/cart.php"  title="Перейти в корзину"><img src="/static/images/buttons/goto-basket.gif" alt="перейти в корзину" title="перейти в корзину"  /></a>');
          a_tag.css({'cursor' : 'default'});
          $(document.body).css({'cursor' : 'default'});
        }, "json" );
       
    });
    
});


function __highlight(s, t) {
    if (s == null) return s; 
    var matcher = new RegExp("(" + $.ui.autocomplete.escapeRegex(t) + ")", "ig");
    return s.replace(matcher, '<strong>$1</strong>');
}

function subscribeXpopUp() {
    var $form = $('.getFileFormSubscribe');
    if(! $form[0].checkValidity()) {
        $('<input type="submit">').hide().appendTo($form).click().remove();
    } else {        
        var emailAddres = $(".getFileFormSubscribe input[type = email]").val();
        var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
        if (regex.test(emailAddres)) {
            $.post('/ajax/process_modal.php', $form.serialize(), function (response) {
                $("#subpop").html('<p style="font: 400 18px/30px &quot;Roboto&quot;,Arial,sans-serif; padding: 10px 0; text-align:center">'+response.result+'</p><p style="text-align:center"><img src="/static/images/success.png"></p>');
            }, "json")
        } else {
            $(".errorinfo").show();
            $(".errorinfo").html("Введите корректный Email");
        }
    }
}
    
function closeXpopUp() {
    $('.popup_filler').hide();
}

$(document).ready(function(){
    autocomplete_input = $("input[name='s[query]']").autocomplete(
        {
        source : function(request, response) {
            $.ajax({
            url: '/ajax/search_autocomplete.php',
            type: 'POST',
            dataType : 'json',
            data : {
                term : request.term
            },
            
            success : function(data) {
                response($.map(data.rows, function(item) {
                return {
                    title : __highlight(item.title, request.term),
                    url : item.url,
                    picture : item.picture,
                    author : __highlight(item.author, request.term),
                    price_promo : item.price_promo,
                    price_effective : item.price_effective,
                    ticker : item.ticker,
                    is_avail : item.is_avail,
                    id : item.id,
                };
                }));
                //See all results
                $('.ui-autocomplete').append('<li class="last_li small_grey">'+(data.is_use_suggested ? 'Показаны результаты по запросу <b>'+ data.suggest +'</b><br>':'')+'<a href="#" onclick="return false">Показать все результаты ['+ data.total +']</a></li>'); //See all results
            }
            });
        },
        minLength : 3,
        delay: 1000,
        search  : function(){
            autocomplete_input.autocomplete('close');
        },
        open: function(event, ui) {
            //
        },
        select : function(event, ui) {
            //$('#inlinesearch').submit();
        }
        }).keydown(function(e) {
        if (e.keyCode === 13) {
            $("#inlinesearch").trigger('submit');
        }});
        
    autocomplete_input.autocomplete( "widget" ).addClass( "autocomplete_s" );
    
    if ( autocomplete_input.data('uiAutocomplete') ) {
       // do what you want with the autoComplete object. below is the changed version of an example from jqueryUI autocomplete tutorial

       autocomplete_input.data('uiAutocomplete')._renderItem = function(ul, item) {
            return $("<li>")
                .append('<a href="'+item.url+'"><table><tr><td width="60">' + (item.picture?'<img width="50" src="' + item.picture + '">':'') + 
                '</td><td class="descr_s">' + item.title + (item.author?'<br><span class="small_grey">'+item.author+'</span>':'') + '</td><td width="110" class="opinions">' +										 
                (item.is_avail ? '<p class="deliv_ok">В&nbsp;продаже</span></p>':'<p class="deliv_error">Нет&nbsp;в&nbsp;продаже</span></p>') +                
                '</td></tr></table></a>')
                .appendTo(ul);
        };
    }
    
    $('body').on('click', 'li.last_li', function (){
        $('#inlinesearch').submit();
    });    
    
    $('body').on('click', function (e) {
        $('.opentip-container').each(function () {
        // hide any open popovers when the anywhere else in the body is clicked
            $(this).hide();
        });
   });
         
    $(".popup_content").click(function(e) {
            e.stopPropagation();
    });    
   
   $('.getFileFormSubscribe').on('keyup keypress', function(e) {
      var keyCode = e.keyCode || e.which;
      if (keyCode === 13) { 
        subscribeXpopUp();
        return false;
      }
    });
   

});
