$(document).ready(function(){
    $("#Male").click(function(){
        window.location.href="page2.html";
    });
    $("#Female").click(function(){
        window.location.href="page2.html";
    });
    $("header").hover(function(){
        $("header").css("cursor","pointer");
    });
});