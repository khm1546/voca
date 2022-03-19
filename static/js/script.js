
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

            $(".cp-btn").click(function (){
                var chapIdx = $(this).index();
                var classCheck = $(this).attr("class").split(" ")[0];
                $(".cp-btn").each(function (){
                   var chapClass = $(this).attr("class").split(" ")[1];
                    var testClass = $(this).attr("class").split(" ")[0];
                    if(testClass == "chapter-btn"){
                         $(this).attr("src", "/static/images/chapter" + chapClass.replaceAll("chapter", "") + "-not.png")
                    }else if(testClass == "chapter-btn-long"){
                          $(this).attr("src", "/static/images/chapter" + chapClass.replaceAll("chapter", "") + "-long-not.png")
                    }
                });
                if(classCheck == "chapter-btn"){
                     $(this).attr("src", "/static/images/chapter" + (chapIdx + 1) + "-com.png")
                }else if(classCheck == "chapter-btn-long"){
                     $(this).attr("src", "/static/images/chapter" + (chapIdx + 1) + "-long-com.png")
                }

            });
        });