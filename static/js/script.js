
        function reszie(){
            var height = $(window).height();
            var width = $(window).width();
            var HEIGHT = 800;
            var WIDTH = 1280;
            if (height / width > HEIGHT / WIDTH){
                var w = width;
                var h = HEIGHT/WIDTH * w;
                $("#wrap").css("height", h+"px");
                $("#wrap").css("width", w+"px");
            }
            else{
                var h = height;
                var w = WIDTH/HEIGHT * h;
                $("#wrap").css("width", w+"px");
                $("#wrap").css("height", h+"px");
            }
        }

        $(window).resize(function(){
            reszie();
        });
        $(document).ready(function(){
            reszie();
        });
