///////////////////// variable declarartion part //////////////////////////////
var charStart = 140;
var charsCurrent = 0;
var nextPage = null;
////////////////////// END ///////////////////////////////////////////////////

///////////////////  Stock Pre Written Functions //////////////////////////////

function getParameterByName( name ){
    name = name.replace(/[\[]/,"\\\[").replace(/[\]]/,"\\\]");
    var regexS = "[\\?&]"+name+"=([^&#]*)";
    var regex = new RegExp( regexS );
    var results = regex.exec( window.location.href );
    if( results == null )
        return "";
    else
        return decodeURIComponent(results[1].replace(/\+/g, " "));
}

//////////////////////////  END ///////////////////////////////////////////////

///////////////////////// UPDATE HASHLINK FUNCTION ////////////////////////////

function updateHashLinks(){
    $(".media-body").each(function (index, data) {
       var hashTagRegex = /(^|\s)#([\w\d-]+)/g
       var newText = $(this).html().replace(hashTagRegex, "$1<a href='/tags/$2/'>#$2</a>")
       
       //console.log($(data).text());
       // $(this) and $(data) is interchangable here
       // whenever we need to call a function 
       // on a html element we enclose it with
       // $() in jquery 
       // $(this)   inside a each function
       // means the each returned data itself

       $(data).html(newText); // $(this) is interchangable here
    });
}


//////////////////////// END /////////////////////////////////////////////////

///////////////////////// Tweet Process and attach part ////////////////////////////

function fetchTweets(url) {

    var requestUrl;

    if (!url){
        requestUrl = "/api/tweet/";
    }else{
        requestUrl = url;
    }

    query = getParameterByName("q");
    console.log(query);

    $.ajax({
        url: requestUrl,
        data: {
            "q": query
        },

        method: "GET",

        success: function(data) {
            nextPage = data.next;

            if (nextPage == null){
                $(".load-more").css("display", "none");
            }
            parseTweets(data.results)
            updateHashLinks();
        },

        error: function (data) {
            console.log("ERROR");
            console.log(data);
        }
    });

}


function parseTweets(tweetlist) {

    if (tweetlist == 0){
        $("#tweetlist").text("No Tweets Found");
    }else{

        $.each(tweetlist, function (index, object) {
            attachTweets(object, false);
        });
    }
    
}

function attachTweets(value, prepend) {
    var content = value.content;
    var user = value.user;
    var date_field = value.date_display;
    var formattedHtml = "<div class=\"media\">"+
                            "<div class=\"media-body\">"+
                                "Is Retweet: " + value.is_retweet + "<br/><br/>"
                                content + "<br/>"+
                                "via " + "<a href='"+user.url+"'>"+ user.username +"</a>" + " | " + date_field + " | " + "<a href='"+ value.tweet_url +"'>View</a>"+
                            "</div>"+
                        "</div>" +
                        "<hr>"


    if (prepend === true){
        $("#tweetlist").prepend(formattedHtml);
    }
    else{
        $("#tweetlist").append(formattedHtml);
    }
    
}

//////////////////////////////  END ////////////////////////////////////////////

//////////////////////////  Ajax Tweet Part ////////////////////////////////

$("#tweetForm").submit(function(event){

    // prevents a form's default sunmit function
    event.preventDefault();

    var thisForm = $(this);
    var FormData = thisForm.serialize();

    if (charsCurrent >= 0){

        $.ajax({
            url: "/api/tweet/create/",
            data: FormData,
            method: "POST",

            success: function(data) {
                thisForm.find("input[type=text], textarea").val("");
                attachTweets(data, true);
                updateHashLinks();
            },

            error: function(data) {
                console.log("ERROR");
                console.log(data.status);
                console.log(data.statusText);
            }
        });

    }else{
        alert("Tweet Too long type something shorter");
    }

});

////////////////////// END ///////////////////////////////////////////////

////////////////////////// Character limit part ////////////////////////////////////////////

$("#tweetForm").append("<span id='tweetCharsleft'>"+ charStart +"</span>");

$("#tweetForm textarea").keyup(function (event) {
    //console.log(event.key, event.keyCode, event.timeStamp);
    var tweetVal = $(this).val();
    charsCurrent = charStart - tweetVal.length;
    var spanText = $("#tweetCharsleft");
    spanText.text(charsCurrent);
    
    if (charsCurrent === 0){
        spanText.removeClass("red-class");
        spanText.removeClass("green-class");
        spanText.addClass("grey-class");
    }
    else if (charsCurrent > 0){
        spanText.removeClass("red-class");
        spanText.removeClass("grey-class");
        spanText.addClass("green-class");
    } else if (charsCurrent < 0){
        spanText.removeClass("grey-class");
        spanText.removeClass("green-class");
        spanText.addClass("red-class");
    }
});

/////////////////////////// END /////////////////////////////////////////////////

////////////////////////// Load More Part /////////////////////////////////////


$(".load-more").bind("click", function (event) {
   event.preventDefault();
   if (nextPage){
       fetchTweets(nextPage);
   }


});


///////////////////////////// END /////////////////////////////////////////////

///////////////  Document Body Part //////////////////////////
$(document).ready(function() {
    
    fetchTweets();
});

///////////// END /////////////////////////////////////////////