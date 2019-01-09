addEvent(window,'load',function() {
    var protocol = location.href.match(/^https/i) ? 'https://' : 'http://';
    var img = new Image();
    img.src = protocol+'counter.yadro.ru/hit?t26.6;r'+escape(document.referrer)+((typeof(screen)=='undefined')?'':';s'+screen.width+'*'+screen.height+'*'+(screen.colorDepth?screen.colorDepth:screen.pixelDepth))+';u'+escape(document.URL)+';'+Math.random();
});

function addEvent(object, event, handler){
    if(object.addEventListener)
        object.addEventListener(event, function(e){handler(object, e);}, false );
    else if(object.attachEvent)
        object.attachEvent('on'+event, function(e){handler(object, e);});
    else
        object['on' + event] = function(e){handler(object, e);}
}