$(document).ready(function() {
            
    $("#who").click(function() {
        $("#an1").toggle(500)
        n = $(document).height() + 50
        $('html, body').animate({ scrollTop: n}, 500);
    })

    $("#do").click(function() {
        $("#an2").toggle(500)
        n = $(document).height() + 50
        $('html, body').animate({ scrollTop: n}, 500);
    })

    
    $.get(
        "https://youtube.googleapis.com/youtube/v3/playlistItems" ,
        {part:"snippet",
        playlistId:"UUZhoQ7RWid75KCcWNsBIy5A",
        maxResults:4,
        key:"AIzaSyA7JknPY7wFkJPNqPinAQJBQn2rgFQxpoU"},
        function(data) {
            $.each(data.items,function (i,item) {
                var vedioId =  item.snippet.resourceId.videoId ,
                vedioTiele =  item.snippet.title ,
                thumbNailImg = item.snippet.thumbnails.standard.url ;

                var veideoHtml = 
                `<div style="display: inline-block; padding:10px;">
                <a href="https://www.youtube.com/watch?v=${vedioId}" target=”_blank">
                <img src="${thumbNailImg}" alt="thumbNailImg" class="img-thumbnail" style="width:300px">
                <br>
                <div style="width:300px; display: inline-block;">${vedioTiele} <div>
                </a>
                </div>`;

                $(veideoHtml).appendTo('#video');
            });

        });




});