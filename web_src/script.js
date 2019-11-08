const onLoad = function(){
    
    var apps = document.querySelectorAll('.app');
    var app_entry = [];

     //loop through each exp entry DOM ref
     var len = apps.length;
     var i = 0;
 
     //Add the DOM's info as an object to array
     for(; i < len; i++){
        
         var tmp = {
             begin: apps[i].getBoundingClientRect().top + window.pageYOffset,
             end: apps[i].getBoundingClientRect().top + window.pageYOffset + apps[i].clientHeight,
             ref: apps[i].getElementsByClassName("id_num")[0],
             follow: function(){
                if( window.pageYOffset > this.begin && window.pageYOffset < this.end - 100 ){
                    this.ref.style.opacity = 1;
                }
                else{
                    this.ref.style.opacity = 0;
                }
            }
         }
        app_entry.push(tmp);
     }


    window.addEventListener('scroll', function(){
        this.window.requestAnimationFrame(function(){
            app_entry.forEach(function(e){
                e.follow();
            })
        })  
    })

}

window.addEventListener('load', onLoad());

